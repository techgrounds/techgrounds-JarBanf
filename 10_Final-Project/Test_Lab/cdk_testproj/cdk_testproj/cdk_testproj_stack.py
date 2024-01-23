from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
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
# RT_PUB_WEBSERV_A_GW = INTERNET_GATEWAY_1_ID
# RT_PUB_WEBSERV_A_RT = ec2.RouterType.GATEWAY

# public route table adminserver
RT_PUB_ADMSERV_A_ID = 'route-table-public-adminserver-a'
RT_PUB_ADMSERV_A_DEST_CIDR = '0.0.0.0/0'
# RT_PUB_ADMSERV_A_GW = INTERNET_GATEWAY_1_ID
# RT_PUB_ADMSERV_A_RT = ec2.RouterType.GATEWAY

# private route table workstations
RT_PRIV_WORKST_A_ID = 'route-table-private-workstations-a'
RT_PRIV_WORKST_A_DEST_CIDR = '0.0.0.0/0'
# RT_PRIV_WORKST_A_GW = NAT_GATEWAY_A
# RT_PRIV_WORKST_A_RT = ec2.RouterType.NAT_GATEWAY


# SUBNETS AZ A
# public subnet webserver
SUB_PUB_WEBSERV_A_ID = 'subnet-public-webserver-a'
SUB_PUB_WEBSERV_A_CIDR = '10.0.1.0/28'
SUB_PUB_WEBSERV_A_AZ = AZ_A
SUB_PUB_WEBSERV_A_IP_LAUNCH = True
# SUB_PUB_WEBSERV_A_RT_ID = RT_PUB_WEBSERV_A_ID

# public subnet adminserver
SUB_PUB_ADMSERV_A_ID = 'subnet-public-adminserver-a'
SUB_PUB_ADMSERV_A_CIDR = '10.0.1.16/28'
SUB_PUB_ADMSERV_A_AZ = AZ_A
SUB_PUB_ADMSERV_A_IP_LAUNCH = True
# PUB_SUB_ADMSERV_A_RT_ID  = PUB_RT_ADMSERV_A_ID

# private subnet workstations
SUB_PRIV_WORKST_A_ID = 'subnet-private-workstation-a'
SUB_PRIV_WORKST_A_CIDR = '10.0.1.64/26'
SUB_PRIV_WORKST_A_AZ = AZ_A
SUB_PRIV_WORKST_A_IP_LAUNCH = False
# PRIV_SUB_WORKST_A_RT_ID  = PRIV_RT_WORKST_A_ID


# NACLs AZ A
# NACL subnet webserver
NACL_SUB_WEBSERV_A_ID = 'nacl-sub-webserv-a'

# NACL subnet adminbserver
NACL_SUB_ADMSERV_A_ID = 'nacl-sub-admserv-a'

# NACL subnet workstation
NACL_SUB_WORKST_A_ID = 'nacl-sub-workst-a'


class CdkTestprojStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # STANDARD CODES
        # Code to create VPC
        def create_vpc(vpc_id, vpc_cidr):
            vpc = ec2.Vpc(self, vpc_id,
                ip_addresses=ec2.IpAddresses.cidr(vpc_cidr),
                nat_gateways=0, # no NAT gateway (yet)
                subnet_configuration=[], # no subnets (yet)
                vpc_name=vpc_id
            )
            return vpc
        
        # Code to create Elastic IP
        def create_eip(elastic_ip_id):
            eip = ec2.CfnEIP(self, elastic_ip_id,
                tags=[{
                    'key': 'Name',
                    'value': elastic_ip_id
                }]
                )
            return eip
        
        # Code to create and attach Internet Gateway
        def create_attach_igw(internet_gateway_id, vpc_id):
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
        def create_route_table(route_table_id, vpc_id):
            route_table = ec2.CfnRouteTable(self, route_table_id,
                vpc_id=vpc_id,
                tags=[{'key': 'Name',
                    'value': route_table_id
                    }]
                )
            return route_table
        
        # Code to create Subnet
        def create_subnet(subnet_id, vpc_id, subnet_cidr, subnet_az, subnet_ip_launch):
            subnet = ec2.CfnSubnet(self, subnet_id,
                vpc_id=vpc_id,
                cidr_block=subnet_cidr,
                availability_zone=subnet_az,
                tags=[{'key': 'Name', 
                    'value': subnet_id
                    }],
                map_public_ip_on_launch=subnet_ip_launch
                )
            return subnet
            
        # Code to associate Subnet with Route Table
        self.ass_nr = 1
        def ass_sub_w_rt(subnet_id, route_table_id):
            associate_id = "ass-sub-w-rt-"+str(self.ass_nr)
            sub_w_rt = ec2.CfnSubnetRouteTableAssociation(self, associate_id,
                subnet_id=subnet_id,
                route_table_id=route_table_id,
                )
            self.ass_nr += 1

        # code to create NAT gateway
        def create_nat_gateway(nat_gateway_id, eip_allocation_id, subnet_id):
            nat_gateway = ec2.CfnNatGateway(self, nat_gateway_id,
                allocation_id=eip_allocation_id,
                subnet_id=subnet_id,
                tags=[{'key': 'Name', 
                    'value': nat_gateway_id
                    }],
                )
            return nat_gateway
        
        # Code to associate Internet Gateway to Route Table
        self.ass_igw_w_rt_nr = 1
        def ass_igw_w_rt(route_table_id, dest_cidr_block, gateway_id):
            associate_id = "ass-igw-w-rt"+str(self.ass_igw_w_rt_nr)
            igw_w_rt = ec2.CfnRoute(self, associate_id,
                route_table_id=route_table_id,
                destination_cidr_block=dest_cidr_block,
                gateway_id=gateway_id
                )
            self.ass_igw_w_rt_nr +=1

        # Code to associate NAT Gateway to Route Table
        self.ass_natgw_w_rt_nr = 1    
        def ass_natgw_w_rt(route_table_id, dest_cidr_block, nat_gateway_id):
            associate_id = "ass-natgw-w-rt"+str(self.ass_natgw_w_rt_nr)
            natgw_w_rt = ec2.CfnRoute(self, associate_id,
                route_table_id=route_table_id,
                destination_cidr_block=dest_cidr_block,
                nat_gateway_id=nat_gateway_id,
                )
            self.ass_natgw_w_rt_nr +=1

        # Code to create and associate NACL to Subnet
        self.ass_nacl_w_sub_nr = 1
        def create_ass_nacl_w_sub(nacl_id, vpc, subnet_id):
            nacl = ec2.NetworkAcl(self, nacl_id,
                vpc=vpc
                )
            associate_id = "ass-nacl-w-sub"+str(self.ass_nacl_w_sub_nr)
            ec2.CfnSubnetNetworkAclAssociation(self, associate_id,
                network_acl_id=nacl.network_acl_id,
                subnet_id=subnet_id
                )
            self.ass_nacl_w_sub_nr +=1
            return nacl
        
        # Code to allow NACL Inbound traffic
        def allow_nacl_inbound(nacl, rule_name, cidr, rule_number, traffic):
            nacl.add_entry(rule_name,
                cidr=cidr,
                rule_number=rule_number,
                traffic=traffic,
                direction=ec2.TrafficDirection.INGRESS
                )
            
        # Code to allow NACL Outbound traffic
        def allow_nacl_outbound(nacl, rule_name, cidr, rule_number, traffic):
            nacl.add_entry(rule_name,
                cidr=cidr,
                rule_number=rule_number,
                traffic=traffic,
                direction=ec2.TrafficDirection.EGRESS
                )

        ################################################################################################


        # INITIATE STANDARD CODES
        # Create VPC
        vpc_1 = create_vpc(VPC_1_ID, VPC_1_CIDR)
        
        # Create Elastic IP
        # eip_a = create_eip(ELASTIC_IP_AZ_A)

        # Create and attach Internet Gateway
        igw_1 = create_attach_igw(INTERNET_GATEWAY_1_ID, vpc_1.vpc_id)

        # Create Route Tables
        rt_pub_webserv_a = create_route_table(RT_PUB_WEBSERV_A_ID, vpc_1.vpc_id)
        rt_pub_admserv_a = create_route_table(RT_PUB_ADMSERV_A_ID, vpc_1.vpc_id)
        rt_priv_workst_a = create_route_table(RT_PRIV_WORKST_A_ID, vpc_1.vpc_id)

        # Create Subnets
        sub_pub_webserv_a = create_subnet(SUB_PUB_WEBSERV_A_ID, vpc_1.vpc_id, SUB_PUB_WEBSERV_A_CIDR, SUB_PUB_WEBSERV_A_AZ, SUB_PUB_WEBSERV_A_IP_LAUNCH)
        sub_pub_admserv_a = create_subnet(SUB_PUB_ADMSERV_A_ID, vpc_1.vpc_id, SUB_PUB_ADMSERV_A_CIDR, SUB_PUB_ADMSERV_A_AZ, SUB_PUB_ADMSERV_A_IP_LAUNCH)
        sub_priv_workst_a = create_subnet(SUB_PRIV_WORKST_A_ID, vpc_1.vpc_id, SUB_PRIV_WORKST_A_CIDR, SUB_PRIV_WORKST_A_AZ, SUB_PRIV_WORKST_A_IP_LAUNCH)

        # Associate Subnet with Route Table
        sub_pub_webserv_a_w_rt = ass_sub_w_rt(sub_pub_webserv_a.ref, rt_pub_webserv_a.ref)
        sub_pub_admserv_a_w_rt = ass_sub_w_rt(sub_pub_admserv_a.ref, rt_pub_admserv_a.ref)
        sub_priv_workst_a_w_rt = ass_sub_w_rt(sub_priv_workst_a.ref, rt_priv_workst_a.ref)

        # Create NAT Gateway
        # nat_gateway_a = create_nat_gateway(NAT_GATEWAY_A_ID, eip_a.attr_allocation_id, sub_pub_webserv_a.ref)
        # nat_gateway_a.add_dependency(eip_a)

        # Associate Internet Gateway to Route Table
        igw_w_rt_pub_webserv_a = ass_igw_w_rt(rt_pub_webserv_a.ref, RT_PUB_WEBSERV_A_DEST_CIDR, igw_1.ref)
        igw_w_rt_pub_admserv_a = ass_igw_w_rt(rt_pub_admserv_a.ref, RT_PUB_ADMSERV_A_DEST_CIDR, igw_1.ref)

        # Associate NAT Gateway to Route Table
        # natgw_w_rt_priv_workst_a = ass_natgw_w_rt(rt_priv_workst_a.ref, RT_PRIV_WORKST_A_DEST_CIDR, nat_gateway_a.ref)

        # Create & Associate NACL to Subnet
        nacl_pub_webserv_a = create_ass_nacl_w_sub(NACL_SUB_WEBSERV_A_ID, vpc_1, sub_pub_webserv_a.ref)
        nacl_pub_admserv_a = create_ass_nacl_w_sub(NACL_SUB_ADMSERV_A_ID, vpc_1, sub_pub_admserv_a.ref)
        nacl_priv_workst_a = create_ass_nacl_w_sub(NACL_SUB_WORKST_A_ID, vpc_1, sub_priv_workst_a.ref)

        # Allow NACL Inbound traffic
        nacl_inb_webserv_a = allow_nacl_inbound(nacl_pub_webserv_a, "InboundHTTP", ec2.AclCidr.any_ipv4(), 100, ec2.AclTraffic.tcp_port(80))

        # Allow NACL Outbound traffic
        nacl_outb_webserv_a = allow_nacl_outbound(nacl_pub_webserv_a, "OutboundAll", ec2.AclCidr.any_ipv4(), 100, ec2.AclTraffic.all_traffic())