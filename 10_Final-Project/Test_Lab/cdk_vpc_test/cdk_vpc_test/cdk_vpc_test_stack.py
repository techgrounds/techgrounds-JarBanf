from constructs import Construct    # needed for CDK
from aws_cdk import (
    Stack,                          # needed for CDK
    aws_ec2 as ec2,                 # for creating the network
    CfnOutput,                      # for outputing values of the stack
    aws_backup as backup,           # for creating backup plan
    Duration,                       # for configuring backup rule
    aws_events as events,           # to schedule Backup time
    aws_s3 as s3,                   # to create S3 bucket
    RemovalPolicy,                  # to set removal policy of S3 bucket (for testing)
    aws_s3_deployment as s3deploy,   # for uploading scripts S3 bucket
    aws_autoscaling as autoscaling,
    aws_elasticloadbalancingv2 as elbv2,
    aws_certificatemanager as cm,
    )
from zipfile import ZipFile         # for creating .zip file before uploading to S3 bucket


class CdkVpcTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        #█    ██ ██████   ██████     ██     ██ ███████ ██████  
        #█    ██ ██   ██ ██          ██     ██ ██      ██   ██ 
        #█    ██ ██████  ██          ██  █  ██ █████   ██████  
         #█  ██  ██      ██          ██ ███ ██ ██      ██   ██ 
          #███   ██       ██████      ███ ███  ███████ ██████


        # Create VPC & Subnet
        self.vpc_webserv = ec2.Vpc(self, 'vpc-webserver',
            ip_addresses=ec2.IpAddresses.cidr('10.0.1.0/24'),
            vpc_name='vpc-webserver',
            nat_gateways=0,                             # 
            max_azs=3,                                  # use all 3 AZ's
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,  # create public subnet
                    name='Public',                      # subnet group name
                    cidr_mask=28                        # 16 IP addresses
                    ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,    # create public subnet
                    name='Private',                                  # subnet group name
                    cidr_mask=28                                    # 16 IP addresses
                    )
                ]
            )



        #█    ██ ██████   ██████      █████  ██████  ███    ███ ██ ███    ██ 
        #█    ██ ██   ██ ██          ██   ██ ██   ██ ████  ████ ██ ████   ██ 
        #█    ██ ██████  ██          ███████ ██   ██ ██ ████ ██ ██ ██ ██  ██ 
         #█  ██  ██      ██          ██   ██ ██   ██ ██  ██  ██ ██ ██  ██ ██ 
          #███   ██       ██████     ██   ██ ██████  ██      ██ ██ ██   ████


        # Create VPC & Subnet
        self.vpc_adminserv = ec2.Vpc(self, 'vpc-adminserver',
            ip_addresses=ec2.IpAddresses.cidr('10.0.2.0/24'),
            vpc_name='vpc-adminserver',
            nat_gateways=0,                             # no gateway needed
            availability_zones=["eu-central-1b"],       # define AZ
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,  # create public subnet
                    name='Adminserver',                 # for webserver
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



        #██    ██  █████   ██████ ██          ██     ██ ███████ ██████  
        #███   ██ ██   ██ ██      ██          ██     ██ ██      ██   ██ 
        #█ ██  ██ ███████ ██      ██          ██  █  ██ █████   ██████  
        #█  ██ ██ ██   ██ ██      ██          ██ ███ ██ ██      ██   ██ 
        #█   ████ ██   ██  ██████ ███████      ███ ███  ███████ ██████                                                             
        

        # Create NACL
        # self.nacl_webserver = ec2.NetworkAcl(self, 'nacl-webserver', 
        #     network_acl_name='nacl-webserver',
        #     vpc=self.vpc_webserv,
        #     subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        #     )
        

        #     #    ||
        #     #    ||
        #     #   \\//
        #     #    \/

        # # Allow NACL Inbound Ephemeral traffic for Linux kernels. 
        # #   Needed to install httpd.
        # self.nacl_webserver.add_entry("Inbound-Ephemeral",
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     rule_number=90,
        #     traffic=ec2.AclTraffic.tcp_port_range(32768, 60999),    # Linux ephemeral ports
        #     direction=ec2.TrafficDirection.INGRESS
        #     )
        
        # # Allow NACL Inbound HTTP traffic from anywhere
        # self.nacl_webserver.add_entry("Inbound-HTTP",
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     rule_number=100,
        #     traffic=ec2.AclTraffic.tcp_port(80),        # HTTP port
        #     direction=ec2.TrafficDirection.INGRESS
        #     )
        
        # # Allow NACL Inbound SSH traffic from admin server
        # self.nacl_webserver.add_entry("Inbound-SSH",
        #     cidr=ec2.AclCidr.ipv4("10.0.2.4/32"),       # Static IP of Admin Server
        #     rule_number=110,
        #     traffic=ec2.AclTraffic.tcp_port(22),        # SSH port
        #     direction=ec2.TrafficDirection.INGRESS
        #     )

        # Allow NACL Inbound All traffic from anywhere
        #   for troubleshooting purposes
        # self.nacl_webserver.add_entry("Inbound-ALL",
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     rule_number=120,
        #     traffic=ec2.AclTraffic.all_traffic(),
        #     direction=ec2.TrafficDirection.INGRESS
        #     )
        

            #    /\
            #   //\\
            #    ||
            #    ||
            
        # Allow NACL Outbound all traffic
        # self.nacl_webserver.add_entry("Outbound-All",
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     rule_number=100,
        #     traffic=ec2.AclTraffic.all_traffic(),
        #     direction=ec2.TrafficDirection.EGRESS
        #     )
        
        

        #██    ██  █████   ██████ ██           █████  ██████  ███    ███ 
        #███   ██ ██   ██ ██      ██          ██   ██ ██   ██ ████  ████ 
        #█ ██  ██ ███████ ██      ██          ███████ ██   ██ ██ ████ ██ 
        #█  ██ ██ ██   ██ ██      ██          ██   ██ ██   ██ ██  ██  ██
        #█   ████ ██   ██  ██████ ███████     ██   ██ ██████  ██      ██
        

        # Create NACL
        # self.nacl_adminserver = ec2.NetworkAcl(self, 'nacl-adminserver', 
        #     network_acl_name='nacl-adminserver',
        #     vpc=self.vpc_adminserv,
        #     subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        #     )
        

            #    ||
            #    ||
            #   \\//
            #    \/
            
        # Allow NACL Inbound Ephemeral traffic for Windows Server 2022.
        # self.nacl_adminserver.add_entry("Inbound-Ephemeral",
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     rule_number=90,
        #     traffic=ec2.AclTraffic.tcp_port_range(49152, 65535),    # Windows ephemeral ports
        #     direction=ec2.TrafficDirection.INGRESS
        #     )
        
        # Allow NACL Inbound RDP traffic from only my IP
        # self.nacl_adminserver.add_entry("Inbound-RDP",
        #     cidr=ec2.AclCidr.ipv4("143.178.129.147/32"),    # change this to your home/office public IP
        #     rule_number=100,
        #     traffic=ec2.AclTraffic.tcp_port(3389),          # RDP port
        #     direction=ec2.TrafficDirection.INGRESS
        #     )

        
            #    /\
            #   //\\
            #    ||
            #    ||

        # Allow NACL Outbound All traffic
        # self.nacl_adminserver.add_entry("Outbound-All",
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     rule_number=100,
        #     traffic=ec2.AclTraffic.all_traffic(),
        #     direction=ec2.TrafficDirection.EGRESS
        #     )

        

        #█     ██ ███████ ██████      ███████ ███████ ██████  ██    ██ 
        #█     ██ ██      ██   ██     ██      ██      ██   ██ ██    ██ 
        #█  █  ██ █████   ██████      ███████ █████   ██████  ██    ██ 
        #█ ███ ██ ██      ██   ██          ██ ██      ██   ██  ██  ██  
         #██ ███  ███████ ██████      ███████ ███████ ██   ██   ████


        # Create Security Group for Private Web server
        self.sg_webserver = ec2.SecurityGroup(self, "sg-private-webserver",
            vpc=self.vpc_webserv,
            description="SG Private Webserver"
            )


            #    ||
            #    ||
            #   \\//
            #    \/
        
        # Allow SG inbound HTTP traffic from admin server
        self.sg_webserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("10.0.2.4/32"),      # Static IP of Admin Server
            connection=ec2.Port.tcp(80),            # HTTP port
            description="Allow HTTP traffic from admin server",
            )
        
        # Allow SG inbound SSH traffic from admin server
        self.sg_webserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("10.0.2.4/32"),    # Static IP of Admin Server
            connection=ec2.Port.tcp(22),          # SSH port
            description="Allow SSH traffic from admin server",
            )
        

        # Allow SG inbound HTTPS traffic from admin server
        #   for troubleshooting purposes
        self.sg_webserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("10.0.2.4/32"),      # Static IP of Admin Server
            connection=ec2.Port.tcp(443),           # HTTPS port
            description="Allow HTTPS traffic from admin server",
            )
        
        # Allow SG inbound SSH traffic from anywhere
        #   for troubleshooting purposes
        # self.sg_webserver.add_ingress_rule(
        #     peer=ec2.Peer.any_ipv4(),               # any ip
        #     connection=ec2.Port.tcp(22),            # SSH port
        #     description="Allow SSH traffic from anywhere",
        #     )

        # Allow SG inbound ICMP (ping) traffic from anywhere
        #   for troubleshooting purposes
        # self.sg_webserver.add_ingress_rule(
        #     peer=ec2.Peer.ipv4("0.0.0.0/0"),
        #     connection=ec2.Port.all_icmp(),
        #     description="Allow ICMP traffic from anywhere",
        #     )


        # Import User Data for Webserver
        with open("./cdk_vpc_test/user_data_webs.sh") as f:
            self.user_data_webs = f.read()  # read User Data script and save to variable
        
        # Refer to existing Keypair Web Server
        # Make sure a keypair with the same name "kp-web-server" is created first via Console
        self.keypair_webserver = ec2.KeyPair.from_key_pair_name(self, "keypair-webserver",
            key_pair_name="kp-web-server",
            )
        
        # Create Webserver instance
        self.instance_webserver = ec2.Instance(self, "instance-webserver",
            instance_name="instance-webserver",
            vpc=self.vpc_webserv,                               # VPC Webserver
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC),             # Public subnet in VPC Webserver
            private_ip_address="10.0.1.4",                      # Give it a static IP address
            key_pair=self.keypair_webserver,                    # refer to keypair. Code above.
            security_group=self.sg_webserver,                   # refer to the SG for Webserver
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),  # choose instance type
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023),    # choose AMI
            block_devices=[ec2.BlockDevice(
                device_name="/dev/xvda",                        # Root EBS for Linux is always "xvda"
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=8,                              # 8 GB
                    encrypted=True,                             # activate encryption on root EBS
                    )
                )],
            user_data=ec2.UserData.custom(self.user_data_webs), # refer to imported User Data. See code above
            )
        
        # Output the Private Web server public IP
        CfnOutput(self, "Private Webserver Public IP",
            value=self.instance_webserver.instance_public_ip,
            export_name="private-webserver-public-ip"
            )
        
        # Output the Private Web server private IP
        CfnOutput(self, "Private Webserver Private IP",
            value=self.instance_webserver.instance_private_ip,
            export_name="private-webserver-private-ip"
            )
        
        # Output the Private Web server private DNS name, needed for SSH-ing from Admin server
        CfnOutput(self, "Private Webserver Private DNS name",
            value=self.instance_webserver.instance_private_dns_name,
            export_name="private-webserver-private-dns-name"
            )



         #████  ██████  ███    ███     ███████ ███████ ██████  ██    ██ 
        #█   ██ ██   ██ ████  ████     ██      ██      ██   ██ ██    ██ 
        #██████ ██   ██ ██ ████ ██     ███████ █████   ██████  ██    ██ 
        #█   ██ ██   ██ ██  ██  ██          ██ ██      ██   ██  ██  ██  
        #█   ██ ██████  ██      ██     ███████ ███████ ██   ██   ████


        # Create Security Group for the Admin server
        self.sg_adminserver = ec2.SecurityGroup(self, "sg-adminserver",
            vpc=self.vpc_adminserv,         # VPC for the Admin server
            description="SG Adminserver"
            )
        

            #    ||
            #    ||
            #   \\//
            #    \/
        
        # Allow SG inbound RDP traffic from only my IP
        self.sg_adminserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("143.178.129.147/32"),   # change this to your home/office public IP
            connection=ec2.Port.tcp(3389),              # RDP port
            description="Allow RDP from only my IP",
            )

        # Allow SG inbound ICMP (ping) traffic from anywhere
        #   for troubleshooting purposes
        # self.sg_adminserver.add_ingress_rule(
        #     peer=ec2.Peer.ipv4("0.0.0.0/0"),
        #     connection=ec2.Port.all_icmp(),
        #     description="Allow ICMP traffic from anywhere",
        #     )


        # Refer to existing Keypair Admin Server
        # Make sure a keypair with the same name "kp-admin-server" is created first via Console.
        self.keypair_adminserver = ec2.KeyPair.from_key_pair_name(self, "keypair-adminserver",
            key_pair_name="kp-admin-server",     
            )

        # Create Adminserver instance
        self.instance_adminserver = ec2.Instance(self,"instance-adminserver",
            instance_name="instance-adminserver",
            vpc=self.vpc_adminserv,                             # VPC Admin server
            vpc_subnets=ec2.SubnetSelection(                    
                subnet_type=ec2.SubnetType.PUBLIC),             # Public subnet in VPC Admin server
            private_ip_address="10.0.2.4",                      # Give it a static IP address
            key_pair=self.keypair_adminserver,                  # refer to keypair. Code above.
            security_group=self.sg_adminserver,                 # refer to the SG for Admin server
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),  # choose instance type
            machine_image=ec2.WindowsImage(
                ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE),  # choose AMI
            block_devices=[ec2.BlockDevice(
                device_name="/dev/sda1",                        # Root EBS for Windows is always "sda1"
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=30,                             # 30 GB
                    encrypted=True,                             # activate encryption on root EBS
                    )
                ), ec2.BlockDevice(
                device_name="/dev/sdf",                         # define volume name
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=256,                            # 256 GB
                    encrypted=True,                             # activate encryption on attached EBS
                    )
                )]
            )
        
        # # Output the Admin server public IP
        CfnOutput(self, "Adminserver Public IP",
            value=self.instance_adminserver.instance_public_ip,
            export_name="adminserver-public-ip"
            )
        
        # Output the Admin server private IP
        CfnOutput(self, "Adminserver Private IP",
            value=self.instance_adminserver.instance_private_ip,
            export_name="adminserver-private-ip"
            )



        #█████   █████   ██████ ██   ██ ██    ██ ██████  
        #█   ██ ██   ██ ██      ██  ██  ██    ██ ██   ██ 
        #█████  ███████ ██      █████   ██    ██ ██████  
        #█   ██ ██   ██ ██      ██  ██  ██    ██ ██      
        #█████  ██   ██  ██████ ██   ██  ██████  ██


        # Create Backup plan
        self.backup_plan = backup.BackupPlan(self, "backup-plan",
            backup_plan_name="7-day-Backup-plan",
            backup_plan_rules=[backup.BackupPlanRule(
                rule_name="Daily-Retention-7days",
                start_window=Duration.hours(1),             # start within 1 hour of scheduled start
                completion_window=Duration.hours(2),        # complete backup within 2 hours of backup start
                delete_after=Duration.days(7),              # retain backups for 7 days
                schedule_expression=events.Schedule.cron(
                    hour="11",       # Daily backup at 01:00 UTC -->
                    minute="00", )   # --> 02:00 Dutch winter time / 03:00 Dutch summer time
                )]
            )
        
        # Select Webserver as a resource to backup
        self.backup_plan.add_selection("add-webserver", 
            backup_selection_name="backup-webserver",
            resources=[
                backup.BackupResource.from_ec2_instance(self.instance_webserver)
                ]
            )
        
        # Select Adminserver as a resource to backup
        self.backup_plan.add_selection("add-adminserver", 
            backup_selection_name="backup-adminserver",
            resources=[
                backup.BackupResource.from_ec2_instance(self.instance_adminserver)
                ]
            )



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
        self.script_bucket = s3.Bucket(self, "script-bucket",
            # removal_policy=RemovalPolicy.DESTROY, # for testing, auto-delete bucket when "CDK-destroy"-ing
            )

        # Create .zip file of the important scripts
        self.zip_file = "scripts_for_s3.zip" # define filename, directory will be the same as "app.py"
        with ZipFile(self.zip_file, "w") as zip_object:
            zip_object.write("./cdk_vpc_test/cdk_vpc_test_stack.py")    # this current script
            zip_object.write("./cdk_vpc_test/user_data_webs.sh")        # the user data script for webserver
            zip_object.write("app.py")                                  # the app.py script

        # Upload the .zip file to S3 bucket
        s3deploy.BucketDeployment(self, "upload-scripts",
            sources=[s3deploy.Source.asset(self.zip_file)], # define source .zip file
            destination_bucket=self.script_bucket           # refer to S3 script bucket
            )
        
        # Output the name of the created S3 bucket
        CfnOutput(self, "Script Bucket Name",
            value=self.script_bucket.bucket_name,
            export_name="script-bucket-name"
            )



        #██████ ██      ██████                 █████  ███████ 
        #█      ██      ██   ██               ██   ██ ██      
        #████   ██      ██████      █████     ███████ ███████ 
        #█      ██      ██   ██               ██   ██      ██ 
        #██████ ███████ ██████                ██   ██ ███████


        # Create Security Group for Auto Scaling Web servers
        self.sg_as_webserver = ec2.SecurityGroup(self, "sg-as-webserver",
            vpc=self.vpc_webserv,
            description="SG AS Webserver"
            )
        
        # Create Launch Template
        self.launch_template_ws = ec2.LaunchTemplate(self, "ws-launch-template",
            launch_template_name="ws-launch-template",
            security_group=self.sg_as_webserver,
            # associate_public_ip_address=False,
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
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
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
            certificate_arn="arn:aws:acm:eu-central-1:908959576754:certificate/3b2179b4-0384-4855-be19-1fb8b84213f3"
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