#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_testproj.cdk_testproj_stack_network import CdkTestprojStackNetwork
from cdk_testproj.cdk_testproj_stack_webserv import CdkTestprojStackWebserv


app = cdk.App()

deploy_network = CdkTestprojStackNetwork(app, "CdkTestprojStackNetwork")

deploy_webserv = CdkTestprojStackWebserv(app, "CdkTestprojStackWebserv")
deploy_webserv.add_dependency(deploy_network)

app.synth()
