#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_testproj.cdk_testproj_stack_main import CdkTestprojStackMain


app = cdk.App()

CdkTestprojStackMain(app, "stack-main", env=cdk.Environment(account='908959576754', region='eu-central-1'))

app.synth()