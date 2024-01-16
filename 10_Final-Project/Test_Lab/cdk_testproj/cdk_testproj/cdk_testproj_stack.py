from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_ec2 as ec2,
)


class CdkTestprojStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #create a VPC
        my_vpc = ec2.Vpc(self, 'MyTestVpc',
            #cidr = '10.0.0.0/16',
            #ip_addresses = ec2.IpAddresses.cidr('10.0.0.0/16'),
            #max_azs = 2
        )
