from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_ec2 as ec2,
)


class CdkTestprojStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create VPC with all default parameters.
        # when no parameters are assigned, it deploys only default values.
        """
        my_vpc = ec2.Vpc(self, 'MyTestVpc', 
        )
        """

        # Specify Availability Zones
        availability_zones = [
            'eu-central-1a', 
            # 'eu-central-1b'
        ]

        # Specify Subnet Configuration
        subnet_configuration = [
            ec2.SubnetConfiguration(
                subnet_type = ec2.SubnetType.PUBLIC, # Subnet connected to the internet
                name = 'public 1',
                cidr_mask = 28 # IP adressess 16 (14 usable)
            ),
            ec2.SubnetConfiguration(
                subnet_type = ec2.SubnetType.PUBLIC, # Subnet that routes to the internet, but not vice versa.
                name = 'public 2',
                cidr_mask = 28 # IP adressess 16 (14 usable)
            ),
            ec2.SubnetConfiguration(
                subnet_type = ec2.SubnetType.PRIVATE_WITH_EGRESS, # Subnet that routes to the internet, but not vice versa.
                name = 'private_egress 2',
                cidr_mask = 26 # IP adressess 64 (62 usable)
            )
        ]

        #create VPC ...
        # """
        my_vpc = ec2.Vpc(self, 'MyTestVpc',
            availability_zones = availability_zones,
            ip_addresses = ec2.IpAddresses.cidr('10.0.0.0/16'), # desired CIDR range
            nat_gateways = 0, # Number of NAT Gateways
            subnet_configuration = subnet_configuration
        )
        # """
        
