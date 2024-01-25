from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)

from cdk_testproj.cdk_testproj_stack_network import CdkTestprojStackNetwork
from cdk_testproj.cdk_testproj_stack_webserv import CdkTestprojStackWebserv


class CdkTestprojStackMain(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack_network = CdkTestprojStackNetwork(self, "stack-network", 
            env={'region': 'eu-central-1', 'account': '908959576754'} # Needed so .from_lookup() can work.
            )

        stack_webserver = CdkTestprojStackWebserv(self, "stack-webserver")
        
        stack_webserver.add_dependency(stack_network)
