from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_ec2 as ec2,
)


class CdkTestprojStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

########################################################################################################

        # create VPC with all default parameters.
        # when no parameters are assigned, it deploys only default values.
        # """
        my_vpc = ec2.Vpc(self, 'MyTestVpc',
            ip_addresses = ec2.IpAddresses.cidr('10.0.0.0/16'), # desired CIDR range
            max_azs=0,
            nat_gateways=0, 
        )

        subnet = ec2.CfnSubnet(self, 'AZa_Webserver',
            vpc_id=my_vpc.vpc_id,
            cidr_block='10.0.10.0/24',
            availability_zone='eu-central-1a',
        )
        # """

########################################################################################################
        
            # Availability zones this VPC spans
        availability_zones = [
            'eu-central-1a', 
            'eu-central-1b',
            # 'eu-central-1c',
        ]

            # 'subnetConfiguration' specifies the "subnet groups" to create.
            # Every subnet group will have a subnet for each AZ, so this
            # configuration will create `amount groups × amount AZs = total` subnets.
        subnet_configuration = [
            ec2.SubnetConfiguration(
                    # 'subnetType' controls Internet access
                subnet_type = ec2.SubnetType.PUBLIC,    # connected to the internet
                
                    # 'name' is used to name this particular subnet group. You will have to
                    # use the name for subnet selection if you have more than one subnet
                    # group of the same type.
                name = 'Webserver',                     # subnet for the webserver and webserver database
                
                    #'cidrMask' specifies the IP addresses in the range of individual
                    # subnets in the group.
                cidr_mask = 28,                         # The subnets in this group will contain: IP adressess 16 (14 usable)
            ),
            ec2.SubnetConfiguration(
                subnet_type = ec2.SubnetType.PUBLIC,    # connected to the internet
                name = 'Adminserver',                   # subnet for the Adminserver
                cidr_mask = 28,                         # IP adressess 16 (14 usable)
            ),
            ec2.SubnetConfiguration(
                subnet_type = ec2.SubnetType.PRIVATE_WITH_EGRESS,   # routes to the internet, but not vice versa.
                name = 'Workstations',                              # subnet for the Workstations
                cidr_mask = 26,                                     # IP adressess 64 (62 usable)
            )
        ]

            #create VPC
        """
        my_vpc = ec2.Vpc(self, 'MyTestVpc',
            availability_zones = availability_zones,    # refers to configuration above
            
                # 'IpAddresses' configures the IP range and size of the entire VPC.
            ip_addresses = ec2.IpAddresses.cidr('10.0.0.0/16'),

                # The number of NAT Gateways to create.
            nat_gateways = 0,
            subnet_configuration = subnet_configuration # refers to configuration above
        )
        """

########################################################################################################