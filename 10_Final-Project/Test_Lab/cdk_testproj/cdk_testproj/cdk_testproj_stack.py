from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)


class CdkTestprojStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        # Configuration parameters

        # basic VPC config
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

        
        #Elastic IPs
        ELASTIC_IP_AZ_A = 'elastic-ip-az-a'
        ELASTIC_IP_AZ_B = 'elastic-ip-az-b'
        ELASTIC_IP_AZ_C = 'elastic-ip-az-c'

        # route tables AZ-a
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


        # subnets AZ-a
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
        PUB_SUB_ADMSERV_A_AZ = AZ_A
        PUB_SUB_ADMSERV_A_CIDR = '10.0.1.64/26'
        PUB_SUB_ADMSERV_A_IP_LAUNCH = True
        PUB_SUB_ADMSERV_A_RT_ID  = PRIV_RT_WORKST_A_ID

        ##########################################

        # Create VPC
        vpc = ec2.Vpc(self, VPC_ID,
                      ip_addresses=ec2.IpAddresses.cidr(VPC_CIDR),
                      nat_gateways=0, # no NAT gateway (yet)
                      subnet_configuration=[] # no subnets (yet)
                      )
        
        # Create Elastic IP AZ-a
        # """
        elastic_ip_a = ec2.CfnEIP(self, ELASTIC_IP_AZ_A)
        # """

        # Create Elastic IP AZ-b

        # Create Elastic IP AZ-c
        
        # Create Internet Gateway
        internet_gateway = ec2.CfnInternetGateway(self, INTERNET_GATEWAY)

        # Attach Internet Gateway to VPC
        # """
        attach_internet_gateway = ec2.CfnVPCGatewayAttachment(self, 'internet-gateway-attachment',
                                                              vpc_id=vpc.vpc_id,
                                                              internet_gateway_id=internet_gateway.ref
                                                              )
        # """
        
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

        # Create Route Table: private for workstations AZ-a

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

        # Create Subnet: private subnet for workstations AZ-a

        # Connect: Route Table webserver to Subnet webserver AZ-a
        # """
        rt_webserv_to_sub_webserv_a = ec2.CfnSubnetRouteTableAssociation(self, 'rt-webserv-to-sub-webserv-a',
                                                                         subnet_id=subnet_pub_webserv_a.ref,
                                                                         route_table_id=cfn_rt_pub_webserv_a.ref,
                                                                         )
        # """

        # Connect: Route Table adminserver to Subnet adminserver AZ-a

        # Connect: Route Table workstations to Subnet workstations AZ-a

        # Create NAT Gateway
        # """
        nat_gateway_a = ec2.CfnNatGateway(self, NAT_GATEWAY_A,
                                          allocation_id=elastic_ip_a.attr_allocation_id,
                                          subnet_id=subnet_pub_webserv_a.ref
                                          )
        nat_gateway_a.add_dependency(elastic_ip_a)
        # """

        # Create Route: Route Table Webserver to Internet Gateway
        # """
        route_rt_webserv_to_igw = ec2.CfnRoute(self, 'route-rt-webserv-to-igw',
                             route_table_id=cfn_rt_pub_webserv_a.ref,
                             destination_cidr_block=PUB_RT_WEBSERV_A_DEST_CIDR,
                             gateway_id=internet_gateway.ref
                             )
        # """

        # Create Route: Route Table Adminserver to Internet Gateway
        """
        route_rt_admserv_to_igw = ec2.CfnRoute(self, 'route-rt-admserv-to-igw',
                             route_table_id=PUB_RT_ADMSERV_A_ID,
                             gateway_id=internet_gateway.ref
                             )
        """