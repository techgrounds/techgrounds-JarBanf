#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_vpc_test.cdk_vpc_test_stack import CdkVpcTestStack

env_eu_central = cdk.Environment(account='908959576754', region='eu-central-1')

app = cdk.App()
CdkVpcTestStack(app, "CdkVpcTestStack", env=env_eu_central)

app.synth()
