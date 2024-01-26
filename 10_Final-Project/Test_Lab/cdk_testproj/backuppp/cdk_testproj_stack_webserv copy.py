from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    Fn,
)
import cdk_testproj.cdk_testproj_stack_network as network


# Configuration parameters



class CdkTestprojStackWebserv(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.input_vpc_1_id = Fn.import_value("OutputVPC1")
        # input_vpc_1_id = self.node.try_get_context("OutputVPC1")


        
        # INITIATE STANDARD CODES


        
        # TEST PER RESOURCE CODE
        
        # Create KeyPair
        # keypair_webserv = ec2.KeyPair(self, "keypair-webserv",
        #     key_pair_name="keypair-webserv"
        #     )

        # Lookup existing VPC
        # self.existing_customer_vpc = ec2.Vpc.from_lookup(self, "existing-customer-vpc", vpc_name=network.VPC_1_ID)
        # print(self.existing_customer_vpc)
        # # # Create Security Group for Webserver
        # self.sg_webserver = ec2.SecurityGroup(self, "sg-webserver",
        #     vpc=self.existing_customer_vpc,
        #     description="Security Group Webserver"
        #     )

        # self.web_server = ec2.Instance(self, "web-server",
        #     vpc=self.input_vpc_1_id,
        #     instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
        #     machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023),
        #     # vpc_subnets=vpc_1_network_class().sub_pub_admserv_a
        #     )
        
     
        ################################################################################################
