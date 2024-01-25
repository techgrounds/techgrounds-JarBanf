from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    CfnOutput,
    Tag
)


# Configuration parameters

# BASIC VPC
VPC_1_ID = 'customer-vpc'
VPC_1_CIDR = '10.0.0.0/16'

INTERNET_GATEWAY_1_ID = 'internet-gateway-1'
NAT_GATEWAY_A_ID = 'nat-gateway-a'
NAT_GATEWAY_B_ID = 'nat-gateway-b'

REGION = 'eu-central-1'
AZ_A = 'eu-central-1a'


#ELASTIC IPs VPC
ELASTIC_IP_AZ_A = 'elastic-ip-az-a'


# ROUTE TABLES AZ A
# public route table webserver
RT_PUB_WEBSERV_A_ID = 'route-table-public-webserver-a'
RT_PUB_WEBSERV_A_DEST_CIDR = '0.0.0.0/0'

# public route table adminserver
RT_PUB_ADMSERV_A_ID = 'route-table-public-adminserver-a'
RT_PUB_ADMSERV_A_DEST_CIDR = '0.0.0.0/0'

# private route table workstations
RT_PRIV_WORKST_A_ID = 'route-table-private-workstations-a'
RT_PRIV_WORKST_A_DEST_CIDR = '0.0.0.0/0'


# SUBNETS AZ A
# public subnet webserver
SUB_PUB_WEBSERV_A_ID = 'subnet-public-webserver-a'
SUB_PUB_WEBSERV_A_CIDR = '10.0.1.0/28'
SUB_PUB_WEBSERV_A_AZ = AZ_A
SUB_PUB_WEBSERV_A_TYPE = "Public"
SUB_PUB_WEBSERV_A_IP_LAUNCH = True

# public subnet adminserver
SUB_PUB_ADMSERV_A_ID = 'subnet-public-adminserver-a'
SUB_PUB_ADMSERV_A_CIDR = '10.0.1.16/28'
SUB_PUB_ADMSERV_A_AZ = AZ_A
SUB_PUB_ADMSERV_A_TYPE = "Public"
SUB_PUB_ADMSERV_A_IP_LAUNCH = True

# private subnet workstations
SUB_PRIV_WORKST_A_ID = 'subnet-private-workstation-a'
SUB_PRIV_WORKST_A_CIDR = '10.0.1.64/26'
SUB_PRIV_WORKST_A_AZ = AZ_A
SUB_PRIV_WORKST_A_TYPE = "Private"
SUB_PRIV_WORKST_A_IP_LAUNCH = False


# NACLs AZ A
# NACL subnet webserver
NACL_SUB_WEBSERV_A_ID = 'nacl-sub-webserv-a'

# NACL subnet adminbserver
NACL_SUB_ADMSERV_A_ID = 'nacl-sub-admserv-a'

# NACL subnet workstation
NACL_SUB_WORKST_A_ID = 'nacl-sub-workst-a'


class CdkTestprojStackNetwork(Stack):
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # INITIATE STANDARD CODES
        # Create VPC
        self.vpc_1 = self.create_vpc(VPC_1_ID, VPC_1_CIDR)

        # Create Elastic IP
        # self.eip_a = self.create_eip(ELASTIC_IP_AZ_A)

        # Create and attach Internet Gateway
        self.igw_1 = self.create_attach_igw(INTERNET_GATEWAY_1_ID, self.vpc_1.vpc_id)

        # Create Route Tables
        self.rt_pub_webserv_a = self.create_route_table(RT_PUB_WEBSERV_A_ID, self.vpc_1.vpc_id)
        self.rt_pub_admserv_a = self.create_route_table(RT_PUB_ADMSERV_A_ID, self.vpc_1.vpc_id)
        self.rt_priv_workst_a = self.create_route_table(RT_PRIV_WORKST_A_ID, self.vpc_1.vpc_id)

        # # Create Subnets
        self.sub_pub_webserv_a = self.create_subnet(SUB_PUB_WEBSERV_A_ID, self.vpc_1.vpc_id, SUB_PUB_WEBSERV_A_CIDR, SUB_PUB_WEBSERV_A_AZ, SUB_PUB_WEBSERV_A_TYPE, SUB_PUB_WEBSERV_A_IP_LAUNCH)
        self.sub_pub_admserv_a = self.create_subnet(SUB_PUB_ADMSERV_A_ID, self.vpc_1.vpc_id, SUB_PUB_ADMSERV_A_CIDR, SUB_PUB_ADMSERV_A_AZ, SUB_PUB_ADMSERV_A_TYPE, SUB_PUB_ADMSERV_A_IP_LAUNCH)
        self.sub_priv_workst_a = self.create_subnet(SUB_PRIV_WORKST_A_ID, self.vpc_1.vpc_id, SUB_PRIV_WORKST_A_CIDR, SUB_PRIV_WORKST_A_AZ, SUB_PRIV_WORKST_A_TYPE, SUB_PRIV_WORKST_A_IP_LAUNCH)

        # # Associate Subnet with Route Table
        self.sub_pub_webserv_a_w_rt = self.ass_sub_w_rt(self.sub_pub_webserv_a.ref, self.rt_pub_webserv_a.ref)
        self.sub_pub_admserv_a_w_rt = self.ass_sub_w_rt(self.sub_pub_admserv_a.ref, self.rt_pub_admserv_a.ref)
        self.sub_priv_workst_a_w_rt = self.ass_sub_w_rt(self.sub_priv_workst_a.ref, self.rt_priv_workst_a.ref)

        # # Create NAT Gateway
        # self.nat_gateway_a = self.create_nat_gateway(NAT_GATEWAY_A_ID, self.eip_a.attr_allocation_id, self.sub_pub_webserv_a.ref)
        # self.nat_gateway_a.add_dependency(self.eip_a)

        # # Associate Internet Gateway to Route Table
        self.igw_w_rt_pub_webserv_a = self.ass_igw_w_rt(self.rt_pub_webserv_a.ref, RT_PUB_WEBSERV_A_DEST_CIDR, self.igw_1.ref)
        # self.igw_w_rt_pub_admserv_a = self.ass_igw_w_rt(self.rt_pub_admserv_a.ref, RT_PUB_ADMSERV_A_DEST_CIDR, self.igw_1.ref)

        # Associate NAT Gateway to Route Table
        # self.natgw_w_rt_priv_workst_a = self.ass_natgw_w_rt(self.rt_priv_workst_a.ref, RT_PRIV_WORKST_A_DEST_CIDR, self.nat_gateway_a.ref)

        # Create & Associate NACL to Subnet
        self.nacl_pub_webserv_a = self.create_ass_nacl_w_sub(NACL_SUB_WEBSERV_A_ID, self.vpc_1, self.sub_pub_webserv_a.ref)
        self.nacl_pub_admserv_a = self.create_ass_nacl_w_sub(NACL_SUB_ADMSERV_A_ID, self.vpc_1, self.sub_pub_admserv_a.ref)
        self.nacl_priv_workst_a = self.create_ass_nacl_w_sub(NACL_SUB_WORKST_A_ID, self.vpc_1, self.sub_priv_workst_a.ref)

        # Allow NACL Inbound traffic
        self.nacl_inb_webserv_a = self.allow_nacl_inbound(self.nacl_pub_webserv_a, "InboundHTTP", ec2.AclCidr.any_ipv4(), 100, ec2.AclTraffic.tcp_port(80))

        # Allow NACL Outbound traffic
        self.nacl_outb_webserv_a = self.allow_nacl_outbound(self.nacl_pub_webserv_a, "OutboundAll", ec2.AclCidr.any_ipv4(), 100, ec2.AclTraffic.all_traffic())


        # Output to Stack Main
        CfnOutput(self, "OutputVPC1", value=self.vpc_1.vpc_id, export_name="OutputVPC1")


        # Create Security Group for Webserver
        self.sg_webserver = ec2.SecurityGroup(self, "sg-webserver",
            vpc=self.vpc_1,
            description="Security Group Webserver"
            )
        
        # Allow SG inbound http traffic
        self.sg_webserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80),
            description="Allow HTTP traffic",
        )
        
        # Lookup existing VPC
        self.existing_customer_vpc = ec2.Vpc.from_lookup(self, "existing-customer-vpc", vpc_name=VPC_1_ID)
 

        # Lookup existing Subnet webserver
        # self.existing_subnet_webserver = ec2.Subnet.from_subnet_id(self, 'existing-subnet-webserver', subnet_id=self.sub_pub_webserv_a.ref)
        # self.existing_subnet_webserver = ec2.SubnetFilter.availability_zones([AZ_A])
        self.existing_subnet_webserver = self.existing_customer_vpc.select_subnets(subnet_type=ec2.SubnetType.PUBLIC)

        # Create Webserver Instance
        self.instance_webserver = ec2.Instance(self, "instance-webserver",
            vpc=self.existing_customer_vpc,
            availability_zone=AZ_A,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023),
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            security_group=self.sg_webserver,
            associate_public_ip_address=True
            )
          
        # self.instance_webserver = ec2.Instance(self, "instance-webserver",
        #     vpc=self.existing_customer_vpc,
        #     availability_zone=AZ_A,
        #     instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
        #     machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023),
        #     vpc_subnets=ec2.SubnetSelection(subnets=([self.sub_pub_webserv_a])),
        #     security_group=self.sg_webserver,
        #     # associate_public_ip_address=True
        #     )


    ################################################################################################


    # STANDARD CODES
    # Code to create VPC
    def create_vpc(self, vpc_id, vpc_cidr):
        vpc = ec2.Vpc(self, vpc_id,
            ip_addresses=ec2.IpAddresses.cidr(vpc_cidr),
            nat_gateways=0, # no NAT gateway (yet)
            subnet_configuration=[], # no subnets (yet)
            vpc_name=vpc_id
        )
        return vpc
        
    # Code to create Elastic IP
    def create_eip(self, elastic_ip_id):
        eip = ec2.CfnEIP(self, elastic_ip_id,
            tags=[{
                'key': 'Name',
                'value': elastic_ip_id
            }]
            )
        return eip
        
    # Code to create and attach Internet Gateway
    def create_attach_igw(self, internet_gateway_id, vpc_id):
        internet_gateway = ec2.CfnInternetGateway(self, internet_gateway_id,
            tags=[{
                'key': 'Name',
                'value': internet_gateway_id
            }]
            )
        attach_internet_gateway = ec2.CfnVPCGatewayAttachment(self, 'internet-gateway-attachment',
            vpc_id=vpc_id,
            internet_gateway_id=internet_gateway.ref
            )
        return internet_gateway

    # Code to create Route Table
    def create_route_table(self, route_table_id, vpc_id):
        route_table = ec2.CfnRouteTable(self, route_table_id,
            vpc_id=vpc_id,
            tags=[{'key': 'Name',
                'value': route_table_id
                }]
            )
        return route_table
        
    # Code to create Subnet
    def create_subnet(self, subnet_id, vpc_id, subnet_cidr, subnet_az, subnet_type, subnet_ip_launch):
        subnet = ec2.CfnSubnet(self, subnet_id,
            vpc_id=vpc_id,
            cidr_block=subnet_cidr,
            availability_zone=subnet_az,
            tags=[{'key': 'Name', 
                'value': subnet_id
                },{'key': 'aws-cdk:subnet-type', 
                'value': subnet_type}],
            map_public_ip_on_launch=subnet_ip_launch
            )
        return subnet
            
    # Code to associate Subnet with Route Table
    ass_sub_w_rt_nr = 1
    def ass_sub_w_rt(self, subnet_id, route_table_id):
        associate_id = "ass-sub-w-rt-"+str(CdkTestprojStackNetwork.ass_sub_w_rt_nr)
        sub_w_rt = ec2.CfnSubnetRouteTableAssociation(self, associate_id,
            subnet_id=subnet_id,
            route_table_id=route_table_id,
            )
        CdkTestprojStackNetwork.ass_sub_w_rt_nr += 1

    # code to create NAT gateway
    def create_nat_gateway(self, nat_gateway_id, eip_allocation_id, subnet_id):
        nat_gateway = ec2.CfnNatGateway(self, nat_gateway_id,
            allocation_id=eip_allocation_id,
            subnet_id=subnet_id,
            tags=[{'key': 'Name', 
                'value': nat_gateway_id
                }],
            )
        return nat_gateway
        
    # Code to associate Internet Gateway to Route Table
    ass_igw_w_rt_nr = 1
    def ass_igw_w_rt(self, route_table_id, dest_cidr_block, gateway_id):
        associate_id = "ass-igw-w-rt-"+str(CdkTestprojStackNetwork.ass_igw_w_rt_nr)
        igw_w_rt = ec2.CfnRoute(self, associate_id,
            route_table_id=route_table_id,
            destination_cidr_block=dest_cidr_block,
            gateway_id=gateway_id
            )
        CdkTestprojStackNetwork.ass_igw_w_rt_nr +=1

    # Code to associate NAT Gateway to Route Table
    ass_natgw_w_rt_nr = 1    
    def ass_natgw_w_rt(self, route_table_id, dest_cidr_block, nat_gateway_id):
        associate_id = "ass-natgw-w-rt-"+str(CdkTestprojStackNetwork.ass_natgw_w_rt_nr)
        natgw_w_rt = ec2.CfnRoute(self, associate_id,
            route_table_id=route_table_id,
            destination_cidr_block=dest_cidr_block,
            nat_gateway_id=nat_gateway_id,
            )
        CdkTestprojStackNetwork.ass_natgw_w_rt_nr +=1

    # Code to create and associate NACL to Subnet
    ass_nacl_w_sub_nr = 1
    def create_ass_nacl_w_sub(self, nacl_id, vpc, subnet_id):
        nacl = ec2.NetworkAcl(self, nacl_id,
            vpc=vpc
            )
        associate_id = "ass-nacl-w-sub-"+str(CdkTestprojStackNetwork.ass_nacl_w_sub_nr)
        ec2.CfnSubnetNetworkAclAssociation(self, associate_id,
            network_acl_id=nacl.network_acl_id,
            subnet_id=subnet_id
            )
        CdkTestprojStackNetwork.ass_nacl_w_sub_nr +=1
        return nacl
        
    # Code to allow NACL Inbound traffic
    def allow_nacl_inbound(self, nacl, rule_name, cidr, rule_number, traffic):
        nacl.add_entry(rule_name,
            cidr=cidr,
            rule_number=rule_number,
            traffic=traffic,
            direction=ec2.TrafficDirection.INGRESS
            )
        
    # Code to allow NACL Outbound traffic
    def allow_nacl_outbound(self, nacl, rule_name, cidr, rule_number, traffic):
        nacl.add_entry(rule_name,
            cidr=cidr,
            rule_number=rule_number,
            traffic=traffic,
            direction=ec2.TrafficDirection.EGRESS
            )