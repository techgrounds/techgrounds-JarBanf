from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)


class CdkVpcTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create VPC 1 & Subnets
        self.vpc_test_1 = ec2.Vpc(self, 'vpc-test-1',
            ip_addresses=ec2.IpAddresses.cidr('10.0.1.0/24'),
            nat_gateways=0,
            max_azs=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name='Webserver',
                    cidr_mask=28
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name='Adminserver',
                    cidr_mask=28
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    name='Workstations',
                    cidr_mask=26
                )
            ]
            )

        # Create VPC 2 & Subnets
        self.vpc_test_2 = ec2.Vpc(self, 'vpc-test-2',
            ip_addresses=ec2.IpAddresses.cidr('10.0.2.0/24'),
            nat_gateways=0,
            max_azs=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name='Webserver2',
                    cidr_mask=28
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name='Adminserver2',
                    cidr_mask=28
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    name='Workstations2',
                    cidr_mask=26
                )
            ]
            )

        #VPC peering
        self.vpc_peering = ec2.CfnVPCPeeringConnection(self,"vpc-peering",
            peer_vpc_id=self.vpc_test_1.vpc_id,
            vpc_id=self.vpc_test_2.vpc_id
            )

        # Create NACLs
        # self.nacl_webserver = ec2.NetworkAcl(self, 'nacl-webserver', 
        #     vpc=self.vpc_test,
        #     network_acl_name='nacl-webserver'
        #     )
        # self.nacl_webserver = ec2.NetworkAcl(self, 'nacl-adminserver', 
        #     vpc=self.vpc_test,
        #     network_acl_name='nacl-adminserver'
        #     )
        # self.nacl_webserver = ec2.NetworkAcl(self, 'nacl-workstations', 
        #     vpc=self.vpc_test,
        #     network_acl_name='nacl-workstations'
        #     )
        
        # Attach NACLs