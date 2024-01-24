#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_testproj.cdk_testproj_stack_main import CdkTestprojStackMain


app = cdk.App()

CdkTestprojStackMain(app, "stack-main")

app.synth()