#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_testproj.cdk_testproj_stack import CdkTestprojStack


app = cdk.App()
CdkTestprojStack(app, "CdkTestprojStack")

app.synth()
