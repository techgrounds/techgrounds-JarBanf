# <a id="top">My Daily Logs</a> 📓 📅
Here I will be logging my daily progress, solutions, and learnings throughout the project.  

Sorted by latest to oldest.  
<br>

## Table of Contents
- Week 1
    - [Fri 12 Jan '24](#fri-12-jan-24)
        - [Create my first CDK project with AWS CDK Workshop tutorial](#create-my-first-cdk-project-with-aws-cdk-workshop-tutorial)
        - [[SOLVED] Auto-complete for `aws`-commands is not working in VSCode, causing import failure.](#auto-complete-for-aws-commands-is-not-working-in-vscode-causing-import-failure)
    - [Thu 11 Jan '24](#thu-11-jan-24)
    - [Wed 10 Jan '24](#wed-10-jan-24)
        - [Set up AWS Cloud Development Kit](#set-up-aws-cloud-development-kit)
    - [Tue 09 Jan '24](#tue-09-jan-24)
        - [Created a clear and structured document for the infrastructure requirements and questions.](#created-a-clear-and-structured-document-for-the-infrastructure-requirements-and-questions)
    - [Mon 08 Jan '24](#mon-08-jan-24)
        - [Watched an introduction video about Jira.](#watched-an-introduction-video-about-jira)
- [Log template](#log-template)  
<br>

## Fri 12 Jan '24
### ✏️ 📄 
### Daily Report
- I created my first CDK project and tried to understand the process and component.

### Obstacles
- Create my first CDK project with AWS CDK Workshop tutorial
- Auto-complete for `aws`-commands is not working in VSCode, causing import failure.

### Solutions
- #### Create my first CDK project with AWS CDK Workshop tutorial
    - Sources:
        - [AWS CDK Workshop](https://cdkworkshop.com/)
    - Create project directory and go to it.
        
        ```bash
        mkdir cdk_workshop && cd cdk_workshop
        ```

    - Use `cdk init` to create a new Pyhton CDK project.

        ```bash
        cdk init sample-app --language python
        ```

        Response:
        - `✅ All done!`

    - Activate the virtualenv.

        ```bash
        source .venv/bin/activate
        ```

    - Once the virtualenv is activated, install the required dependencies

        ```bash
        pip install -r requirements.txt
        ```

        Response:
        - `Successfully installed attrs-23.2.0 aws-cdk-lib-2.119.0 aws-cdk.asset-awscli-v1-2.2.201 aws-cdk.asset-kubectl-v20-2.1.2 aws-cdk.asset-node-proxy-agent-v6-2.0.1 cattrs-23.2.3 constructs-10.3.0 importlib-resources-6.1.1 jsii-1.94.0 publication-0.0.3 python-dateutil-2.8.2 six-1.16.0 typeguard-2.13.3 typing-extensions-4.9.0`

    - The first time I deploy an AWS CDK app into an environment (account/region), I’ll need to install a “bootstrap stack”.

        ```bash
        cdk bootstrap
        ```
        Response:
        - `✅  Environment aws://908959576754/eu-central-1 bootstrapped.`

    - Before deploying a CDK app, I can synthesize it first to preview the CDK app output CloudFormation file. The output CloudFormation file is the actual thing that gets uploaded into the AWS cloud.  
    To synthesize a CDK app, use the `cdk synth` command.

        ```bash
        cdk synth
        ```
        Response:
        - A CloudFormation template file including the resources.
    
    - Use `cdk deploy` to deploy the CDK app.

        ```bash
        cdk deploy
        ```

        If presented with `Do you wish to deploy these changes (y/n)?`, enter `y`.

        Response:
        - ```bash
            ✅  CdkWorkshopStack

            ✨  Deployment time: 22.37s

            Stack ARN:
            arn:aws:cloudformation:eu-central-1:908959576754:stack/CdkWorkshopStack/0a311dd0-b15d-11ee-abb8-06f21afcb2df

            ✨  Total time: 31.47s
            ```

    - CDK apps are deployed through AWS CloudFormation. This means that I can use the AWS CloudFormation console in order to manage my stacks.

    - To clean up the stack, I can either delete the stack through the AWS CloudFormation console or use `cdk destroy`.

        ```bash
        cdk destroy
        ```

        When asked `Are you sure you want to delete: CdkWorkshopStack (y/n)?`, enter `y`,

        Response:
        - `✅  CdkWorkshopStack: destroyed`
- #### Auto-complete for `aws`-commands is not working in VSCode, causing import failure.
    Install the required python modules BEFORE activating the virtualenv.
    - First:

        ```bash
        pip install -r requirements.txt
        ```
    
    - And then:

        ```bash
        source .venv/bin/activate
        ```

### Learnings
- I know how to create, deploy, and destroy a sample-app project. I have a tiny bit of a understanding how it works.

*back to [top](#top)*  
<br>

## Thu 11 Jan '24
### ✏️ 📄 
### Daily Report
- I completed User Stories ```1: As a team, we want to be clear about the requirements of the application.``` & `3: As a team, we want to have a clear overview of the Cloud Infrastructure that the application needs.` from the `Exploration` Epic

### Obstacles
- ...

### Solutions
- ...

### Learnings
- ...

*back to [top](#top)*  
<br>

## Wed 10 Jan '24
### ✏️ 📄 
### Daily Report
- Together with my team we had a meeting with the product owner to discuss the requirements for the cloud infrastructure that we individually have to develop. I still have to process these requirements in a deliverable document.  

- Also, I started with the set-up of AWS CDK on my workstation.

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
- During the meeting with the product owner I got more information about the cloud infrastructure requirements that I will need to adhere to when developing the cloud infrastructure.

- I know now how to set up the AWS CDK on my workstation. That being said, this AWS CDK is still totally new for me. I may have successfully set up AWS CDK on my workstation, but I still do no not understand how it works, and how to interact with it.

*back to [top](#top)*  
<br>

## Tue 09 Jan '24
### ✏️ 📄 
### Daily Report
- I made a list of questions for our meeting with the product owner tomorrow at 9:15. I also created a clear and structured document where the requirements and questions were categorized.

### Obstacles
- Missing a clear and structured overview of the already known requirements in combination with the questions towards the other not yet known requirements. 

### Solutions
- #### Created a clear and structured [document](https://docs.google.com/drawings/d/1Emfy-G-C1uBrazpZSeBZxsg9z3ydj0bhI2TDCuuZbHs/edit?usp=sharing) for the infrastructure requirements and questions.

### Learnings
- It helps and it is more efficient to create a clear overview for myself and my team of all that we need to go into a meeting prepared.

*back to [top](#top)*  
<br>

## Mon 08 Jan '24
### ✏️ 📄 
### Daily Report
- First day of the project. I read and tried to understand what the project is about and what is expected from me.

- We will be using Jira to track our progress throughout the project. I read and watched a video on what Jira is about. Also made an account.

### Obstacles
- No idea what Jira is about.

### Solutions
- #### Watched an introduction [video](https://www.youtube.com/watch?v=GWxMTvRGIpc) about Jira.

### Learnings
- I have a better understanding why Jira is a handy tool to use during projects.

*back to [top](#top)*  
<br>

++++++++++++++++++++
## Log template
Template for easy daily logging  

## insert-date-here
### ✏️ 📄 
### Daily Report
- ...

### Obstacles
- ...

### Solutions
- ...

### Learnings
- ...

*back to [top](#top)*  
<br>
++++++++++++++++++++