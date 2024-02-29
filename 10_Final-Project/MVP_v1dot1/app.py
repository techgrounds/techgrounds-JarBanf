#!/usr/bin/env python3

#█ ███    ███ ██████   ██████  ██████  ████████ ███████ 
#█ ████  ████ ██   ██ ██    ██ ██   ██    ██    ██      
#█ ██ ████ ██ ██████  ██    ██ ██████     ██    ███████ 
#█ ██  ██  ██ ██      ██    ██ ██   ██    ██         ██ 
#█ ██      ██ ██       ██████  ██   ██    ██    ███████ 

import aws_cdk as cdk

from mvp_v1dot1.mvp_v1dot1_stack import MvpV1Dot1Stack


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
MvpV1Dot1Stack(app, "MvpV1Dot1Stack",
    env=cdk.Environment(account=account, region=region)
    )

app.synth()
