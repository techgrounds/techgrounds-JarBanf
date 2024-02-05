#!/usr/bin/env python3

import aws_cdk as cdk

from mvp_v1dot0.mvp_v1dot0_stack import MvpV1Dot0Stack

env_eu_central = cdk.Environment(account='908959576754', region='eu-central-1')

app = cdk.App()
MvpV1Dot0Stack(app, "MvpV1Dot0Stack", env=env_eu_central)

app.synth()
