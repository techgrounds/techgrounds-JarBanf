#!/usr/bin/env python3

#█ ███    ███ ██████   ██████  ██████  ████████ ███████ 
#█ ████  ████ ██   ██ ██    ██ ██   ██    ██    ██      
#█ ██ ████ ██ ██████  ██    ██ ██████     ██    ███████ 
#█ ██  ██  ██ ██      ██    ██ ██   ██    ██         ██ 
#█ ██      ██ ██       ██████  ██   ██    ██    ███████ 

import aws_cdk as cdk

from cdk_vpc_test.cdk_vpc_test_stack import CdkVpcTestStack


 #█████  ██████  ███    ██ ███████ ██  ██████  
#█      ██    ██ ████   ██ ██      ██ ██       
#█      ██    ██ ██ ██  ██ █████   ██ ██   ███ 
#█      ██    ██ ██  ██ ██ ██      ██ ██    ██ 
 #█████  ██████  ██   ████ ██      ██  ██████

# What is the account number?
account='908959576754'

# In which region will this application deploy?
region='eu-central-1'


 #████  ██████  ██████  
#█   ██ ██   ██ ██   ██ 
#██████ ██████  ██████  
#█   ██ ██      ██      
#█   ██ ██      ██

app = cdk.App()
CdkVpcTestStack(app, "CdkVpcTestStack", 
    env=cdk.Environment(account=account, region=region)
    )

app.synth()
