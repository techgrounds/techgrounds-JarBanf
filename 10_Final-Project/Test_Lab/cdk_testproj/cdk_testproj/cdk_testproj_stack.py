from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)


class CdkTestprojStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        # Configuration parameters

        # BASIC VPC
        VPC_ID = 'customer-vpc'
        VPC_CIDR = '10.0.0.0/16'

        INTERNET_GATEWAY = 'internet-gateway'
        NAT_GATEWAY_A = 'nat-gateway-a'
        NAT_GATEWAY_B = 'nat-gateway-b'
        NAT_GATEWAY_C = 'nat-gateway-c'
        
        REGION = 'eu-central-1'
        AZ_A = 'eu-central-1a'
        AZ_B = 'eu-central-1b'
        AZ_C = 'eu-central-1c'

        
        #ELASTIC IPs VPC
        ELASTIC_IP_AZ_A = 'elastic-ip-az-a'
        ELASTIC_IP_AZ_B = 'elastic-ip-az-b'
        ELASTIC_IP_AZ_C = 'elastic-ip-az-c'


        # ROUTE TABLES AZ A
        # public route table webserver
        PUB_RT_WEBSERV_A_ID = 'public-route-table-webserver-a'
        PUB_RT_WEBSERV_A_DEST_CIDR = '0.0.0.0/0'
        PUB_RT_WEBSERV_A_GW = INTERNET_GATEWAY
        PUB_RT_WEBSERV_A_RT = ec2.RouterType.GATEWAY

        # public route table adminserver
        PUB_RT_ADMSERV_A_ID = 'public-route-table-adminserver-a'
        PUB_RT_ADMSERV_A_DEST_CIDR = '0.0.0.0/0'
        PUB_RT_ADMSERV_A_GW = INTERNET_GATEWAY
        PUB_RT_ADMSERV_A_RT = ec2.RouterType.GATEWAY

        # private route table workstations
        PRIV_RT_WORKST_A_ID = 'private-route-table-workstations-a'
        PRIV_RT_WORKST_A_DEST_CIDR = '0.0.0.0/0'
        PRIV_RT_WORKST_A_GW = NAT_GATEWAY_A
        PRIV_RT_WORKST_A_RT = ec2.RouterType.NAT_GATEWAY


        # SUBNETS AZ A
        # subnet public webserver
        PUB_SUB_WEBSERV_A_ID = 'public-subnet-webserver-a'
        PUB_SUB_WEBSERV_A_AZ = AZ_A
        PUB_SUB_WEBSERV_A_CIDR = '10.0.1.0/28'
        PUB_SUB_WEBSERV_A_IP_LAUNCH = True
        PUB_SUB_WEBSERV_A_RT_ID = PUB_RT_WEBSERV_A_ID

        # subnet public adminserver
        PUB_SUB_ADMSERV_A_ID = 'public-subnet-adminserver-a'
        PUB_SUB_ADMSERV_A_AZ = AZ_A
        PUB_SUB_ADMSERV_A_CIDR = '10.0.1.16/28'
        PUB_SUB_ADMSERV_A_IP_LAUNCH = True
        PUB_SUB_ADMSERV_A_RT_ID  = PUB_RT_ADMSERV_A_ID

        # subnet private workstations
        PRIV_SUB_WORKST_A_ID = 'private-subnet-workstation-a'
        PRIV_SUB_WORKST_A_AZ = AZ_A
        PRIV_SUB_WORKST_A_CIDR = '10.0.1.64/26'
        PRIV_SUB_WORKST_A_IP_LAUNCH = False
        PRIV_SUB_WORKST_A_RT_ID  = PRIV_RT_WORKST_A_ID

        ##########################################


        # CREATE VPC
        vpc = ec2.Vpc(self, VPC_ID,
                      ip_addresses=ec2.IpAddresses.cidr(VPC_CIDR),
                      nat_gateways=0, # no NAT gateway (yet)
                      subnet_configuration=[] # no subnets (yet)
                      )
        

        # CREATE ELASTIC IPs VPC
        # Create Elastic IP AZ-a
        """
        elastic_ip_a = ec2.CfnEIP(self, ELASTIC_IP_AZ_A)
        """

        # Create Elastic IP AZ-b

        # Create Elastic IP AZ-c
        
        # CREATE AND ATTACH INTERNET GATEWAY VPC
        # Create Internet Gateway
        internet_gateway = ec2.CfnInternetGateway(self, INTERNET_GATEWAY)

        # Attach Internet Gateway to VPC
        # """
        attach_internet_gateway = ec2.CfnVPCGatewayAttachment(self, 'internet-gateway-attachment',
                                                              vpc_id=vpc.vpc_id,
                                                              internet_gateway_id=internet_gateway.ref
                                                              )
        # """
        

        # CREATE ROUTE TABLES AZ A
        # Create Route Table: public for webserver AZ-a
        # """
        cfn_rt_pub_webserv_a = ec2.CfnRouteTable(self, PUB_RT_WEBSERV_A_ID,
                                                 vpc_id=vpc.vpc_id,
                                                 tags=[{'key': 'Name',
                                                        'value': PUB_RT_WEBSERV_A_ID
                                                        }]
                                                 )
        # """
        
        # Create Route Table: public for adminserver AZ-a
        # """
        cfn_rt_pub_admserv_a = ec2.CfnRouteTable(self, PUB_RT_ADMSERV_A_ID,
                                                 vpc_id=vpc.vpc_id,
                                                 tags=[{'key': 'Name',
                                                        'value': PUB_RT_ADMSERV_A_ID
                                                        }]
                                                 )
        # """

        # Create Route Table: private for workstations AZ-a
        # """
        cfn_rt_priv_workst_a = ec2.CfnRouteTable(self, PRIV_RT_WORKST_A_ID,
                                                 vpc_id=vpc.vpc_id,
                                                 tags=[{'key': 'Name',
                                                        'value': PRIV_RT_WORKST_A_ID
                                                        }]
                                                 )
        # """


        # CREATE SUBNETS AZ A
        # Create Subnet: public subnet for webserver AZ-a
        # """
        subnet_pub_webserv_a = ec2.CfnSubnet(self, PUB_SUB_WEBSERV_A_ID,
                                             vpc_id=vpc.vpc_id,
                                             cidr_block=PUB_SUB_WEBSERV_A_CIDR,
                                             availability_zone=PUB_SUB_WEBSERV_A_AZ,
                                             tags=[{'key': 'Name', 
                                                    'value': PUB_SUB_WEBSERV_A_ID
                                                    }],
                                             map_public_ip_on_launch=PUB_SUB_WEBSERV_A_IP_LAUNCH
                                             )
        # """

        # Create Subnet: public subnet for adminserver AZ-a
        # """
        subnet_pub_admserv_a = ec2.CfnSubnet(self, PUB_SUB_ADMSERV_A_ID,
                                             vpc_id=vpc.vpc_id,
                                             cidr_block=PUB_SUB_ADMSERV_A_CIDR,
                                             availability_zone=PUB_SUB_ADMSERV_A_AZ,
                                             tags=[{'key': 'Name', 
                                                    'value': PUB_SUB_ADMSERV_A_ID
                                                    }],
                                             map_public_ip_on_launch=PUB_SUB_ADMSERV_A_IP_LAUNCH
                                             )
        # """

        # Create Subnet: private subnet for workstations AZ-a
        # """
        subnet_priv_workst_a = ec2.CfnSubnet(self, PRIV_SUB_WORKST_A_ID,
                                             vpc_id=vpc.vpc_id,
                                             cidr_block=PRIV_SUB_WORKST_A_CIDR,
                                             availability_zone=PRIV_SUB_WORKST_A_AZ,
                                             tags=[{'key': 'Name', 
                                                    'value': PRIV_SUB_WORKST_A_ID
                                                    }],
                                             map_public_ip_on_launch=PRIV_SUB_WORKST_A_IP_LAUNCH
                                             )
        # """


        # CONNECT ROUTE TABLES TO SUBNETS AZ A
        # Connect: Route Table webserver to Subnet webserver AZ-a
        # """
        rt_webserv_to_sub_webserv_a = ec2.CfnSubnetRouteTableAssociation(self, 'rt-webserv-to-sub-webserv-a',
                                                                         subnet_id=subnet_pub_webserv_a.ref,
                                                                         route_table_id=cfn_rt_pub_webserv_a.ref,
                                                                         )
        # """

        # Connect: Route Table adminserver to Subnet adminserver AZ-a
        # """
        rt_admserv_to_sub_admserv_a = ec2.CfnSubnetRouteTableAssociation(self, 'rt-admserv-to-sub-admserv-a',
                                                                         subnet_id=subnet_pub_admserv_a.ref,
                                                                         route_table_id=cfn_rt_pub_admserv_a.ref,
                                                                         )
        # """

        # Connect: Route Table workstations to Subnet workstations AZ-a
        # """
        rt_workst_to_sub_workst_a = ec2.CfnSubnetRouteTableAssociation(self, 'rt-workst-to-sub-workst-a',
                                                                         subnet_id=subnet_priv_workst_a.ref,
                                                                         route_table_id=cfn_rt_priv_workst_a.ref,
                                                                         )
        # """


        # CREATE NAT GATEWAYS IN VPC
        # Create NAT Gateway AZ-a
        """
        nat_gateway_a = ec2.CfnNatGateway(self, NAT_GATEWAY_A,
                                          allocation_id=elastic_ip_a.attr_allocation_id,
                                          subnet_id=subnet_pub_webserv_a.ref
                                          )
        nat_gateway_a.add_dependency(elastic_ip_a)
        """

        # Create NAT Gateway AZ-b

        # Create NAT Gateway AZ-c


        # CREATE ROUTES AZ A
        # Create Route: Route Table Webserver to Internet Gateway AZ-a
        # """
        route_rt_webserv_to_igw = ec2.CfnRoute(self, 'route-rt-webserv-to-igw',
                             route_table_id=cfn_rt_pub_webserv_a.ref,
                             destination_cidr_block=PUB_RT_WEBSERV_A_DEST_CIDR,
                             gateway_id=internet_gateway.ref
                             )
        # """

        # Create Route: Route Table Adminserver to Internet Gateway AZ-a
        # """
        route_rt_admserv_to_igw = ec2.CfnRoute(self, 'route-rt-admserv-to-igw',
                             route_table_id=cfn_rt_pub_admserv_a.ref,
                             destination_cidr_block=PUB_RT_ADMSERV_A_DEST_CIDR,
                             gateway_id=internet_gateway.ref
                             )
        #"""

        # Create Route: Route Table Workstations to NAT Gateway AZ-a