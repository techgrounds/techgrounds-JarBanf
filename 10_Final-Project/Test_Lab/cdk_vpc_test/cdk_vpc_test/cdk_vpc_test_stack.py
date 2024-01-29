from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)


class CdkVpcTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        # # # # # # # # # # #
        #                   #
        #   VPC WEBSERVER   #
        #                   #
        # # # # # # # # # # #
        
        # Create VPC & Subnet
        self.vpc_webserv = ec2.Vpc(self, 'vpc-webserver',
            ip_addresses=ec2.IpAddresses.cidr('10.0.1.0/24'),
            vpc_name='vpc-webserver',
            nat_gateways=0,
            availability_zones=["eu-central-1a"],
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name='Webserver',
                    cidr_mask=28
                )
            ]
            )


        # # # # # # # # # # # #
        #                     #
        #   VPC ADMINSERVER   #
        #                     #
        # # # # # # # # # # # #

        # Create VPC & Subnet
        self.vpc_adminserv = ec2.Vpc(self, 'vpc-adminserver',
            ip_addresses=ec2.IpAddresses.cidr('10.0.2.0/24'),
            vpc_name='vpc-adminserver',
            nat_gateways=0,
            availability_zones=["eu-central-1b"],
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name='Adminserver',
                    cidr_mask=28
                )
            ]
            )
        

        # # # # # # # # # #
        #                 #
        #   VPC PEERING   #
        #                 #
        # # # # # # # # # #
        
        # Create VPC Peering service
        self.vpc_peering = ec2.CfnVPCPeeringConnection(self,"vpc-peering",
            peer_vpc_id=self.vpc_webserv.vpc_id,
            vpc_id=self.vpc_adminserv.vpc_id
            )

        # Connect VPC Peering service to Route Table from Webserver
        # Get Subnet Webserver
        self.subnet_webserver = self.vpc_webserv.public_subnets[0]
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


        # # # # # # # # # # #
        #                   #
        #   NACL WEBSERVER  #
        #                   #
        # # # # # # # # # # # 
        
        # Create NACL
        self.nacl_webserver = ec2.NetworkAcl(self, 'nacl-webserver', 
            network_acl_name='nacl-webserver',
            vpc=self.vpc_webserv,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
            )
        
        # Allow NACL Inbound traffic
        self.nacl_webserver.add_entry("InboundHTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # Allow NACL Outbound traffic
        self.nacl_webserver.add_entry("OutboundAll",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS
            )
        

        # # # # # # # # # # # #
        #                     #
        #   NACL ADMINSERVER  #
        #                     #
        # # # # # # # # # # # #
        
        # Create NACL
        # self.nacl_webserver = ec2.NetworkAcl(self, 'nacl-adminserver', 
        #     network_acl_name='nacl-adminserver',
        #     vpc=self.vpc_adminserv,
        #     subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        #     )
        
        # Allow NACL Inbound traffic
        
        
        # Allow NACL Outbound traffic
        


        # # # # # # # # #
        #               #
        #   WEBSERVER   #
        #               #
        # # # # # # # # #

        # Create Security Group
        self.sg_webserver = ec2.SecurityGroup(self, "sg-webserver",
            vpc=self.vpc_webserv,
            description="SG Webserver"
            )
        
        # Allow SG inbound HTTP traffic from anywhere
        self.sg_webserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80),
            description="Allow HTTP traffic",
        )

        # Import User Data for Webserver
        with open("./cdk_vpc_test/user_data_webs.sh") as f:
            self.user_data_webs = f.read()
        
        # Create Webserver instance
        self.instance_webserver = ec2.Instance(self, "instance-webserver",
            instance_name="instance-webserver",
            vpc=self.vpc_webserv,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            security_group=self.sg_webserver,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023),
            user_data=ec2.UserData.custom(self.user_data_webs),
            )
        

        # # # # # # # # # #
        #                 #
        #   ADMINSERVER   #
        #                 #
        # # # # # # # # # #

        # Create Security Group
        # self.sg_adminserver = ec2.SecurityGroup(self, "sg-adminserver",
        #     vpc=self.vpc_adminserv,
        #     description="SG Adminserver"
        #     )
        
        # Allow SG inbound RDP traffic from anywhere
        # self.sg_adminserver.add_ingress_rule(
        #     peer=ec2.Peer.ipv4("0.0.0.0/0"),
        #     connection=ec2.Port.tcp(3389),
        #     description="Allow RDP from anywhere",
        # )

        # Create Adminserver instance
        # self.instance_adminserver = ec2.Instance(self,"instance-adminserver",
        #     instance_name="instance-adminserver",
        #     vpc=self.vpc_adminserv,
        #     vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
        #     security_group=self.sg_adminserver,
        #     instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
        #     machine_image=ec2.WindowsImage(ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE)
        #     )