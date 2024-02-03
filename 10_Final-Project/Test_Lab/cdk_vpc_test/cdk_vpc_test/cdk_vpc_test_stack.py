from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    CfnOutput,
    aws_backup as backup,
    Duration,
    aws_events as events
)


class CdkVpcTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)



        #  ██    ██ ██████   ██████     ██     ██ ███████ ██████  
        #  ██    ██ ██   ██ ██          ██     ██ ██      ██   ██ 
        #  ██    ██ ██████  ██          ██  █  ██ █████   ██████  
        #   ██  ██  ██      ██          ██ ███ ██ ██      ██   ██ 
        #    ████   ██       ██████      ███ ███  ███████ ██████

        
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
                )])



        #  ██    ██ ██████   ██████      █████  ██████  ███    ███ ██ ███    ██ 
        #  ██    ██ ██   ██ ██          ██   ██ ██   ██ ████  ████ ██ ████   ██ 
        #  ██    ██ ██████  ██          ███████ ██   ██ ██ ████ ██ ██ ██ ██  ██ 
        #   ██  ██  ██      ██          ██   ██ ██   ██ ██  ██  ██ ██ ██  ██ ██ 
        #    ████   ██       ██████     ██   ██ ██████  ██      ██ ██ ██   ████


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
                )])
        


        #  ██████  ███████ ███████ ██████  ██ ███    ██  ██████  
        #  ██   ██ ██      ██      ██   ██ ██ ████   ██ ██       
        #  ██████  █████   █████   ██████  ██ ██ ██  ██ ██   ███ 
        #  ██      ██      ██      ██   ██ ██ ██  ██ ██ ██    ██ 
        #  ██      ███████ ███████ ██   ██ ██ ██   ████  ██████
        

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



        #  ███    ██  █████   ██████ ██          ██     ██ ███████ ██████  
        #  ████   ██ ██   ██ ██      ██          ██     ██ ██      ██   ██ 
        #  ██ ██  ██ ███████ ██      ██          ██  █  ██ █████   ██████  
        #  ██  ██ ██ ██   ██ ██      ██          ██ ███ ██ ██      ██   ██ 
        #  ██   ████ ██   ██  ██████ ███████      ███ ███  ███████ ██████                                                             
        

        # Create NACL
        self.nacl_webserver = ec2.NetworkAcl(self, 'nacl-webserver', 
            network_acl_name='nacl-webserver',
            vpc=self.vpc_webserv,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
            )
        

            #    ||
            #    ||
            #   \\//
            #    \/

        # Allow NACL Inbound Ephemeral traffic for Linux kernels. Needed to install httpd.
        self.nacl_webserver.add_entry("Inbound-Ephemeral",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=90,
            traffic=ec2.AclTraffic.tcp_port_range(32768, 60999),
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # Allow NACL Inbound HTTP traffic from anywhere
        self.nacl_webserver.add_entry("Inbound-HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # Allow NACL Inbound SSH traffic from admin server
        self.nacl_webserver.add_entry("Inbound-SSH",
            cidr=ec2.AclCidr.ipv4("10.0.2.4/32"),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS
            )

        # Allow NACL Inbound ICMP (ping) traffic from anywhere
        # self.nacl_webserver.add_entry("Inbound-ICMP",
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
        self.nacl_webserver.add_entry("Outbound-All",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS
            )
        
        

        #  ███    ██  █████   ██████ ██           █████  ██████  ███    ███ 
        #  ████   ██ ██   ██ ██      ██          ██   ██ ██   ██ ████  ████ 
        #  ██ ██  ██ ███████ ██      ██          ███████ ██   ██ ██ ████ ██ 
        #  ██  ██ ██ ██   ██ ██      ██          ██   ██ ██   ██ ██  ██  ██
        #  ██   ████ ██   ██  ██████ ███████     ██   ██ ██████  ██      ██
        

        # Create NACL
        self.nacl_adminserver = ec2.NetworkAcl(self, 'nacl-adminserver', 
            network_acl_name='nacl-adminserver',
            vpc=self.vpc_adminserv,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
            )
        

            #    ||
            #    ||
            #   \\//
            #    \/
            
        # Allow NACL Inbound Ephemeral traffic for Windows Server 2022.
        self.nacl_adminserver.add_entry("Inbound-Ephemeral",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=90,
            traffic=ec2.AclTraffic.tcp_port_range(49152, 65535),
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # Allow NACL Inbound RDP traffic from only my IP
        self.nacl_adminserver.add_entry("Inbound-RDP",
            cidr=ec2.AclCidr.ipv4("143.178.129.147/32"),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(3389),
            direction=ec2.TrafficDirection.INGRESS
            )

        
            #    /\
            #   //\\
            #    ||
            #    ||

        # Allow NACL Outbound traffic
        self.nacl_adminserver.add_entry("Outbound-All",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS
            )

        

        #  ██     ██ ███████ ██████      ███████ ███████ ██████  ██    ██ 
        #  ██     ██ ██      ██   ██     ██      ██      ██   ██ ██    ██ 
        #  ██  █  ██ █████   ██████      ███████ █████   ██████  ██    ██ 
        #  ██ ███ ██ ██      ██   ██          ██ ██      ██   ██  ██  ██  
        #   ███ ███  ███████ ██████      ███████ ███████ ██   ██   ████


        # Create Security Group
        self.sg_webserver = ec2.SecurityGroup(self, "sg-webserver",
            vpc=self.vpc_webserv,
            description="SG Webserver"
            )


            #    ||
            #    ||
            #   \\//
            #    \/
        
        # Allow SG inbound HTTP traffic from anywhere
        self.sg_webserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80),
            description="Allow HTTP traffic from anywhere",
        )

        # Allow SG inbound SSH traffic from admin server
        self.sg_webserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("10.0.2.4/32"),
            connection=ec2.Port.tcp(22),
            description="Allow SSH traffic from admin server",
        )

        # Allow SG inbound ICMP (ping) traffic from anywhere
        # self.sg_webserver.add_ingress_rule(
        #     peer=ec2.Peer.ipv4("0.0.0.0/0"),
        #     connection=ec2.Port.all_icmp(),
        #     description="Allow ICMP traffic from anywhere",
        # )


        # Import User Data for Webserver
        with open("./cdk_vpc_test/user_data_webs.sh") as f:
            self.user_data_webs = f.read()
        
        # Refer to existing Keypair Web Server
        self.keypair_webserver = ec2.KeyPair.from_key_pair_name(self, "keypair-webserver",
            key_pair_name="kp-web-server",
            )

        # Create Webserver instance
        self.instance_webserver = ec2.Instance(self, "instance-webserver",
            instance_name="instance-webserver",
            vpc=self.vpc_webserv,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            private_ip_address="10.0.1.4",
            key_pair=self.keypair_webserver,
            security_group=self.sg_webserver,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023),
            block_devices=[ec2.BlockDevice(
                device_name="/dev/xvda",
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=8,
                    encrypted=True,
                ))],
            user_data=ec2.UserData.custom(self.user_data_webs),
            )



        #   █████  ██████  ███    ███     ███████ ███████ ██████  ██    ██ 
        #  ██   ██ ██   ██ ████  ████     ██      ██      ██   ██ ██    ██ 
        #  ███████ ██   ██ ██ ████ ██     ███████ █████   ██████  ██    ██ 
        #  ██   ██ ██   ██ ██  ██  ██          ██ ██      ██   ██  ██  ██  
        #  ██   ██ ██████  ██      ██     ███████ ███████ ██   ██   ████


        # Create Security Group
        self.sg_adminserver = ec2.SecurityGroup(self, "sg-adminserver",
            vpc=self.vpc_adminserv,
            description="SG Adminserver"
            )
        

            #    ||
            #    ||
            #   \\//
            #    \/
        
        # Allow SG inbound RDP traffic from only my IP
        self.sg_adminserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("143.178.129.147/32"),
            connection=ec2.Port.tcp(3389),
            description="Allow RDP from only my IP",
        )

        # Allow SG inbound ICMP (ping) traffic from anywhere
        self.sg_adminserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.all_icmp(),
            description="Allow ICMP traffic from anywhere",
        )


        # Refer to existing Keypair Admin Server
        self.keypair_adminserver = ec2.KeyPair.from_key_pair_name(self, "keypair-adminserver",
            key_pair_name="kp-admin-server",
            )

        # Create Adminserver instance
        self.instance_adminserver = ec2.Instance(self,"instance-adminserver",
            instance_name="instance-adminserver",
            vpc=self.vpc_adminserv,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            private_ip_address="10.0.2.4",
            key_pair=self.keypair_adminserver,
            security_group=self.sg_adminserver,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            machine_image=ec2.WindowsImage(ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE),
            block_devices=[ec2.BlockDevice(
                device_name="/dev/sda1",
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=30,
                    encrypted=True,
                )
            ), ec2.BlockDevice(
                device_name="/dev/sdf",
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=16,
                    encrypted=True,
                )
            )]
            )
        
        # Output
        CfnOutput(self,
                  "Webserver Private IP",
                  value=self.instance_webserver.instance_private_ip,
                  export_name="webserver-private-ip")
        
        CfnOutput(self,
                  "Webserver Public IP",
                  value=self.instance_webserver.instance_public_ip,
                  export_name="webserver-public-ip")
        
        CfnOutput(self,
                  "Adminserver Private IP",
                  value=self.instance_adminserver.instance_private_ip,
                  export_name="adminserver-private-ip")
        
        CfnOutput(self,
                  "Adminserver Public IP",
                  value=self.instance_adminserver.instance_public_ip,
                  export_name="adminserver-public-ip")



        #  ██████   █████   ██████ ██   ██ ██    ██ ██████  
        #  ██   ██ ██   ██ ██      ██  ██  ██    ██ ██   ██ 
        #  ██████  ███████ ██      █████   ██    ██ ██████  
        #  ██   ██ ██   ██ ██      ██  ██  ██    ██ ██      
        #  ██████  ██   ██  ██████ ██   ██  ██████  ██


        # Create Backup plan
        # self.backup_plan = backup.BackupPlan(self, "backup-plan",
        #     backup_plan_name="7-day-Backup-plan",
        #     backup_plan_rules=[backup.BackupPlanRule(
        #         rule_name="Daily-Retention-7days",
        #         start_window=Duration.hours(1),
        #         completion_window=Duration.hours(2),
        #         delete_after=Duration.days(7),
        #         schedule_expression=events.Schedule.cron(
        #             hour="1", 
        #             minute="0", ) # 01:00 UTC -> 02:00 Dutch winter time / 03:00 Dutch summer time
        #     )]
        #     )
        
        # Select Webserver as a resource to backup
        # self.backup_plan.add_selection("add-webserver", 
        #     backup_selection_name="backup-webserver",
        #     resources=[
        #         backup.BackupResource.from_ec2_instance(self.instance_webserver)
        #         ]
        #     )
        
        # Select Adminserver as a resource to backup
        # self.backup_plan.add_selection("add-adminserver", 
        #     backup_selection_name="backup-adminserver",
        #     resources=[
        #         backup.BackupResource.from_ec2_instance(self.instance_adminserver)
        #         ]
        #     )