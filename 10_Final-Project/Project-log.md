# Project Log
Here I will be logging my daily progress and learnings throughout the project.

## Table of Contents
- [Wednesday 10 Jan '24](#wednesday-10-jan-24)
    - [Set up AWS Cloud Development Kit](#set-up-aws-cloud-development-kit)
- [Tuesday 09 Jan '24](#tuesday-09-jan-24)
- [Monday 08 Jan '24](#monday-08-jan-24)
- [Template](#template)



## Wednesday 10 Jan '24
### Daily Report
Together with my team we had a meeting with the product owner to discuss the requirements for the cloud infrastructure that we individually have to develop. I still have to process these requirements in a document.  

Also, I started with the set-up of AWS CDK on my workstation.

### Obstacles
- Set up AWS Cloud Development Kit.

### Solutions
- #### Set up AWS Cloud Development Kit.

    - Sources:
        - [Working with the AWS CDK in Python](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html)
        - [What is the AWS Command Line Interface?](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)

    - Create Access keys in IAM.
    - Install [AWS Command Line Interface](https://aws.amazon.com/cli/).

        ```bash
        curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
        sudo installer -pkg ./AWSCLIV2.pkg -target /
        ```

    - Verify that the shell can find and run the aws command in my `$PATH`.

        ```bash
        which aws
        aws --version
        ```

        Response:  
        - `/usr/local/bin/aws`
        - `aws-cli/2.15.9 Python/3.11.6 Darwin/21.6.0 exe/x86_64 prompt/off`

    - Configure my workstation so the AWS CDK uses my credentials.

        ```bash
        aws configure
        ```

        ```bash
        AWS Access Key ID [None]: my-access-key-id
        AWS Secret Access Key [None]: my-secret-key-id
        Default region name [None]: eu-central-1
        Default output format [None]: json
        ```

    - Install [Node.js](https://nodejs.org/).
    - Install AWS CDK Toolkit.  
    
        ```bash
        sudo npm install -g aws-cdk
        ```
    
    - Test CDK installation. 
    
        ```bash
        cdk --version
        ```
        
        Response: 
        - `2.118.0 (build a40f2ec)`

    - Install Package Installer for Python (`PIP`) and virtual environment manager (`virtualenv`).

        ```bash
        python3 -m ensurepip --upgrade
        python3 -m pip install --upgrade pip
        python3 -m pip install --upgrade virtualenv
        ```

### Learnings
During the meeting with the product owner I got more information about the cloud infrastructure requirements that I will need to adhere to when developing the cloud infrastructure.

I know now how to set up the AWS CDK on my workstation. That being said, this AWS CDK is still totally new for me. I may have successfully set up AWS CDK on my workstation, but I still do no not understand how it works, and how to interact with it.

*back to [top](#project-log)*  

## Tuesday 09 Jan '24
### Daily Report

### Obstacles

### Solutions

### Learnings

*back to [top](#project-log)* 

## Monday 08 Jan '24
### Daily Report

### Obstacles

### Solutions

### Learnings

*back to [top](#project-log)*  

++++++++++++++++++++
## Template
## insert-date-here
### Daily Report
### Obstacles
### Solutions
### Learnings

*back to [top](#project-log)*  
++++++++++++++++++++