#█ ███    ███ ██████   ██████  ██████  ████████ ███████ 
#█ ████  ████ ██   ██ ██    ██ ██   ██    ██    ██      
#█ ██ ████ ██ ██████  ██    ██ ██████     ██    ███████ 
#█ ██  ██  ██ ██      ██    ██ ██   ██    ██         ██ 
#█ ██      ██ ██       ██████  ██   ██    ██    ███████ 


from constructs import Construct    # needed for CDK
from aws_cdk import (
    Stack,                          # needed for CDK
    aws_ec2 as ec2,                 # for creating the network
    aws_backup as backup,           # for creating backup plan
    Duration,                       # for configuring backup rule
    aws_events as events,           # to schedule Backup time
    aws_s3 as s3,                   # to create S3 bucket
    aws_s3_deployment as s3deploy,  # for uploading scripts S3 bucket
    aws_autoscaling as autoscaling,
    aws_elasticloadbalancingv2 as elbv2,
    aws_certificatemanager as cm,
    aws_iam as iam,
    aws_rds as rds,
    RemovalPolicy,
    )
from zipfile import ZipFile         # for creating .zip file before uploading to S3 bucket



 #█████  ██████  ███    ██ ███████ ██  ██████  
#█      ██    ██ ████   ██ ██      ██ ██       
#█      ██    ██ ██ ██  ██ █████   ██ ██   ███ 
#█      ██    ██ ██  ██ ██ ██      ██ ██    ██ 
 #█████  ██████  ██   ████ ██      ██  ██████


# What is the home/office IP address of the Administrator that will be accessing the Admin Server?
ip_address_administrator="143.178.129.147/32"

# What is the certificate ARN for the Application Load Balancer?
certificate_arn_alb="arn:aws:acm:eu-central-1:908959576754:certificate/3b2179b4-0384-4855-be19-1fb8b84213f3"



class CdkVpcTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        #█    ██ ██████   ██████     ██     ██ ███████ ██████  
        #█    ██ ██   ██ ██          ██     ██ ██      ██   ██ 
        #█    ██ ██████  ██          ██  █  ██ █████   ██████  
         #█  ██  ██      ██          ██ ███ ██ ██      ██   ██ 
          #███   ██       ██████      ███ ███  ███████ ██████


        # Create VPC & Subnet
        self.vpc_webserv = ec2.Vpc(self, 'vpc-1-web',
            ip_addresses=ec2.IpAddresses.cidr('10.0.1.0/24'),
            vpc_name='vpc-1-web',
            nat_gateways=1,                             # 
            max_azs=3,                                  # use all 3 AZ's
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,  # create public subnet
                    name='Public',                      # subnet group name
                    cidr_mask=28                        # 16 IP addresses
                    ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,    # create public subnet
                    name='Private',                                 # subnet group name
                    cidr_mask=28                                    # 16 IP addresses
                    )
                ]
            )

        # Add S3 endpoint
        self.vpc_webserv.add_gateway_endpoint("S3-endpoint",
            service=ec2.GatewayVpcEndpointAwsService.S3,
            subnets=[ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)]
            )



        #█    ██ ██████   ██████      █████  ██████  ███    ███ ██ ███    ██ 
        #█    ██ ██   ██ ██          ██   ██ ██   ██ ████  ████ ██ ████   ██ 
        #█    ██ ██████  ██          ███████ ██   ██ ██ ████ ██ ██ ██ ██  ██ 
         #█  ██  ██      ██          ██   ██ ██   ██ ██  ██  ██ ██ ██  ██ ██ 
          #███   ██       ██████     ██   ██ ██████  ██      ██ ██ ██   ████


        # Create VPC & Subnet
        self.vpc_adminserv = ec2.Vpc(self, 'vpc-admin',
            ip_addresses=ec2.IpAddresses.cidr('10.0.2.0/24'),
            vpc_name='vpc-admin',
            nat_gateways=0,                             # no gateway needed
            availability_zones=["eu-central-1b"],       # define AZ
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,  # create public subnet
                    name='Public',                 # for webserver
                    cidr_mask=28                        # 16 IP addresses
                    )
                ]
            )
        


        #█████  ███████ ███████ ██████  ██ ███    ██  ██████  
        #█   ██ ██      ██      ██   ██ ██ ████   ██ ██       
        #█████  █████   █████   ██████  ██ ██ ██  ██ ██   ███ 
        #█      ██      ██      ██   ██ ██ ██  ██ ██ ██    ██ 
        #█      ███████ ███████ ██   ██ ██ ██   ████  ██████
        

        # Create VPC Peering service
        self.vpc_peering = ec2.CfnVPCPeeringConnection(self,"vpc-peering",
            peer_vpc_id=self.vpc_webserv.vpc_id,    # VPC webserver
            vpc_id=self.vpc_adminserv.vpc_id        # VPC adminserver
            )
        

        # Connect VPC Peering service to Route Table from Webserver
        # Get Subnet Webserver
        self.subnet_webserver = self.vpc_webserv.private_subnets[0]

        # Get Route Table Webserver
        self.rt_sub_webserv = self.subnet_webserver.route_table

        # Add route from Subnet Route Table to VPC Peering
        self.rt_webserv_w_vpcpeering = ec2.CfnRoute(self, "rt-webserv-w-vpcpeering",
            route_table_id=self.rt_sub_webserv.route_table_id,
            destination_cidr_block="10.0.2.0/24",
            vpc_peering_connection_id=self.vpc_peering.ref
            )
        

        # Connect VPC Peering service to Route Table from Adminserver
        # Get Subnet Adminserver
        self.subnet_adminserver = self.vpc_adminserv.public_subnets[0]

        # Get Route Table Adminserver
        self.rt_sub_adminserv = self.subnet_adminserver.route_table

        # Add route from Subnet Route Table to VPC Peering
        self.rt_adminserv_w_vpcpeering = ec2.CfnRoute(self, "rt-adminserv-w-vpcpeering",
            route_table_id=self.rt_sub_adminserv.route_table_id,
            destination_cidr_block="10.0.1.0/24",
            vpc_peering_connection_id=self.vpc_peering.ref
            )



        #██    ██  █████   ██████ ██          ██████  ██    ██     ██     ██ ███████ ██████  
        #███   ██ ██   ██ ██      ██          ██   ██ ██    ██     ██     ██ ██      ██   ██ 
        #█ ██  ██ ███████ ██      ██          ██████  ██    ██     ██  █  ██ █████   ██████  
        #█  ██ ██ ██   ██ ██      ██          ██      ██    ██     ██ ███ ██ ██      ██   ██ 
        #█   ████ ██   ██  ██████ ███████     ██       ██████       ███ ███  ███████ ██████                                                            
        

        # - - - - - - - - NACL WEBSERVER PUBLIC SUBNET & RULES - - - - - - - - - -
        
        # Create NACL
        self.nacl_webserver_pu = ec2.NetworkAcl(self, 'nacl-webserver-pulic', 
            network_acl_name='nacl-webserver-public',
            vpc=self.vpc_webserv,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
            )
        
        # - - - - - - - - INBOUND TRAFFIC - - - - - - - - - -
            #    ||
            #    ||
            #   \\//
            #    \/

        # Allow all inbound HTTP traffic on the load balancer listener port
        self.nacl_webserver_pu.add_entry("Inbound-HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),        # HTTP port
            direction=ec2.TrafficDirection.INGRESS
            )

        # Allow all inbound HTTPS traffic on the load balancer listener port
        self.nacl_webserver_pu.add_entry("Inbound-HTTPS",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),       # HTTPS port
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # Allow inbound traffic from the VPC CIDR on the ephemeral ports
        self.nacl_webserver_pu.add_entry("Inbound-Ephemeral",
            cidr=ec2.AclCidr.ipv4("10.0.1.0/24"),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),    # ephemeral ports
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # - - - - - - - - FOR TESTING PURPOSES ONLY - - - - - - - - - -
        # - - - - comment out when deploying in production - - - - - - - - - -
        
        # Allow NACL Inbound All traffic from anywhere
        #   for troubleshooting purposes
        # self.nacl_webserver_pu.add_entry("Inbound-ALL",
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     rule_number=50,
        #     traffic=ec2.AclTraffic.all_traffic(),
        #     direction=ec2.TrafficDirection.INGRESS
        #     )
        

        # - - - - - - - - OUTBOUND TRAFFIC - - - - - - - - - -
            #    /\
            #   //\\
            #    ||
            #    ||
            
        # Allow all outbound traffic on the instance-listener/health-check port
        self.nacl_webserver_pu.add_entry("Outbound-HTTPS/health-check",
            cidr=ec2.AclCidr.ipv4("10.0.1.0/24"),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),       # HTTPS/health-check port
            direction=ec2.TrafficDirection.EGRESS
            )
        
        # Allow all outbound traffic on the ephemeral ports
        self.nacl_webserver_pu.add_entry("Outbound-Ephemeral",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),    # ephemeral ports
            direction=ec2.TrafficDirection.EGRESS
            )
        
        # - - - - - - - - FOR TESTING PURPOSES ONLY - - - - - - - - - -
        # - - - - comment out when deploying in production - - - - - - - - - -
        
        # Allow NACL Outbound all traffic
        # self.nacl_webserver_pu.add_entry("Outbound-All",
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     rule_number=50,
        #     traffic=ec2.AclTraffic.all_traffic(),
        #     direction=ec2.TrafficDirection.EGRESS
        #     )
        
        

        #██    ██  █████   ██████ ██          ██████  ██████      ██     ██ ███████ ██████  
        #███   ██ ██   ██ ██      ██          ██   ██ ██   ██     ██     ██ ██      ██   ██ 
        #█ ██  ██ ███████ ██      ██          ██████  ██████      ██  █  ██ █████   ██████  
        #█  ██ ██ ██   ██ ██      ██          ██      ██   ██     ██ ███ ██ ██      ██   ██ 
        #█   ████ ██   ██  ██████ ███████     ██      ██   ██      ███ ███  ███████ ██████


        # - - - - - - - - NACL WEBSERVER PRIVATE SUBNET & RULES - - - - - - - - - -

        # Create NACL
        self.nacl_webserver_pr = ec2.NetworkAcl(self, 'nacl-webserver-private', 
            network_acl_name='nacl-webserver-private',
            vpc=self.vpc_webserv,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)
            )


        # - - - - - - - - INBOUND TRAFFIC - - - - - - - - - -
            #    ||
            #    ||
            #   \\//
            #    \/

        # Allow inbound SSH traffic from admin server
        self.nacl_webserver_pr.add_entry("Inbound-SSH",
            cidr=ec2.AclCidr.ipv4("10.0.2.4/32"),       # Static IP of Admin Server
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(22),        # SSH port
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # Allow inbound HTTP traffic from VPC 1 & 2
        self.nacl_webserver_pr.add_entry("Inbound-HTTP",
            cidr=ec2.AclCidr.ipv4("10.0.0.0/16"),
            rule_number=105,
            traffic=ec2.AclTraffic.tcp_port(80),        # HTTP port
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # Allow inbound HTTPS traffic from VPC 1 & 2
        self.nacl_webserver_pr.add_entry("Inbound-HTTPS",
            cidr=ec2.AclCidr.ipv4("10.0.0.0/16"),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),       # HTTPS port
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # Allow inbound traffic from the VPC CIDR on the MySQL port
        self.nacl_webserver_pr.add_entry("Inbound-MySQL",
            cidr=ec2.AclCidr.ipv4("10.0.1.0/24"),
            rule_number=115,
            traffic=ec2.AclTraffic.tcp_port(3306),       # MySQL port
            direction=ec2.TrafficDirection.INGRESS
            )

        # Allow inbound traffic from the VPC CIDR on the ephemeral ports
        #   Needed for webservers to install packages.
        self.nacl_webserver_pr.add_entry("Inbound-Ephemeral",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),    # ephemeral ports
            direction=ec2.TrafficDirection.INGRESS
            )

        # - - - - - - - - FOR TESTING PURPOSES ONLY - - - - - - - - - -
        # - - - - comment out when deploying in production - - - - - - - - - -
        
        # Allow NACL Inbound All traffic from anywhere
        #   for troubleshooting purposes
        # self.nacl_webserver_pr.add_entry("Inbound-ALL",
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     rule_number=50,
        #     traffic=ec2.AclTraffic.all_traffic(),
        #     direction=ec2.TrafficDirection.INGRESS
        #     )


        # - - - - - - - - OUTBOUND TRAFFIC - - - - - - - - - -
            #    /\
            #   //\\
            #    ||
            #    ||
        
        # Allow all outbound traffic on HTTPS port
        #   Needed for downloading mysql packages.
        self.nacl_webserver_pr.add_entry("Outbound-HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),   # http port
            direction=ec2.TrafficDirection.EGRESS
            )
        
        # Allow all outbound traffic on HTTPS port
        #   Needed for webservers to install packages.
        self.nacl_webserver_pr.add_entry("Outbound-HTTPS",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),   # https port
            direction=ec2.TrafficDirection.EGRESS
            )
        
        # Allow all outbound traffic on the ephemeral ports
        self.nacl_webserver_pr.add_entry("Outbound-Ephemeral",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),    # ephemeral ports
            direction=ec2.TrafficDirection.EGRESS
            )
        
        # - - - - - - - - FOR TESTING PURPOSES ONLY - - - - - - - - - -
        # - - - - comment out when deploying in production - - - - - - - - - -

        # Allow NACL Outbound all traffic
        # self.nacl_webserver_pr.add_entry("Outbound-All",
            # cidr=ec2.AclCidr.any_ipv4(),
            # rule_number=50,
            # traffic=ec2.AclTraffic.all_traffic(),
            # direction=ec2.TrafficDirection.EGRESS
            # )



        #██    ██  █████   ██████ ██          ██████  ██    ██      █████  ██████  ███    ███ 
        #███   ██ ██   ██ ██      ██          ██   ██ ██    ██     ██   ██ ██   ██ ████  ████ 
        #█ ██  ██ ███████ ██      ██          ██████  ██    ██     ███████ ██   ██ ██ ████ ██ 
        #█  ██ ██ ██   ██ ██      ██          ██      ██    ██     ██   ██ ██   ██ ██  ██  ██ 
        #█   ████ ██   ██  ██████ ███████     ██       ██████      ██   ██ ██████  ██      ██
        

        # Create NACL
        self.nacl_adminserver = ec2.NetworkAcl(self, 'nacl-adminserver-public', 
            network_acl_name='nacl-adminserver-public',
            vpc=self.vpc_adminserv,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
            )
        
        # - - - - - - - - INBOUND TRAFFIC - - - - - - - - - -
            #    ||
            #    ||
            #   \\//
            #    \/
            
        # Allow NACL Inbound Ephemeral traffic for Windows Server 2022.
        self.nacl_adminserver.add_entry("Inbound-Ephemeral",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=90,
            traffic=ec2.AclTraffic.tcp_port_range(49152, 65535),    # Windows ephemeral ports
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # Allow NACL Inbound RDP traffic from only my IP
        self.nacl_adminserver.add_entry("Inbound-RDP",
            cidr=ec2.AclCidr.ipv4("143.178.129.147/32"),    # change this to your home/office public IP
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(3389),          # RDP port
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # - - - - - - - - FOR TESTING PURPOSES ONLY - - - - - - - - - -
        # - - - - comment out when deploying in production - - - - - - - - - -
        
        # Allow NACL Inbound All traffic from anywhere
        #   for troubleshooting purposes
        # self.nacl_adminserver.add_entry("Inbound-ALL",
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     rule_number=50,
        #     traffic=ec2.AclTraffic.all_traffic(),
        #     direction=ec2.TrafficDirection.INGRESS
        #     )

        
        # - - - - - - - - OUTBOUND TRAFFIC - - - - - - - - - -
            #    /\
            #   //\\
            #    ||
            #    ||

        # Allow outbound SSH traffic to Admin Webserver
        self.nacl_adminserver.add_entry("Outbound-SSH",
            cidr=ec2.AclCidr.ipv4("10.0.1.52/32"),
            rule_number=90,
            traffic=ec2.AclTraffic.tcp_port(22),    # ssh port
            direction=ec2.TrafficDirection.EGRESS
            )
        
        # Allow all outbound traffic on HTTP port
        self.nacl_adminserver.add_entry("Outbound-HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),   # http port
            direction=ec2.TrafficDirection.EGRESS
            )
        
        # Allow all outbound traffic on HTTPS port
        self.nacl_adminserver.add_entry("Outbound-HTTPS",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),   # https port
            direction=ec2.TrafficDirection.EGRESS
            )
        
        # Allow all outbound traffic on the ephemeral ports
        self.nacl_adminserver.add_entry("Outbound-Ephemeral",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),    # ephemeral ports
            direction=ec2.TrafficDirection.EGRESS
            )

        # - - - - - - - - FOR TESTING PURPOSES ONLY - - - - - - - - - -
        # - - - - comment out when deploying in production - - - - - - - - - -
        
        # Allow NACL Outbound All traffic
        # self.nacl_adminserver.add_entry("Outbound-All",
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     rule_number=50,
        #     traffic=ec2.AclTraffic.all_traffic(),
        #     direction=ec2.TrafficDirection.EGRESS
        #     )

        

        #█     ██ ███████ ██████      ███████ ███████ ██████  ██    ██ 
        #█     ██ ██      ██   ██     ██      ██      ██   ██ ██    ██ 
        #█  █  ██ █████   ██████      ███████ █████   ██████  ██    ██ 
        #█ ███ ██ ██      ██   ██          ██ ██      ██   ██  ██  ██  
         #██ ███  ███████ ██████      ███████ ███████ ██   ██   ████


        # - - - - - - - - SECURITY GROUP & RULES - - - - - - - - - -
        
        # Create Security Group for Private Web server
        # self.sg_admin_webserver = ec2.SecurityGroup(self, "sg-admin-webserver",
        #     vpc=self.vpc_webserv,
        #     description="SG Admin Webserver"
        #     )

        # - - - - - - - - INBOUND TRAFFIC - - - - - - - - - -
            #    ||
            #    ||
            #   \\//
            #    \/
        
        # Allow SG inbound HTTP traffic from admin server
        # self.sg_admin_webserver.add_ingress_rule(
        #     peer=ec2.Peer.ipv4("10.0.2.4/32"),      # Static IP of Admin Server
        #     connection=ec2.Port.tcp(80),            # HTTP port
        #     description="Allow HTTP traffic from admin server",
        #     )
        
        # # Allow SG inbound HTTPS traffic from admin server
        # self.sg_admin_webserver.add_ingress_rule(
        #     peer=ec2.Peer.ipv4("10.0.2.4/32"),      # Static IP of Admin Server
        #     connection=ec2.Port.tcp(443),           # HTTPS port
        #     description="Allow HTTPS traffic from admin server",
        #     )
        
        # # Allow SG inbound SSH traffic from admin server
        # self.sg_admin_webserver.add_ingress_rule(
        #     peer=ec2.Peer.ipv4("10.0.2.4/32"),    # Static IP of Admin Server
        #     connection=ec2.Port.tcp(22),          # SSH port
        #     description="Allow SSH traffic from admin server",
        #     )
        
        # - - - - - - - - FOR TESTING PURPOSES ONLY - - - - - - - - - -
        # - - - - comment out when deploying in production - - - - - - - - - -
        
        # Allow SG inbound HTTP traffic from anywhere                   
        # self.sg_admin_webserver.add_ingress_rule(                           
        #     peer=ec2.Peer.any_ipv4(),                                 
        #     connection=ec2.Port.tcp(80),                              
        #     description="Allow HTTP traffic from anywhere",          
        #     )                                                        
                                                                        
        # Allow SG inbound HTTPS traffic from anywhere
        # self.sg_admin_webserver.add_ingress_rule(
        #     peer=ec2.Peer.any_ipv4(),      
        #     connection=ec2.Port.tcp(443),            
        #     description="Allow HTTPS traffic from anywhere",
        #     )
        
        # Allow SG inbound SSH traffic from anywhere
        # self.sg_admin_webserver.add_ingress_rule(
        #     peer=ec2.Peer.any_ipv4(),
        #     connection=ec2.Port.tcp(22),               
        #     description="Allow SSH traffic from anywhere",
        #     )

        # Allow SG inbound ICMP (ping) traffic from anywhere
        # sself.sg_admin_webserver.add_ingress_rule(
        #     peer=ec2.Peer.ipv4("0.0.0.0/0"),
        #     connection=ec2.Port.all_icmp(),
        #     description="Allow ICMP traffic from anywhere",
        #     )


        # - - - - - - - - S3 BUCKET & WEB CONTENT - - - - - - - - - - 
        
        # Create S3 Bucket for Website
        self.website_bucket = s3.Bucket(self, "website-bucket",
            bucket_name="cdkbucket-forwebserver-121212",
            )
    
        # Upload a the lab zipfiles to the S3 bucket
        self.deploy_website = s3deploy.BucketDeployment(self, "deploy-website",
            sources=[s3deploy.Source.asset(path="./cdk_vpc_test/lab-app.zip")],
            destination_bucket=self.website_bucket,
        )
        
        
        # - - - - - - - - CREATE WEBSERVER INSTANCE FOR ADMIN - - - - - - - - - -
        
        # Create Role for webserver instance
        self.role_webserv = iam.Role(self, "role-webserv",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )

        # Allow Role to access S3 bucket.
        self.role_webserv.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3ReadOnlyAccess"))

        # Import User Data for Webserver
        with open("./cdk_vpc_test/user_data_webs.sh") as f:
            self.user_data_webs = f.read()  # read User Data script and save to variable
        
        # Create Keypair Web Server -> Private Key in Parameter Store
        # self.keypair_webserver = ec2.KeyPair(self, "keypair-admin-webserver",
        #     key_pair_name="kp-admin-webserver",
        #     )
        
        # Create Webserver instance
        # self.instance_webserver = ec2.Instance(self, "admin-webserver",
        #     role=self.role_webserv,
        #     instance_name="admin-webserver",
        #     vpc=self.vpc_webserv,                               # VPC Webserver
        #     vpc_subnets=ec2.SubnetSelection(
        #         subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),   # Private subnet in VPC Webserver
        #     private_ip_address="10.0.1.52",                     # Give it a static IP address
        #     key_pair=self.keypair_webserver,                    # refer to keypair. Code above.
        #     security_group=self.sg_admin_webserver,             # refer to the SG for Webserver
        #     instance_type=ec2.InstanceType.of(
        #         ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),  # choose instance type
        #     machine_image=ec2.AmazonLinuxImage(
        #         generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023),    # choose AMI
        #     block_devices=[ec2.BlockDevice(
        #         device_name="/dev/xvda",                        # Root EBS for Linux is always "xvda"
        #         volume=ec2.BlockDeviceVolume.ebs(
        #             volume_size=8,                              # 8 GB
        #             encrypted=True,                             # activate encryption on root EBS
        #             )
        #         )],
        #     user_data=ec2.UserData.custom(self.user_data_webs), # refer to imported User Data. See code above
        #     )



         #████  ██████  ███    ███     ███████ ███████ ██████  ██    ██ 
        #█   ██ ██   ██ ████  ████     ██      ██      ██   ██ ██    ██ 
        #██████ ██   ██ ██ ████ ██     ███████ █████   ██████  ██    ██ 
        #█   ██ ██   ██ ██  ██  ██          ██ ██      ██   ██  ██  ██  
        #█   ██ ██████  ██      ██     ███████ ███████ ██   ██   ████


        # - - - - - - - - SECURITY GROUP & RULES - - - - - - - - - -
        
        # Create Security Group for the Admin server
        # self.sg_adminserver = ec2.SecurityGroup(self, "sg-adminserver",
        #     vpc=self.vpc_adminserv,         # VPC for the Admin server
        #     description="SG Adminserver"
        #     )
        

        # # - - - - - - - - INBOUND TRAFFIC - - - - - - - - - -
        #     #    ||
        #     #    ||
        #     #   \\//
        #     #    \/
        
        # # Allow SG inbound RDP traffic from only my IP
        # self.sg_adminserver.add_ingress_rule(
        #     peer=ec2.Peer.ipv4(ip_address_administrator),   # refer to admin home/office IP address
        #     connection=ec2.Port.tcp(3389),                  # RDP port
        #     description="Allow RDP from only my IP",
        #     )
        
        # - - - - - - - - FOR TESTING PURPOSES ONLY - - - - - - - - - -
        # - - - - comment out when deploying in production - - - - - - - - - -
        
        # Allow SG inbound ICMP (ping) traffic from anywhere
        # self.sg_adminserver.add_ingress_rule(
        #     peer=ec2.Peer.ipv4("0.0.0.0/0"),
        #     connection=ec2.Port.all_icmp(),
        #     description="Allow ICMP traffic from anywhere",
        #     )


        # - - - - - - - - CREATE ADMIN SERVER - - - - - - - - - -

        # Create Keypair Admin Server -> Private Key in Parameter Store
        # self.keypair_adminserver = ec2.KeyPair(self, "keypair-adminserver",
        #     key_pair_name="kp-adminserver",     
        #     )

        # Create Adminserver instance
        # self.instance_adminserver = ec2.Instance(self,"adminserver",
        #     instance_name="adminserver",
        #     vpc=self.vpc_adminserv,                             # VPC Admin server
        #     vpc_subnets=ec2.SubnetSelection(                    
        #         subnet_type=ec2.SubnetType.PUBLIC),             # Public subnet in VPC Admin server
        #     private_ip_address="10.0.2.4",                      # Give it a static IP address
        #     key_pair=self.keypair_adminserver,                  # refer to keypair. Code above.
        #     security_group=self.sg_adminserver,                 # refer to the SG for Admin server
        #     instance_type=ec2.InstanceType.of(
        #         ec2.InstanceClass.T3, ec2.InstanceSize.SMALL),  # choose instance type
        #     machine_image=ec2.WindowsImage(
        #         ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE),  # choose AMI
        #     block_devices=[ec2.BlockDevice(
        #         device_name="/dev/sda1",                        # Root EBS for Windows is always "sda1"
        #         volume=ec2.BlockDeviceVolume.ebs(
        #             volume_size=30,                             # 30 GB
        #             encrypted=True,                             # activate encryption on root EBS
        #             )
        #         ), ec2.BlockDevice(
        #         device_name="/dev/sdf",                         # define volume name
        #         volume=ec2.BlockDeviceVolume.ebs(
        #             volume_size=256,                            # 256 GB
        #             encrypted=True,                             # activate encryption on attached EBS
        #             )
        #         )]
        #     )



        #██████ ██      ██████                 █████  ███████ 
        #█      ██      ██   ██               ██   ██ ██      
        #████   ██      ██████      █████     ███████ ███████ 
        #█      ██      ██   ██               ██   ██      ██ 
        #██████ ███████ ██████                ██   ██ ███████


        # - - - - - - - - SECURITY GROUP - - - - - - - - - -

        # Create Security Group for Auto Scaling Web servers
        self.sg_as_webserver = ec2.SecurityGroup(self, "sg-as-webserver",
            vpc=self.vpc_webserv,
            description="SG AS Webservers"
            )
        

        # - - - - - - - - AUTO SCALING - - - - - - - - - -

        # Create Launch Template
        self.launch_template_ws = ec2.LaunchTemplate(self, "ws-launch-template",
            launch_template_name="ws-launch-template",
            role=self.role_webserv,
            security_group=self.sg_as_webserver,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023),
            block_devices=[ec2.BlockDevice(
                device_name="/dev/xvda",                       
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=8,                              
                    encrypted=True,                            
                    )
                )],
            user_data=ec2.UserData.custom(self.user_data_webs),
            )

        # Create Autoscaling group
        self.auto_scaling_group = autoscaling.AutoScalingGroup(self, "asg",
            vpc=self.vpc_webserv,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
            launch_template=self.launch_template_ws,
            desired_capacity=1,
            min_capacity=1,
            max_capacity=3,
            health_check=autoscaling.HealthCheck.elb(
                grace=Duration.minutes(5)
                )
            )

        # Set Scale Policy
        self.scale_policy = self.auto_scaling_group.scale_on_cpu_utilization("scale-policy",
            target_utilization_percent=75,
            )
        

        # - - - - - - - - APPLICATION LOAD BALANCER - - - - - - - - - -

        # Create Application Load balancer
        self.load_balancer_ws = elbv2.ApplicationLoadBalancer(self, "load-balancer-ws",
            load_balancer_name="load-balancer-ws",
            vpc=self.vpc_webserv,
            internet_facing=True,
            )

        # Create Target Group for ALB
        self.target_group = elbv2.ApplicationTargetGroup(self, "target-group",
            vpc=self.vpc_webserv,
            port=443,
            targets=[self.auto_scaling_group],
            )

        # Import self signed certificate from console
        self.certificate_ss_imp = cm.Certificate.from_certificate_arn(self, "certificate-ss-imp",
            certificate_arn=certificate_arn_alb
            )
        
        # Add listener to the ALB for port 443
        self.https_listener = self.load_balancer_ws.add_listener("https_listener",
            port=443,
            ssl_policy=elbv2.SslPolicy.RECOMMENDED_TLS,
            certificates=[self.certificate_ss_imp],
            default_target_groups=[self.target_group]
            )

        # Add listener to the ALB for port 80 and redirect traffic to port 443
        self.http_listener = self.load_balancer_ws.add_listener("http_listener",
            port=80,
            default_action=elbv2.ListenerAction.redirect(
                port="443",
                protocol="HTTPS",
                )
            )



        #█████   █████  ████████  █████  ██████   █████  ███████ ███████ 
        #█   ██ ██   ██    ██    ██   ██ ██   ██ ██   ██ ██      ██      
        #█   ██ ███████    ██    ███████ ██████  ███████ ███████ █████   
        #█   ██ ██   ██    ██    ██   ██ ██   ██ ██   ██      ██ ██      
        #█████  ██   ██    ██    ██   ██ ██████  ██   ██ ███████ ███████


        # - - - - - - - - SECURITY GROUP - - - - - - - - - -

        # Create Security Group for database
        # self.sg_database = ec2.SecurityGroup(self, "sg-database",
        #     vpc=self.vpc_webserv,
        #     description="SG Database"
        #     )


        # # - - - - - - - - INBOUND TRAFFIC - - - - - - - - - -
        #     #    ||
        #     #    ||
        #     #   \\//
        #     #    \/
        
        # # Allow inbound traffic from the VPC CIDR on the MySQL port
        # self.sg_database.add_ingress_rule(
        #     peer=ec2.Peer.ipv4("10.0.1.0/24"),          # VPC CIDR
        #     connection=ec2.Port.tcp(3306),              # MySQL port
        #     description="Allow MySQL from VPC-1 Web",
        #     )
        

        # - - - - - - - - TEST WEBSERVER FOR DATABASE - - - - - - - - 
        # - - - - comment out when deploying in production - - - - - - - - - -
        # self.sg_test_webserver = ec2.SecurityGroup(self, "sg-test-webserver",
        #     vpc=self.vpc_webserv,
        #     description="SG Test Webserver"
        #     )
        # self.sg_test_webserver.add_ingress_rule(
        #     peer=ec2.Peer.any_ipv4(), 
        #     connection=ec2.Port.tcp(80),  
        #     description="Allow HTTP traffic from anywhere",
        #     )
        # self.sg_test_webserver.add_ingress_rule(
        #     peer=ec2.Peer.any_ipv4(), 
        #     connection=ec2.Port.tcp(443),  
        #     description="Allow HTTPS traffic from anywhere",
        #     )
        # self.sg_test_webserver.add_ingress_rule(
        #     peer=ec2.Peer.any_ipv4(), 
        #     connection=ec2.Port.tcp(22),  
        #     description="Allow SSH traffic from anywhere",
        #     )
        # self.keypair_testwebserver = ec2.KeyPair(self, "keypair-test-webserver",
        #     key_pair_name="kp-test-webserver",
        #     )
        # self.instance_webserver = ec2.Instance(self, "test-webserver",
        #     role=self.role_webserv,
        #     instance_name="test-webserver",
        #     vpc=self.vpc_webserv,                               
        #     vpc_subnets=ec2.SubnetSelection(
        #         subnet_type=ec2.SubnetType.PUBLIC),  
        #     key_pair=self.keypair_testwebserver,                    
        #     security_group=self.sg_test_webserver,             
        #     instance_type=ec2.InstanceType.of(
        #         ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),  
        #     machine_image=ec2.AmazonLinuxImage(
        #         generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023),    
        #     block_devices=[ec2.BlockDevice(
        #         device_name="/dev/xvda",                        
        #         volume=ec2.BlockDeviceVolume.ebs(
        #             volume_size=8,                              
        #             encrypted=True,                             
        #             )
        #         )],
        #     user_data=ec2.UserData.custom(self.user_data_webs), 
        #     )
        

        # - - - - - - - - DATABASE - - - - - - - - - -

        # Create RDS database
        # self.database = rds.DatabaseInstance(self, "database-webserver",
        #     vpc=self.vpc_webserv,
        #     vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
        #     security_groups=[self.sg_database],
        #     multi_az=True,
        #     engine=rds.DatabaseInstanceEngine.MYSQL,
        #     allocated_storage=20,
        #     instance_type=ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MICRO),
        #     iops=1000,
        #     storage_encrypted=True,
        #     backup_retention=Duration.days(7),
        #     removal_policy=RemovalPolicy.DESTROY,
        #     deletion_protection=False,
        #     )



        #█████   █████   ██████ ██   ██ ██    ██ ██████  
        #█   ██ ██   ██ ██      ██  ██  ██    ██ ██   ██ 
        #█████  ███████ ██      █████   ██    ██ ██████  
        #█   ██ ██   ██ ██      ██  ██  ██    ██ ██      
        #█████  ██   ██  ██████ ██   ██  ██████  ██


        # - - - - - - - - BACKUP PLAN - - - - - - - - - -
        
        # Create Backup plan
        # self.backup_plan = backup.BackupPlan(self, "backup-plan",
        #     backup_plan_name="7-day-Backup-plan",
        #     backup_plan_rules=[backup.BackupPlanRule(
        #         rule_name="Daily-Retention-7days",
        #         start_window=Duration.hours(1),             # start within 1 hour of scheduled start
        #         completion_window=Duration.hours(2),        # complete backup within 2 hours of backup start
        #         delete_after=Duration.days(7),              # retain backups for 7 days
        #         schedule_expression=events.Schedule.cron(
        #             hour="1",       # Daily backup at 01:00 UTC -->
        #             minute="0", )   # --> 02:00 Dutch winter time / 03:00 Dutch summer time
        #         )]
        #     )
        

        # # - - - - - - - - RESOURCES TO BACKUP - - - - - - - - - -

        # # Select Webserver as a resource to backup
        # self.backup_plan.add_selection("add-webserver", 
        #     backup_selection_name="backup-webserver",
        #     resources=[
        #         backup.BackupResource.from_ec2_instance(self.instance_webserver)
        #         ]
        #     )
        
        # # Select Adminserver as a resource to backup
        # self.backup_plan.add_selection("add-adminserver", 
        #     backup_selection_name="backup-adminserver",
        #     resources=[
        #         backup.BackupResource.from_ec2_instance(self.instance_adminserver)
        #         ]
        #     )
        
        
        
        #█████  ██    ██  ██████ ██   ██ ███████ ████████ 
        #█   ██ ██    ██ ██      ██  ██  ██         ██    
        #█████  ██    ██ ██      █████   █████      ██    
        #█   ██ ██    ██ ██      ██  ██  ██         ██    
        #█████   ██████   ██████ ██   ██ ███████    ██ 


        # Below is the code to create an S3 bucket and automatically
        # upload the important scripts to this bucket.

        # If for some reason this script is being executed after an
        # initial execute, there is probably no need to upload the scripts
        # againt to S3. In that case, comment out the code below.
        # If there is indeed a reason to re-upload the scripts to S3,
        # be sure to update the directories in the code below to the
        # current situation.

        # Create S3 Bucket for Scripts
        # self.script_bucket = s3.Bucket(self, "script-bucket",
        #     )

        # # Create .zip file of the important scripts
        # self.zip_file = "scripts_for_s3.zip" # define filename, directory will be the same as "app.py"
        # with ZipFile(self.zip_file, "w") as zip_object:
        #     zip_object.write("./cdk_vpc_test/cdk_vpc_test_stack.py")    # this current script
        #     zip_object.write("./cdk_vpc_test/user_data_webs.sh")        # the user data script for webserver
        #     zip_object.write("app.py")                                  # the app.py script

        # # Upload the .zip file to S3 bucket
        # s3deploy.BucketDeployment(self, "upload-scripts",
        #     sources=[s3deploy.Source.asset(self.zip_file)], # define source .zip file
        #     destination_bucket=self.script_bucket           # refer to S3 script bucket
        #     )