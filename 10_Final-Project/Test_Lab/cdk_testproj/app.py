#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_testproj.cdk_testproj_stack import CdkTestprojStack
from cdk_testproj.cdk_tesproj_stack_webserv import CdkTestprojStackWebserv


app = cdk.App()
CdkTestprojStack(app, "CdkTestprojStack")
CdkTestprojStackWebserv(app, "CdkTestprojStackWebserv")

app.synth()
