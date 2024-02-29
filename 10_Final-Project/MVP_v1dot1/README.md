# <a id="top">Minimum Viable Product version 1.1</a>
This is MVP v1.1. Here you will find the AWS CDK application made with Python. 
<br>

## Architecture Design
![Architecture design](/10_Final-Project/MVP_v1dot1/includes/v1dot1_architecture_design.drawio.png)
*Architecture design*  
<br>

## Table of Contents
- [Architecture Design](#architecture-design)
- Table of Contents
- [Design Document](#design-document)
- [v1.1 Packages Specs](#v11-packages-specs)
- [Prepare working environment](#prepare-working-environment)
    - [Set up AWS Account and User](#set-up-aws-account-and-user)
    - [Install AWS CDK Toolkit](#install-aws-cdk-toolkit)
    - [Install Python (and Python package installer (pip))](#install-python-and-python-package-installer-pip)
- [Preconfigurations](#preconfigurations)
    - [Certificate for SSL/TLS](#certificate-for-ssltls)
    - [AWS Account number](#aws-account-number)
    - [AWS Region](#aws-region)
    - [Home/Office IP address](#homeoffice-ip-address)
- [Explore project directory](#explore-project-directory)
- [Deploy the applicaton](#deploy-the-application)
- [Destroy the application](#destroy-the-application)  
<br>

## Design Document
This document contains technical and practical information about the application.  
Architecture Design, Estimated costs, SG & NACL rules, and resource specs are listed here. 

To view the Design Document v1.1, [click here](/10_Final-Project/Documents/design_doc_v1dot1.md).  
<br>

*back to [top](#top)*  
<br>

## v1.1 Packages Specs
| Used Packages | Version |
| - | - |
| AWS CDK | 2.119.0 (build 0392e71) |
| Python | 3.12.1 |
| pip (Package installer for Python) | 23.3.2 |  
<br>

*back to [top](#top)*  
<br>

## Prepare working environment
### Set up AWS Account and User
Follow [this guide](https://cdkworkshop.com/15-prerequisites/200-account.html) to set up your AWS Account and user for programmatic access.  
<br>

### Install AWS CDK Toolkit
- Open a terminal session and run the following command:
    ```bash
    npm install -g aws-cdk
    ```
- To verify the installation, run the following command:
    ```bash
    cdk --version
    ```  
<br>

### Install Python (and Python package installer (pip))
- Follow [this guide](https://cdkworkshop.com/15-prerequisites/600-python.html) to install Python.
- To verify the python installation, run the following command:
    ```bash
    python3 --version
    ```
- Python comes with an ensurepip module, which can install pip in a Python environment.
    ```bash
    python3 -m ensurepip --upgrade
    ```
- Upgrade your pip by running:
    ```bash
    python3 -m pip install --upgrade pip
    ```
- Check the version of pip by running:
    ```bash
    pip --version
    ```  
<br>

*back to [top](#top)*  
<br>

## Preconfigurations
### Certificate for SSL/TLS
- Request or import a certificate for SSL/TLS using AWS Certificate Manager.
- get the ARN of the certificate.  

### AWS Account number
- Get the account number from the AWS console.

### AWS Region
- Choose a region to deploy the application and get the region name. For example `eu-central-1`.

### Home/Office IP address
- Get your home/office IP address you will be using to RDP into the admin server.  
<br>

*back to [top](#top)*  
<br>

## Explore project directory
- Make sure you have a copy of the `MVP_v1dot1`-folder on your local machine.
- Open the project in your favorite IDE.
- `MVP_v1dot1` contains the following files:
    - `.venv` - The python virtual environment.
    - `mvp_v1dot1` — A Python module directory.
        - `lab-app.zip` - The webapp zip file to test the Auto Scaling feature.
        - `mvp_v1dot1_stack.py` - CDK stack construct.
        - `user_data_webs.sh` - The user data script for the web servers.
    - `app.py` — The “main” for this application
    - `cdk.json` — A configuration file for CDK that defines what executable CDK should run to generate the CDK construct tree.
    - `README.md` — This introductory for the project you are currently reading.
    - `requirements.txt` — This file is used by pip to install all of the dependencies for your application.  
<br>

*back to [top](#top)*  
<br>

## Deploy the application
- Open a terminal session and navigate to the `MVP_v1dot1`-folder.
- Activate the virtual environment by running the following command:
    ```bash
    source .venv/bin/activate
    ```
    - If you are using Windows, use the following command:
        ```bash
        .venv\Scripts\activate.bat
        ```
- Install the required python modules by running the following command:
    ```bash
    pip install -r requirements.txt
    ```
- Open the `app.py` file and update the following lines with your own values:
    - Line 21: `account='<your account number>'`
    - Line 24: `region='<your region name>'`
- Open the `mvp_v1dot1/mvp_v1dot1_stack.py` file and update the following lines with your own values:
    - Line 37: `ip_address_administrator="<your ip address>/32"`
    - Line 40: `certificate_arn_alb="<your certificate arn>"`
- Synthesize a template from application code by running the following command:
    ```bash
    cdk synth
    ```
    This will output a CloudFormation template to your terminal session.
- The first time you deploy an AWS CDK app into an environment (account/region), you’ll need to install a “bootstrap stack”. This stack includes resources that are needed for the toolkit’s operation. Bootstrap the environment by running the following command:
    ```bash
    cdk bootstrap
    ```
- Deploy the application by running the following command:
    ```bash
    cdk deploy
    ```
    You will first be informed of security-related changes that the CDK is going to perform on your behalf, if there are any security-related changes. This is warning you that deploying the app contains security-sensitive changes. Since we need to allow the topic to send messages to the queue, enter y to deploy the stack and create the resources.
- AWS CloudFormation will start to deploy the stack. Database creation will take atleast 10 minutes.
- Once stack is deployed, you can view the created resources in the AWS console.

### Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation  
<br>

*back to [top](#top)*  
<br>

## Destroy the application
- To destroy the application, run the following command:
    ```bash
    cdk destroy
    ```
- Some resources will not be deleted automatically. You will need to delete the following manually:
    - S3 buckets
    - Backup vault  
<br>

*back to [top](#top)*  
<br>