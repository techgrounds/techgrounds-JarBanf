# <a id="top">My Daily Logs</a> 📓 📅
Here I log my daily progress, solutions, and learnings throughout the project.  

Sorted by latest to oldest.  
<br>

## Table of Contents
- Week 6
    - [Sat 17 Feb '14](#sat17feb)
    - [Fri 16 Feb '14](#fri16feb)
    - [Wed 14 Feb '14](#wed14feb)
        - [ [SOLVED] NACLs keeps blocking my traffic to/from loadbalancer](#nacls-keeps-blocking-my-traffic-tofrom-loadbalancer)
        - [ [SOLVED] “Warning: Remote Host Identification Has Changed”](#warning-remote-host-identification-has-changed)
- Week 5
    - [Fri 09 Feb '24](#fri09feb)
    - [Thu 08 Feb '24](#thu08feb)
        - [ [SOLVED] Traffic between ALB and backend EC2 Instance encrypted via HTTPS using self-signed certificate.](#traffic-between-alb-and-backend-ec2-instance-encrypted-via-https-using-self-signed-certificate)
        - [ [SOLVED] Traffic between ALB and internet clients also encrypted via HTTPS using self-signed certificate.](#traffic-between-alb-and-internet-clients-also-encrypted-via-https-using-self-signed-certificate)
        - [ [SOLVED] Traffic from client to ALB via HTTP automatically redirected to HTTPS.](#traffic-from-client-to-alb-via-http-automatically-redirected-to-https)
    - [Wed 07 Feb '24](#wed07feb)
    - [Tue 06 Feb '24](#tue06feb)
    - [Mon 05 Feb '24](#mon05feb)

- From now on working on v1.1
- v1.0 DONE! (database feature missing, no biggie)  

- Week 4
    - [Sat 03 Feb '24](#sat03feb)
        - [ [SOLVED] Can't upload whole project directory to S3, I get errors.](#cant-upload-whole-project-directory-to-s3-i-get-errors)
    - [Fri 02 Feb '24](#fri02feb)
        - [ [SOLVED] Can not restore backup because I don't have the authorization to do so.](#can-not-restore-backup-because-i-dont-have-the-authorization-to-do-so)
    - [Thu 01 Feb '24](#thu01feb)
    - [Wed 31 Jan '24](#wed31jan)
    - [Tue 30 Jan '24](#tue30jan)
        - [ [Solved] `httpd` not installing when NACL is deployed first](#httpd-not-installing-when-nacl-is-deployed-first)
    - [Mon 29 Jan '24](#mon29jan)
        - [ [SOLVED] Making the instance install `httpd` automatically and using the IPv4 address to display html page.](#making-the-instance-install-httpd-automatically-and-using-the-ipv4-address-to-display-html-page)
- Week 3
    - [Fri 26 Jan '24](#fri26jan)
        - [ [SOLVED] `Vpc.fromLookup` not getting up-to-date situtaion from my existing VPC in the cloud.](#vpcfromlookup-not-getting-up-to-date-situtaion-from-my-existing-vpc-in-the-cloud)
    - [Thu 25 Jan '24](#thu25jan)
        - [ [SOLVED] My "create instance" code does not recognize my VPC and Subnets](#my-create-instance-code-does-not-recognize-my-vpc-and-subnets)
        - [ [SOLVED] Using `from_lookup()` does not work](#using-from_lookup-does-not-work)
    - [Wed 24 Jan '24](#wed24jan)
- Week 2
    - [Sun 21 Jan '24](#sun21jan)
        - [ [SOLVED] I could not get a working code to associate NACL with subnet.](#i-could-not-get-a-working-code-to-associate-nacl-with-subnet)
    - [Sat 20 Jan '24](#sat20jan)
        - [ [SOLVED] Deploy process getting stuck when creating route between route table and nat gateway.](#deploy-process-getting-stuck-when-creating-route-between-route-table-and-nat-gateway
        )
    - [Fri 19 Jan '24](#fri19jan)
    - [Thu 18 Jan '24](#thu18jan)
    - [Wed 17 Jan '24](#wed17jan)
    - [Tue 16 Jan '24](#tue16jan)
        - [Finding and understanding the code I need to deploy a basic VPC.](#finding-and-understanding-the-code-i-need-to-deploy-a-basic-vpc)
    - [Mon 15 Jan '24](#mon15jan)
        - [Write some practice CDK code using cdkworkshop.com. Lambda function & API gateway.](#write-some-practice-cdk-code-using-cdkworkshopcom-lambda-function--api-gateway)
- Week 1
    - [Sun 14 Jan '24](#sun14jan)
    - [Sat 13 Jan '24](#sat13jan)
    - [Fri 12 Jan '24](#fri12jan)
        - [Create my first CDK project with AWS CDK Workshop tutorial](#create-my-first-cdk-project-with-aws-cdk-workshop-tutorial)
        - [[SOLVED] Auto-complete for `aws`-commands is not working in VSCode, causing import failure.](#auto-complete-for-aws-commands-is-not-working-in-vscode-causing-import-failure)
    - [Thu 11 Jan '24](#thu11jan)
    - [Wed 10 Jan '24](#wed10jan)
        - [Set up AWS Cloud Development Kit](#set-up-aws-cloud-development-kit)
    - [Tue 09 Jan '24](#tue09jan)
        - [Created a clear and structured document for the infrastructure requirements and questions.](#created-a-clear-and-structured-document-for-the-infrastructure-requirements-and-questions)
    - [Mon 08 Jan '24](#mon08jan)
        - [Watched an introduction video about Jira.](#watched-an-introduction-video-about-jira)
- [Log template](#log-template)  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="sat17feb">Sat 17 Feb '14</a>
### Daily Report
- Database up and running in public subnet. Still need to test it in a private subnet.
- I succesfully connected to RDS MySQL database using AWS Linux 2023 instance.

### Obstacles
- Connecting to RDS MySQL using AWS Linux 2023 instance.

### Solutions
- #### Connecting to RDS MySQL using AWS Linux 2023 instance.
    - Sources:
        - [Installing MySQL 8 server & client on Amazon Linux 2023](https://linux.how2shout.com/installing-mysql-8-server-client-on-amazon-linux-2023/)
    - Solution:
        - Download MySQL Yum repository
            ```bash
            wget https://dev.mysql.com/get/mysql80-community-release-el9-3.noarch.rpm
            ```
        - Install MySQL Yum repository
            ```bash
            sudo dnf install mysql80-community-release-el9-3.noarch.rpm -y
            ```
        - Update Al2023 Packages
            ```bash
            sudo dnf update -y
            ```
        - Install MySQL 8 on Amazon Linux 2023
            ```bash
            sudo dnf install mysql-community-server -y
            ```
        - Start the service of MySQL
            ```bash
            sudo systemctl start mysqld
            ```
        - Enable it to activate automatically with the  system boot or crash
            ```bash
            sudo systemctl enable mysqld
            ```
        - Check the service status
            ```bash
            sudo systemctl status mysqld
            ```
        - Connect to the RDS instance: (`mysql -h <RDS_ENDPOINT> -u <USERNAME> -p`)
            ```bash
            mysql -h cdkvpcteststack-databasewebserver14fd81e3-9szt0qt33ueo.coxnyfceatsl.eu-central-1.rds.amazonaws.com -u admin -p
            ```
        - Get password from AWS Secrets Manager and enter it.
        - Connected!!! :)

### Learnings
- ...  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="fri16feb">Fri 16 Feb '24</a>
### Daily Report
- Started working on the RDS MySQL database.
- Managed to create a database. Took almost 18 minutes to deploy.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="wed14feb">Wed 14 Feb '14</a>
### Daily Report
- Updating my NACLs to the current situation.

### Obstacles
- NACLs keeps blocking my traffic to/from loadbalancer.
- “Warning: Remote Host Identification Has Changed”.

### Solutions
- #### NACLs keeps blocking my traffic to/from loadbalancer.
    - Sources:
        - [Network ACLs for load balancers in a VPC](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html#elb-vpc-nacl)
    - Solution:
        - Allow the correct inbound and outbound ports

- #### “Warning: Remote Host Identification Has Changed”.
    - Sources:
        - [How To Fix the “Warning: Remote Host Identification Has Changed” Error](https://kinsta.com/knowledgebase/warning-remote-host-identification-has-changed/)
    - Solution:
        - Remove old key from known_hosts file. 

### Learnings
- NACLs help provide a security layer which controls and efficiently manages the traffic that moves around in the subnets. It is important to configure them correctly. I have to be able to know exactly which ports, protocols and destination are used.   
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="fri09-feb">Fri 09 Feb '24</a>
### Daily Report
- Gave my progresion presentation. According to the learning coach I'm 90% done with my project. This is nice to hear.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="thu08feb">Thu 08 Feb '24</a>
### Daily Report
- Traffic between ALB and backend EC2 Instance is encrypted via HTTPS using self-signed certificate.
- Traffic between ALB and internet clients can also be encrypted via HTTPS using self-signed certificate.
- Traffic from client to ALB via HTTP is automatically redirected to HTTPS.

### Obstacles
- Traffic between ALB and backend EC2 Instance encrypted via HTTPS using self-signed certificate.
- Traffic between ALB and internet clients also encrypted via HTTPS using self-signed certificate.
- Traffic from client to ALB via HTTP automatically redirected to HTTPS.

### Solutions
- #### Traffic between ALB and backend EC2 Instance encrypted via HTTPS using self-signed certificate.
    - Sources:
        - [Traffic between ALB and backend EC2 Instance needs to be encrypted](https://repost.aws/questions/QU97HoG_YMQxO1LXTj76ui-w/traffic-between-alb-and-backend-ec2-instance-needs-to-be-encrypted)
        - [Securing Apache HTTPD](https://docs.fedoraproject.org/en-US/quick-docs/getting-started-with-apache-http-server/#_securing_apache_httpd)
    - Solution:
        - Add the following to the user data:  
            ```bash
            # Enable TLS/SSL support, mod_ssl also automatically creates a self-signed certificate.
            sudo dnf install mod_ssl -y
            # Fully restart Apache
            sudo systemctl restart httpd.service
            ```
        - Change port in Target group from 80 (HTTP) to 443 (HTTPS):   
            ```py
            # Create Target Group for ALB
            self.target_group = elbv2.ApplicationTargetGroup(self, "target-group",
            vpc=self.vpc_webserv,
            port=443,
            targets=[self.auto_scaling_group],
            )
            ```
        - I tested it out and it works with all the instances spinning up via Auto Scaling.

- #### Traffic between ALB and internet clients also encrypted via HTTPS using self-signed certificate.
    - Sources:
        - [TLS on AWS LB Using Self Signed Certificate](https://www.youtube.com/watch?v=45dmwFAZF9g)
    - Solution: Spin up a linux server. On this server I will create a self-signed certificate. This certificate information I will then import in AWS Certificate Manager via the console.
        - Spin up linux server.
        - Generate .key file:  
            ```bash
            openssl genrsa -out keyfile.key 4096
            ```
        
        - Generate CSR(Certificate Signing Request) file using keyfile.key:
            ```bash
            openssl req -new -key keyfile.key -out csrfile.csr
            ```

        - Fill in information requested. Values have to valid input (for example: common name has to end with top-level-domain like ".com"), but does not have to be existing. No password input needed.
        - Self-sign the .csr file:
            ```bash
            openssl x509 -in csrfile.csr -out cert.crt -req -signkey keyfile.key -days 365
            ```
        - Copy contents of cert.crt and paste in AWS Certificate Manager in "Certificate body".
            ```bash
            cat cert.crt
            ```
        - Copy contents of keyfile.key and paste in AWS Certificate Manager in "Certificate private key".
        - Go ahead and Create Certificate. Copy the ARN of the certificate I just created so I can refer to it in CDK.
        - In CDK, import certificate and add it to the listener.
            ```py
            # Import self signed certificate from console
            self.certificate_ss_imp = cm.Certificate.from_certificate_arn(self, "certificate-ss-imp",
                certificate_arn="arn:aws:acm:eu-central-1:908959576754:certificate/3b2179b4-0384-4855-be19-1fb8b84213f3"
                )
            
            # Add listener to the ALB for port 443
            self.https_listener = self.load_balancer_ws.add_listener("https_listener",
                port=443,
                ssl_policy=elbv2.SslPolicy.RECOMMENDED_TLS,
                certificates=[self.certificate_ss_imp],
                default_target_groups=[self.target_group]
                )
            ```
        - I tested it and it works! I can connect to load balancer using HTTPS.

- #### Traffic from client to ALB via HTTP automatically redirected to HTTPS.
    - Sources:
        - ChatGPT
        - [ApplicationLoadBalancer](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_elasticloadbalancingv2/ApplicationLoadBalancer.html)
        - [ListenerAction](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_elasticloadbalancingv2/ListenerAction.html#aws_cdk.aws_elasticloadbalancingv2.ListenerAction)
    - Solution:
        - Add redirect on listener port 80:
            ```py
            # Add listener to the ALB for port 80 and redirect traffic to port 443
            self.http_listener = self.load_balancer_ws.add_listener("http_listener",
                port=80,
                default_action=elbv2.ListenerAction.redirect(
                    port="443",
                    protocol="HTTPS",
                    )
                )
            ```

### Learnings
- What is needed to setup HTTPS and also create self signed certificates.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="wed07feb">Wed 07 Feb '24</a>
### Daily Report
- My loadbalancer and autoscaling are working in 2 different setups:
    - Setup 1: Webservers in public subnet with public IP so linux can download apache webserver.
    - Setup 2: Webservers in private subnet with NAT gateway so linux can download apache webserver.

- NAT gateway is expensive. So there is another way to setup webserver without public IP and also without NAT gateway. I am thinking to use an AMI that already has all the configuration on it. So there is no need for the webserver to access the internet to download anything.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="tue06feb">Tue 06 Feb '24</a>
### Daily Report
- Figuring out the codes for Load Balancers and Autoscaling.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="mon05feb">Mon 05 Feb '24</a>
### Daily Report
- MVP v1.0 is done and repository is tagged in GitHub! 
- Database is still missing, but that is no hard requirement.
- I didn't have time to draft a document for using the application. I will do this for v1.1
- Reading up on Reverse Proxy  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="sat03feb">Sat 03 Feb '24</a>
### Daily Report
- Succesfully SSH-ed into webserver from adminserver via private IP address.
- Security Groups and NACLs are also set up properly.
- S3 bucket create
- Scripts automatically uploads to S3 Bucket

### Obstacles
- Can't upload whole project directory to S3, I get errors.

### Solutions
- #### Can't upload whole project directory to S3, I get errors.
    - Sources:
        - [How to create a zip file using Python?](https://www.tutorialspoint.com/How-to-create-a-zip-file-using-Python)
    - Solution:
        - First I select the important script files that are worth uploading to S3.
        - I then create a .zip file of these scripts.
        - And then upload the .zip file to the S3 bucket.

        Working code:
        ```py
        # Create S3 Bucket for Scripts
        self.script_bucket = s3.Bucket(self, "script-bucket",
            removal_policy=RemovalPolicy.DESTROY, # for testing, auto-delete bucket when "CDK-destroy"-ing
            )

        # Create .zip file of the important scripts
        self.zip_file = "scripts_for_s3.zip"
        with ZipFile(self.zip_file, "w") as zip_object:
            zip_object.write("./cdk_vpc_test/cdk_vpc_test_stack.py")
            zip_object.write("./cdk_vpc_test/user_data_webs.sh")
            zip_object.write("app.py")

        # Upload the .zip file to S3 bucket
        s3deploy.BucketDeployment(self, "upload-scripts",
            sources=[s3deploy.Source.asset(self.zip_file)],
            destination_bucket=self.script_bucket
            )
        ```

### Learnings
- ...  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="fri02feb">Fri 02 Feb '24</a>
### Daily Report
- Backup of my servers work. I also managed to restore a backup. So Backup = Done!

### Obstacles
- Can not restore backup because I don't have the authorization to do so.

### Solutions
- #### Can not restore backup because I don't have the authorization to do so.
    - Sources:
        - [EC2 Instance Restore: "You are not authorized to perform this operation"](https://repost.aws/questions/QUHiD7geQrR6mKhUzhWyMZLQ/ec2-instance-restore-you-are-not-authorized-to-perform-this-operation)
    - The error message i get:
        `You are not authorized to perform this operation. Please consult the permissions associated with your AWS Backup role(s), and refer to the AWS Backup documentation for more details. User: arn:aws:sts::908959576754:assumed-role/AWSServiceRoleForBackup/AWSBackup-AWSServiceRoleForBackup is not authorized to perform: iam:PassRole on resource: arn:aws:iam::908959576754:role/CdkVpcTestStack-instancewebserverInstanceRole6FB4F7-hqnAwNWH4BLo because no identity-based policy allows the iam:PassRole action. Encoded authorization failure message: Slxg7-xAy-leso4qPxgQOXgi1MFaUR_YwaXFMLEnhwPQ6Nsn8zTYjMgGdbJ-m1oOdMzSakw8ks3tJAqkEXbUFuMyYCPdu5_Id1uWDt18NNnGpS2NigLy_C4QohEqPMDKMt6z77qj-rNKwso71hb0WRVEpZosX7AJOzhG7dMNlsvxlyQ2wgimjZdjbHY3zVrUmL2atq2qykipsF_x59zlbRqDIEPWmzZmt-q3-RGg34vghPD8BHFlmA6LVpCH6_sdy35It4-JtLGZP1k07hMJnVlYat7kGKSldSc5I2nhs1NoA5cdlFVU6pB3E_faTKUgc2HFpHuwPRZ8PaYCTuaqv_Dnl6FbTD4vT-21ge-VCDOEqwx1shc0Z1HPPLPBWbOE1hsRHxxBM-85jxLbCoDNN3B5E-fPfxV9wnaFe_E0dutocYR6_rRaVz1uJPciI_K7sf-gHiLz53DudTLFaLNk58MY1Atkf_7jdugc5TaOBMzcDPfJ3wAQY_mGDDTrw4SMeMKZM1iEYSJTzc6Nd9w0gMF3YlZ71j6vgi5oW5Rfi9lan5W1GkX4Sv7wa8CIjXLLQtaWm9Up-SobG1KevfKEK6zv`
    - Solution:
        I needed to add the following policy to the `AWSBackupDefaultServiceRole`.
        ```json
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "iam:PassRole",
                    "Resource": "arn:aws:iam::account_id_here:role/*",
                    "Effect": "Allow"
                }
            ]
        }
        ```

### Learnings
- Ik begrijp wat meer wat voor invloed "Roles" heeft op services.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="thu01feb">Thu 01 Feb '24</a>
### Daily Report
- EBS root volume for Admin Server encrypted
- EBS attached volume for Admin Server encrypted
- EBS root volume for Web Server encrypted
- Create Backup plan
- Selected Web server and Admin server as resources to backup
- I still need to test if the backup works.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="wed31jan">Wed 31 Jan '24</a>
### Daily Report
- RDP from my own IP to Admin Server instance succesful. Also NACL rules are well defined.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="tue30jan">Tue 30 Jan '24</a>
### Daily Report
- Figured out the NACL issue.

### Obstacles
- `httpd` not installing when NACL is deployed first.

### Solutions
- #### `httpd` not installing when NACL is deployed first.
    - sources
        - [Ephemeral port](https://en.wikipedia.org/wiki/Ephemeral_port)
    - NACL did not allow incomming connections to install/download httpd. I needed to add a rule allowing incomming traffic for downloading httpd.

        rule to allow:
        ```py
        # Allow NACL Inbound Ephemeral traffic. Needed to install httpd.
        self.nacl_webserver.add_entry("Inbound-Ephemeral",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=90,
            traffic=ec2.AclTraffic.tcp_port_range(32768, 60999),
            direction=ec2.TrafficDirection.INGRESS
            )
        ```

### Learnings
- Think about ephemeral ports when setting up firewall rules.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="mon29jan">Mon 29 Jan '24</a>
### Daily Report
- Webserver up and running with user data.
- VPC Peering Connection active.
- VPC Peering Connection connected to the route tables in different VPC.

### Obstacles
- Making the instance install `httpd` automatically and using the IPv4 address to display html page.

### Solutions
- #### Making the instance install `httpd` automatically and using the IPv4 address to display html page.
    - In my user data I was using a `!`-sign which the bash shell does not appreciate. this caused the instance not to properly display the indext.html page. Removed the `!` from the user data and voila!

        NOT-working user data:
        ```sh
        #!/bin/bash
        sudo yum install -y httpd
        sudo systemctl start httpd
        sudo systemctl enable httpd
        sudo su
        echo "<h1>Hello From Jared's CDK created Web Server!</h1>" > /var/www/html/index.html
        ```

        WORKING user data:
        ```sh
        #!/bin/bash
        sudo yum install -y httpd
        sudo systemctl start httpd
        sudo systemctl enable httpd
        sudo su
        echo "<h1>Hello From Jared's CDK created Web Server :)</h1>" > /var/www/html/index.html
        ```

### Learnings
- I have a bit more understanding how route tables work.   
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="fri26jan">Fri 26 Jan '24</a>
### Daily Report
- Gave my progression presentation
- Working on the user data and making the webserver instance to install `httpd` automatically and display a simple html page.

### Obstacles
- Making the instance install `httpd` automatically and using the IPv4 address to display html page.
- `Vpc.fromLookup` not getting up-to-date situtaion from my existing VPC in the cloud.
  
### Solutions
- #### `Vpc.fromLookup` not getting up-to-date situtaion from my existing VPC in the cloud.
    - Sources
        - [Runtime context](https://docs.aws.amazon.com/cdk/v2/guide/context.html)
    - I needed to clear my `cdk.context.json` file.

        ```py
        cdk context --clear
        ```

        When I run `cdk synth` again, it will pick up my up-to-date situation from my existing VPC in the cloud.

<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="thu25jan">Thu 25 Jan '24</a>
### Daily Report
- I am able to create an instance

### Obstacles
- My "create instance" code does not recognize my VPC and Subnets.

- Using `from_lookup()` does not work.
    - Error: `RuntimeError: Error: Cannot retrieve value from context provider vpc-provider since account/region are not specified at the stack level. Configure "env" with an account and region when you define your stack.See https://docs.aws.amazon.com/cdk/latest/guide/environments.html for more details.`

### Solutions
- #### My "create instance" code does not recognize my VPC and Subnets.
    - sources:
        - [VPC Static Methods from_lookup()](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ec2/Vpc.html#aws_cdk.aws_ec2.Vpc.from_lookup)
    - I stopped reffering to the vpc directly in my code. Instead I used `from_lookup()` to look up the created/running VPC in my cloud environment. And use that information to pass it on to the "create instance" code.

        My NOT-working code looked like this:

        ```py
        # Create VPC
        self.vpc_1 = ...code to create a vpc without subnets...

        # Create Subnet
        self.subnet_webserver = ...code to create a public subnet...

        # Create Webserver Instance
        self.instance_webserver = ec2.Instance(self, "instance-webserver",
            vpc=self.vpc_1, # referring to my vpc in my code
            availability_zone=AZ_A,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023),
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC), # this code looks for a public subnet in my vpc
            security_group=self.sg_webserver,
            associate_public_ip_address=True
            )
        ```

        My WORKING code is now this:

        ```py
        # Create VPC
        self.vpc_1 = ...code to create a vpc without subnets...

        # Create Subnet
        self.subnet_webserver = ...code to create a public subnet...
        
        # Lookup existing VPC
        self.existing_customer_vpc = ec2.Vpc.from_lookup(self, "existing-customer-vpc", vpc_name=VPC_1_ID)

        # Create Webserver
        self.instance_webserver = ec2.Instance(self, "instance-webserver",
            vpc=self.existing_customer_vpc,
            availability_zone=AZ_A,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023),
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            security_group=self.sg_webserver,
            associate_public_ip_address=True,
            )
        ```
        
 - #### Using `from_lookup()` does not work.
    - Error: `RuntimeError: Error: Cannot retrieve value from context provider vpc-provider since account/region are not specified at the stack level. Configure "env" with an account and region when you define your stack.See https://docs.aws.amazon.com/cdk/latest/guide/environments.html for more details.`
    - Sources:
        - [Environments](https://docs.aws.amazon.com/cdk/v2/guide/environments.html)
        - [Vpc.fromLookup can't determine region](https://github.com/aws/aws-cdk/issues/4846)
    - Needed to add `env={'region': 'my-region', 'account': 'my-account'}` to `stack_network = CdkTestprojStackNetwork(self, "stack-network",)` in my `StackMain`.

        Now it works :).
        ```py
        from constructs import Construct
        from aws_cdk import (
            Stack,
            aws_ec2 as ec2,
        )

        from cdk_testproj.cdk_testproj_stack_network import CdkTestprojStackNetwork
        from cdk_testproj.cdk_testproj_stack_webserv import CdkTestprojStackWebserv


        class CdkTestprojStackMain(Stack):

            def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
                super().__init__(scope, construct_id, **kwargs)

                stack_network = CdkTestprojStackNetwork(self, "stack-network", 
                    env={'region': 'eu-central-1', 'account': '908959576754'} # Needed so .from_lookup() can work.
                    )

                stack_webserver = CdkTestprojStackWebserv(self, "stack-webserver")
                
                stack_webserver.add_dependency(stack_network)
        ```   
<br>

## ✏️ 📄 <a id="wed24jan">Wed 24 Jan '24</a>
### Daily Report
- Busy with the creation of an insance

### Obstacles
- My "create instance" code does not recognize my subnet in my VPC.  
<br>

## ✏️ 📄 <a id="sun21jan">Sun 21 Jan '24/a>
### Daily Report
- Created:
    - NACLs for the 3 subnets in AZ a
    - Association between NACLs and subnet

### Obstacles
- I could not get a working code to associate NACL with subnet.

### Solutions
- #### I could not get a working code to associate NACL with subnet.
    - I was using the `.associate_with_subnet`-method to try and associate NACL with subnet. I could not get it to work. ChatGPT suggested I use `.CfnSubnetRouteTableAssociation`. This end up working.

        Working code:

        ```py
        ec2.CfnSubnetNetworkAclAssociation(self, 'nacl-to-sub-webserv-a',
            network_acl_id=nacl_sub_webserv_a.network_acl_id,
            subnet_id=subnet_pub_webserv_a.ref
            )
        ```  
<br>

*back to [top](#top)*  
<br>
++++++++++

## ✏️ 📄 <a id="sat20jan">Sat 20 Jan '24</a>
### Daily Report
- Created: 
    - route table: 
        - for public subnet Admin server.
        - for private subnet Workstations.
    - subnet:
        - public subnet for Admin server.
        - private subnet Workstations.
    - elastic IP.
    - nat gateway in public subnet AZ a.
    - routes:
        - between public subnet Admin server and Internet gateway.
        - between private subnet Workstations and Nat gateway.

### Obstacles
- Deploy process getting stuck when creating route between route table and nat gateway.

### Solutions
- #### Deploy process getting stuck when creating route between route table and nat gateway.
    - Sources:
        - [AWS CDK Python Reference](https://docs.aws.amazon.com/cdk/api/v2/python/)
    - Used the wrong attribute to assign nat gateway.  
        Wrong code:  

        ```py
        route_rt_workst_to_natgw = ec2.CfnRoute(self, 
            'route-rt-workst-to-natgw',
            route_table_id=cfn_rt_priv_workst_a.ref,
            destination_cidr_block=PRIV_RT_WORKST_A_DEST_CIDR,
            gateway_id=nat_gateway_a.ref,
            )
        ```
    
        Correct code:  

        ```py
        route_rt_workst_to_natgw = ec2.CfnRoute(self, 
            'route-rt-workst-to-natgw',
            route_table_id=cfn_rt_priv_workst_a.ref,
            destination_cidr_block=PRIV_RT_WORKST_A_DEST_CIDR,
            nat_gateway_id=nat_gateway_a.ref,
            )
        ```

### Learnings
- Check if I have selected the right attribute. Use [AWS CDK Python Reference](https://docs.aws.amazon.com/cdk/api/v2/python/) frequently to check for the correct attributes I will be needing.   
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="fri19jan">Fri 19 Jan '24</a>
### Daily Report
- Watched a video shared by a co-student: ([ Create AWS VPC Infrastructure with AWS CDK & PYTHON | Subnets, Route Tables, Gateway, NAT with CDK ](https://www.youtube.com/watch?v=ZmbcgRpGmrs))
- Created:
    - vpc
    - internet gateway & attachmenet to vpc
    - route table:
        - for public subnet Web server
    - subnet:
        - public subnet for Web server
    - routes:
        - between public subnet Web server and Internet Gateway.

### Obstacles
- Understanding the `for`-loops used in the video.

### Solutions
- Understanding the `for`-loops used in the video.
    - I analyzed the code use and followed the code flow to understand what the purpose and the results were of the `for`-loops.

### Learnings
- When Python is used correctly, it can make your code efficient and less prone to user error. I still feel uncomforable using the `for`-loops the way the video does. So for now, I will not be using the `for`-loops (yet). Instead my code will be less efficient, but I will atleast be able to troubleshoot and explain my code.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="thu18jan">Thu 18 Jan '24</a>
### Daily Report
- Searching and testing out codes for creating VPC related resources.

### Obstacles
- Understanding CDK codes, their usage, their attributes.

### Solutions
- Understanding CDK codes, their usage, their attributes.
    - See [Wed 17 Jan '24](#wed17jan)  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="wed17jan">Wed 17 Jan '24</a>
### Daily Report
- Meeting with my talent coach
- On LinkedIn, activated the feature that recruiters can see that I'm open for work.
- Searching and testing out codes for creating VPC related resources.

### Obstacles
- Understanding CDK codes, their usage, their attributes.

### Solutions
- Understanding CDK codes, their usage, their attributes.
    - Sources:
        - ChatGPT
        - [AWS CDK Python Reference](https://docs.aws.amazon.com/cdk/api/v2/python/)
    - Used ChatGPT and other CDK-pyhton examples to give me an idea how the codes are used. These examples I also compared to the AWS CDK Python Reference to get a better understanding of how the parameters explanation compares to the actual code.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="tue16jan">Tue 16 Jan '24</a>
### Daily Report
- I made a first version diagram of the network infrastructre. I will be using this diagram as a starting point to start building the network as IaC.
- I started with:  
    | Epic | User Story | Description | Deliverable |
    | - | - | - | - |
    | v1.0 | As a customer, I want a working application with which I can deploy a secure network. | The application must build a network that meets all requirements. An example of a stated requirement is that only traffic from trusted sources may access the management server. | 1. IaC code for the network and all components. |

### Obstacles
- Finding and understanding the code I need to deploy a basic VPC

### Solutions
- #### Finding and understanding the code I need to deploy a basic VPC.
    - Sources
        - [Vpc](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ec2/Vpc.html)
        - [GitHub aws-cdk-examples](https://github.com/aws-samples/aws-cdk-examples/blob/master/python/ec2/instance/app.py)
        - ChatGPT
    - Working code to deploy VPC with only default parameters.

        ```py
        from constructs import Construct
        from aws_cdk import (
            Duration,
            Stack,
            aws_ec2 as ec2,
        )


        class CdkTestprojStack(Stack):

            def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
                super().__init__(scope, construct_id, **kwargs)

                #create a VPC
                my_vpc = ec2.Vpc(self, 'MyTestVpc',
                    #cidr = '10.0.0.0/16',
                    #ip_addresses = ec2.IpAddresses.cidr('10.0.0.0/16'),
                    #max_azs = 2
                )
        ```

### Learnings
- I know which construct I need to set up a VPC. I still need to find out about the available parameters I will need to build the network.
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="mon15jan">Mon 15 Jan '24</a>
### Daily Report
- I practiced CDK deployment using a tutorial.
- Also, my team and I discussed our assumptions and list of services that are important to implement in our infrastructure design. I found this meeting to be very insightful moving forward. 

### Obstacles
- Write some practice CDK code using cdkworkshop.com.

### Solutions
- #### Write some practice CDK code using cdkworkshop.com. Lambda function & API gateway.  
    Instead of the SNS/SQS code that I have in my app now, I’ll add a Lambda function with an API Gateway endpoint in front of it.  

    Users will be able to hit any URL in the endpoint and they’ll receive a heartwarming greeting from our function.  

    - Sources:
        - [Hello, CDK!](https://cdkworkshop.com/30-python/30-hello-cdk.html)

    - Make sure the sample-app is deployed in my AWS cloud. See [Create my first CDK project with AWS CDK Workshop tutorial](#create-my-first-cdk-project-with-aws-cdk-workshop-tutorial) from [Fri 12 Jan '24](#fri12jan).

    - Delete the sample code from my stack. After deletion, my stack looks like this. 
        
        ```py
        from constructs import Construct
        from aws_cdk import (
        Stack
        )


        class CdkWorkshopStack(Stack):

            def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
                super().__init__(scope, construct_id, **kwargs)
        ```
    - Ask toolkit to show us the difference between our CDK app and what's currently deployed.
        
        ```bash
        cdk diff
        ```
        Output:
        
        ```bash
        Stack CdkWorkshopStack
        Creating a change set, this may take a while...
        IAM Statement Changes
        ┌───┬─────────────────────────┬────────┬─────────────────┬───────────────────────────┬─────────────────────────────────────────────────────────┐
        │   │ Resource                │ Effect │ Action          │ Principal                 │ Condition                                               │
        ├───┼─────────────────────────┼────────┼─────────────────┼───────────────────────────┼─────────────────────────────────────────────────────────┤
        │ - │ ${CdkWorkshopQueue.Arn} │ Allow  │ sqs:SendMessage │ Service:sns.amazonaws.com │ "ArnEquals": {                                          │
        │   │                         │        │                 │                           │   "aws:SourceArn": "${CdkWorkshopTopic}"                │
        │   │                         │        │                 │                           │ }                                                       │
        └───┴─────────────────────────┴────────┴─────────────────┴───────────────────────────┴─────────────────────────────────────────────────────────┘
        (NOTE: There may be security-related changes not in this list. See https://github.com/aws/aws-cdk/issues/1299)

        Resources
        [-] AWS::SQS::Queue CdkWorkshopQueue CdkWorkshopQueue50D9D426 destroy
        [-] AWS::SQS::QueuePolicy CdkWorkshopQueue/Policy CdkWorkshopQueuePolicyAF2494A5 destroy
        [-] AWS::SNS::Subscription CdkWorkshopQueue/CdkWorkshopStackCdkWorkshopTopicD7BE9643 CdkWorkshopQueueCdkWorkshopStackCdkWorkshopTopicD7BE96438B5AD106 destroy
        [-] AWS::SNS::Topic CdkWorkshopTopic CdkWorkshopTopicD368A42F destroy


        ✨  Number of stacks with differences: 1
        ```
    - Deploy CDK

        ```bash
        cdk deploy
        ```
    
        Output:

        ```bash
        ✨  Synthesis time: 10.87s

        CdkWorkshopStack:  start: Building e2e301c815e2e96080a1c52841ba3eca59257bb55f200a4c2bcedab40469944b:current_account-current_region
        CdkWorkshopStack:  success: Built e2e301c815e2e96080a1c52841ba3eca59257bb55f200a4c2bcedab40469944b:current_account-current_region
        CdkWorkshopStack:  start: Publishing e2e301c815e2e96080a1c52841ba3eca59257bb55f200a4c2bcedab40469944b:current_account-current_region
        CdkWorkshopStack:  success: Published e2e301c815e2e96080a1c52841ba3eca59257bb55f200a4c2bcedab40469944b:current_account-current_region
        CdkWorkshopStack: deploying... [1/1]
        CdkWorkshopStack: creating CloudFormation changeset...

        ✅  CdkWorkshopStack

        ✨  Deployment time: 79.16s

        Stack ARN:
        arn:aws:cloudformation:eu-central-1:908959576754:stack/CdkWorkshopStack/70149150-b391-11ee-a9b0-0addcb7edc13

        ✨  Total time: 90.03s
        ```
    - Create a directory `lambda` in the root of my project tree (next to the `cdk_workshop`).
    - Add a file called `lambda/hello.py` eith the following contents:

        ```py
        import json

        def handler(event, context):
            print('request: {}'.format(json.dumps(event)))
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'text/plain'
                },
                'body': 'Hello, CDK! You have hit {}\n'.format(event['path'])
            }
        ```
        This is a simple Lambda function which returns the text "Hello, CDK! You've hit [url path]". The function's output also includes HTTP status code and HTTP headers. These are used by API Gateway to formulate the HTTP response to the user.
    - Add an `import` statement at the beginning of `cdk_workshop/cdk_workshop_stack.py`, and a `lambda.Function` to my stack.

        ```py
        from constructs import Construct
        from aws_cdk import (
            Stack,
            aws_lambda as _lambda,
        )


        class CdkWorkshopStack(Stack):

            def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
                super().__init__(scope, construct_id, **kwargs)

                # Defines an AWS Lambda resource
                my_lambda = _lambda.Function(
                    self, 'HelloHandler' ,
                    runtime=_lambda.Runtime.PYTHON_3_12 ,
                    code=_lambda.Code.from_asset('lambda'),
                    handler='hello.handler' ,
                )
        ```
    
    - Save my code, and take a quick look at the diff before I deploy.

        ```bash
        cdk diff
        ```

        Output:

        ```bash
        Stack CdkWorkshopStack
        Creating a change set, this may take a while...
        IAM Statement Changes
        ┌───┬─────────────────────────────────┬────────┬────────────────┬──────────────────────────────┬───────────┐
        │   │ Resource                        │ Effect │ Action         │ Principal                    │ Condition │
        ├───┼─────────────────────────────────┼────────┼────────────────┼──────────────────────────────┼───────────┤
        │ + │ ${HelloHandler/ServiceRole.Arn} │ Allow  │ sts:AssumeRole │ Service:lambda.amazonaws.com │           │
        └───┴─────────────────────────────────┴────────┴────────────────┴──────────────────────────────┴───────────┘
        IAM Policy Changes
        ┌───┬─────────────────────────────┬────────────────────────────────────────────────────────────────────────────────┐
        │   │ Resource                    │ Managed Policy ARN                                                             │
        ├───┼─────────────────────────────┼────────────────────────────────────────────────────────────────────────────────┤
        │ + │ ${HelloHandler/ServiceRole} │ arn:${AWS::Partition}:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole │
        └───┴─────────────────────────────┴────────────────────────────────────────────────────────────────────────────────┘
        (NOTE: There may be security-related changes not in this list. See https://github.com/aws/aws-cdk/issues/1299)

        Resources
        [+] AWS::IAM::Role HelloHandler/ServiceRole HelloHandlerServiceRole11EF7C63 
        [+] AWS::Lambda::Function HelloHandler HelloHandler2E4FBA4D 


        ✨  Number of stacks with differences: 1
        ```

    - Deploy CDK.

        ```bash
        cdk deploy
        ```

        Output:
        
        ```bash
        ✨  Synthesis time: 9.47s

        CdkWorkshopStack:  start: Building 5f83e2a8bc7ca79afcc300d45df613dd32db40aa141b1ab5d88b910f3dbd995e:current_account-current_region
        CdkWorkshopStack:  success: Built 5f83e2a8bc7ca79afcc300d45df613dd32db40aa141b1ab5d88b910f3dbd995e:current_account-current_region
        CdkWorkshopStack:  start: Building 8e681d924af319446955d3bdfb9e36e8da860119419f1055a1e1447a5729f9d6:current_account-current_region
        CdkWorkshopStack:  success: Built 8e681d924af319446955d3bdfb9e36e8da860119419f1055a1e1447a5729f9d6:current_account-current_region
        CdkWorkshopStack:  start: Publishing 5f83e2a8bc7ca79afcc300d45df613dd32db40aa141b1ab5d88b910f3dbd995e:current_account-current_region
        CdkWorkshopStack:  start: Publishing 8e681d924af319446955d3bdfb9e36e8da860119419f1055a1e1447a5729f9d6:current_account-current_region
        CdkWorkshopStack:  success: Published 8e681d924af319446955d3bdfb9e36e8da860119419f1055a1e1447a5729f9d6:current_account-current_region
        CdkWorkshopStack:  success: Published 5f83e2a8bc7ca79afcc300d45df613dd32db40aa141b1ab5d88b910f3dbd995e:current_account-current_region
        This deployment will make potentially sensitive changes according to your current security approval level (--require-approval broadening).
        Please confirm you intend to make the following modifications:

        IAM Statement Changes
        ┌───┬─────────────────────────────────┬────────┬────────────────┬──────────────────────────────┬───────────┐
        │   │ Resource                        │ Effect │ Action         │ Principal                    │ Condition │
        ├───┼─────────────────────────────────┼────────┼────────────────┼──────────────────────────────┼───────────┤
        │ + │ ${HelloHandler/ServiceRole.Arn} │ Allow  │ sts:AssumeRole │ Service:lambda.amazonaws.com │           │
        └───┴─────────────────────────────────┴────────┴────────────────┴──────────────────────────────┴───────────┘
        IAM Policy Changes
        ┌───┬─────────────────────────────┬────────────────────────────────────────────────────────────────────────────────┐
        │   │ Resource                    │ Managed Policy ARN                                                             │
        ├───┼─────────────────────────────┼────────────────────────────────────────────────────────────────────────────────┤
        │ + │ ${HelloHandler/ServiceRole} │ arn:${AWS::Partition}:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole │
        └───┴─────────────────────────────┴────────────────────────────────────────────────────────────────────────────────┘
        (NOTE: There may be security-related changes not in this list. See https://github.com/aws/aws-cdk/issues/1299)

        Do you wish to deploy these changes (y/n)? y
        CdkWorkshopStack: deploying... [1/1]
        CdkWorkshopStack: creating CloudFormation changeset...

        ✅  CdkWorkshopStack

        ✨  Deployment time: 42.98s

        Stack ARN:
        arn:aws:cloudformation:eu-central-1:908959576754:stack/CdkWorkshopStack/70149150-b391-11ee-a9b0-0addcb7edc13

        ✨  Total time: 52.45s
        ```

    - In AWS Console I can see the `CdkWorkshoStack`-resources has status `CREATE_COMPLETE`.

        ![update_complete](/10_Final-Project/includes/15jan24_dl_cdk01.png)
        <br>
        <br>

    - Test my function
        - In the AWS Lambda Console, choose `HelloHandler` function. Configure test event and save.
            
            ![configure test](/10_Final-Project/includes/15jan24_dl_cdk02.png)
            <br>
            <br>
    
        - Click Test again and wait for the execution to complete.

            ![test result](/10_Final-Project/includes/15jan24_dl_cdk03.png)
            <br>
        Status: Succeeded

    - Add a LambdaRestAPI construct to my stack.

        ```py
        from constructs import Construct
        from aws_cdk import (
            Stack,
            aws_lambda as _lambda,
            aws_apigateway as apigw,
        )


        class CdkWorkshopStack(Stack):

            def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
                super().__init__(scope, construct_id, **kwargs)

                # Defines an AWS Lambda resource
                my_lambda = _lambda.Function(
                    self, 'HelloHandler' ,
                    runtime=_lambda.Runtime.PYTHON_3_12 ,
                    code=_lambda.Code.from_asset('lambda'),
                    handler='hello.handler' ,
                )

                apigw.LambdaRestApi(
                    self, 'Endpoint' ,
                    handler=my_lambda,
                )
        ```

    - Save my code, and take a quick look at the diff before I deploy.
    
        ```bash
        cdk diff
        ```

        Output:

        ```bash
        Stack CdkWorkshopStack
        Creating a change set, this may take a while...
        IAM Statement Changes
        ┌───┬─────────────────────┬────────┬───────────────────────┬────────────────────────────────────────────────┬────────────────────────────────────────────────┐
        │   │ Resource            │ Effect │ Action                │ Principal                                      │ Condition                                      │
        ├───┼─────────────────────┼────────┼───────────────────────┼────────────────────────────────────────────────┼────────────────────────────────────────────────┤
        │ + │ ${HelloHandler.Arn} │ Allow  │ lambda:InvokeFunction │ Service:apigateway.amazonaws.com               │ "ArnLike": {                                   │
        │   │                     │        │                       │                                                │   "AWS:SourceArn": "arn:${AWS::Partition}:exec │
        │   │                     │        │                       │                                                │ ute-api:${AWS::Region}:${AWS::AccountId}:${End │
        │   │                     │        │                       │                                                │ pointEEF1FD8F}/${Endpoint/DeploymentStage.prod │
        │   │                     │        │                       │                                                │ }/*/*"                                         │
        │   │                     │        │                       │                                                │ }                                              │
        │ + │ ${HelloHandler.Arn} │ Allow  │ lambda:InvokeFunction │ Service:apigateway.amazonaws.com               │ "ArnLike": {                                   │
        │   │                     │        │                       │                                                │   "AWS:SourceArn": "arn:${AWS::Partition}:exec │
        │   │                     │        │                       │                                                │ ute-api:${AWS::Region}:${AWS::AccountId}:${End │
        │   │                     │        │                       │                                                │ pointEEF1FD8F}/test-invoke-stage/*/*"          │
        │   │                     │        │                       │                                                │ }                                              │
        │ + │ ${HelloHandler.Arn} │ Allow  │ lambda:InvokeFunction │ Service:apigateway.amazonaws.com               │ "ArnLike": {                                   │
        │   │                     │        │                       │                                                │   "AWS:SourceArn": "arn:${AWS::Partition}:exec │
        │   │                     │        │                       │                                                │ ute-api:${AWS::Region}:${AWS::AccountId}:${End │
        │   │                     │        │                       │                                                │ pointEEF1FD8F}/${Endpoint/DeploymentStage.prod │
        │   │                     │        │                       │                                                │ }/*/"                                          │
        │   │                     │        │                       │                                                │ }                                              │
        │ + │ ${HelloHandler.Arn} │ Allow  │ lambda:InvokeFunction │ Service:apigateway.amazonaws.com               │ "ArnLike": {                                   │
        │   │                     │        │                       │                                                │   "AWS:SourceArn": "arn:${AWS::Partition}:exec │
        │   │                     │        │                       │                                                │ ute-api:${AWS::Region}:${AWS::AccountId}:${End │
        │   │                     │        │                       │                                                │ pointEEF1FD8F}/test-invoke-stage/*/"           │
        │   │                     │        │                       │                                                │ }                                              │
        └───┴─────────────────────┴────────┴───────────────────────┴────────────────────────────────────────────────┴────────────────────────────────────────────────┘
        (NOTE: There may be security-related changes not in this list. See https://github.com/aws/aws-cdk/issues/1299)

        Resources
        [+] AWS::ApiGateway::RestApi Endpoint EndpointEEF1FD8F 
        [+] AWS::ApiGateway::Deployment Endpoint/Deployment EndpointDeployment318525DA5f8cdfe532107839d82cbce31f859259 
        [+] AWS::ApiGateway::Stage Endpoint/DeploymentStage.prod EndpointDeploymentStageprodB78BEEA0 
        [+] AWS::ApiGateway::Resource Endpoint/Default/{proxy+} Endpointproxy39E2174E 
        [+] AWS::Lambda::Permission Endpoint/Default/{proxy+}/ANY/ApiPermission.CdkWorkshopStackEndpoint018E8349.ANY..{proxy+} EndpointproxyANYApiPermissionCdkWorkshopStackEndpoint018E8349ANYproxy747DCA52 
        [+] AWS::Lambda::Permission Endpoint/Default/{proxy+}/ANY/ApiPermission.Test.CdkWorkshopStackEndpoint018E8349.ANY..{proxy+} EndpointproxyANYApiPermissionTestCdkWorkshopStackEndpoint018E8349ANYproxy41939001 
        [+] AWS::ApiGateway::Method Endpoint/Default/{proxy+}/ANY EndpointproxyANYC09721C5 
        [+] AWS::Lambda::Permission Endpoint/Default/ANY/ApiPermission.CdkWorkshopStackEndpoint018E8349.ANY.. EndpointANYApiPermissionCdkWorkshopStackEndpoint018E8349ANYE84BEB04 
        [+] AWS::Lambda::Permission Endpoint/Default/ANY/ApiPermission.Test.CdkWorkshopStackEndpoint018E8349.ANY.. EndpointANYApiPermissionTestCdkWorkshopStackEndpoint018E8349ANYB6CC1B64 
        [+] AWS::ApiGateway::Method Endpoint/Default/ANY EndpointANY485C938B 

        Outputs
        [+] Output Endpoint/Endpoint Endpoint8024A810: {"Value":{"Fn::Join":["",["https://",{"Ref":"EndpointEEF1FD8F"},".execute-api.",{"Ref":"AWS::Region"},".",{"Ref":"AWS::URLSuffix"},"/",{"Ref":"EndpointDeploymentStageprodB78BEEA0"},"/"]]}}


        ✨  Number of stacks with differences: 1
        ```

    - Deploy CDK.

        ```bash
        cdk deploy
        ```

        Output:
        
        ```bash
        ✨  Synthesis time: 11.55s

        CdkWorkshopStack:  start: Building 1db71cd140606ea1a187b8db5a974ea8818f2957daaec5188b866c73f0322b45:current_account-current_region
        CdkWorkshopStack:  success: Built 1db71cd140606ea1a187b8db5a974ea8818f2957daaec5188b866c73f0322b45:current_account-current_region
        CdkWorkshopStack:  start: Publishing 1db71cd140606ea1a187b8db5a974ea8818f2957daaec5188b866c73f0322b45:current_account-current_region
        CdkWorkshopStack:  success: Published 1db71cd140606ea1a187b8db5a974ea8818f2957daaec5188b866c73f0322b45:current_account-current_region
        This deployment will make potentially sensitive changes according to your current security approval level (--require-approval broadening).
        Please confirm you intend to make the following modifications:

        IAM Statement Changes
        ┌───┬─────────────────────┬────────┬───────────────────────┬────────────────────────────────────────────────┬────────────────────────────────────────────────┐
        │   │ Resource            │ Effect │ Action                │ Principal                                      │ Condition                                      │
        ├───┼─────────────────────┼────────┼───────────────────────┼────────────────────────────────────────────────┼────────────────────────────────────────────────┤
        │ + │ ${HelloHandler.Arn} │ Allow  │ lambda:InvokeFunction │ Service:apigateway.amazonaws.com               │ "ArnLike": {                                   │
        │   │                     │        │                       │                                                │   "AWS:SourceArn": "arn:${AWS::Partition}:exec │
        │   │                     │        │                       │                                                │ ute-api:${AWS::Region}:${AWS::AccountId}:${End │
        │   │                     │        │                       │                                                │ pointEEF1FD8F}/${Endpoint/DeploymentStage.prod │
        │   │                     │        │                       │                                                │ }/*/*"                                         │
        │   │                     │        │                       │                                                │ }                                              │
        │ + │ ${HelloHandler.Arn} │ Allow  │ lambda:InvokeFunction │ Service:apigateway.amazonaws.com               │ "ArnLike": {                                   │
        │   │                     │        │                       │                                                │   "AWS:SourceArn": "arn:${AWS::Partition}:exec │
        │   │                     │        │                       │                                                │ ute-api:${AWS::Region}:${AWS::AccountId}:${End │
        │   │                     │        │                       │                                                │ pointEEF1FD8F}/test-invoke-stage/*/*"          │
        │   │                     │        │                       │                                                │ }                                              │
        │ + │ ${HelloHandler.Arn} │ Allow  │ lambda:InvokeFunction │ Service:apigateway.amazonaws.com               │ "ArnLike": {                                   │
        │   │                     │        │                       │                                                │   "AWS:SourceArn": "arn:${AWS::Partition}:exec │
        │   │                     │        │                       │                                                │ ute-api:${AWS::Region}:${AWS::AccountId}:${End │
        │   │                     │        │                       │                                                │ pointEEF1FD8F}/${Endpoint/DeploymentStage.prod │
        │   │                     │        │                       │                                                │ }/*/"                                          │
        │   │                     │        │                       │                                                │ }                                              │
        │ + │ ${HelloHandler.Arn} │ Allow  │ lambda:InvokeFunction │ Service:apigateway.amazonaws.com               │ "ArnLike": {                                   │
        │   │                     │        │                       │                                                │   "AWS:SourceArn": "arn:${AWS::Partition}:exec │
        │   │                     │        │                       │                                                │ ute-api:${AWS::Region}:${AWS::AccountId}:${End │
        │   │                     │        │                       │                                                │ pointEEF1FD8F}/test-invoke-stage/*/"           │
        │   │                     │        │                       │                                                │ }                                              │
        └───┴─────────────────────┴────────┴───────────────────────┴────────────────────────────────────────────────┴────────────────────────────────────────────────┘
        (NOTE: There may be security-related changes not in this list. See https://github.com/aws/aws-cdk/issues/1299)

        Do you wish to deploy these changes (y/n)? y
        CdkWorkshopStack: deploying... [1/1]
        CdkWorkshopStack: creating CloudFormation changeset...

        ✅  CdkWorkshopStack

        ✨  Deployment time: 38.34s

        Outputs:
        CdkWorkshopStack.Endpoint8024A810 = https://b6uougqw64.execute-api.eu-central-1.amazonaws.com/prod/
        Stack ARN:
        arn:aws:cloudformation:eu-central-1:908959576754:stack/CdkWorkshopStack/70149150-b391-11ee-a9b0-0addcb7edc13

        ✨  Total time: 49.89s
        ```

    - Testing my app
        - Copy the URL and execute.

        ![](/10_Final-Project/includes/15jan24_dl_cdk04.png)
        <br>

        - My app works.
    - Because this is for learning purposes, I will be destroying the deployed CDK app.

        ```bash
        cdk destroy
        ```

### Learnings
- I got to experience a bit more how the process of CDK deployment works. A tiny bit more familiar with the CDK environment. The codes are still gibberish and intimidating to me.
- Discussing our assumptions as a team was really insightful and informational moving forward.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="sun14jan">Sun 14 Jan '24</a>
### Daily Report
- I completed: 

    | Epic | User Story | Description | Deliverable |
    | - | - | - | - |
    | Exploration | 2: As a team, we want a clear overview of the assumptions we have made. | You have already received a lot of information. There may be questions that none of the stakeholders have been able to answer. Your team should be able to produce an overview of the assumptions you are making as a result. | A point-by-point overview of all assumptions. |    
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="sat13jan">Sat 13 Jan '24</a>
### Daily Report
- I finished setting up my Jira SCRUM board for this project.
- Also I started structuring the project folder so it is more organized and easier to explore the process of my project.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="fri12jan">Fri 12 Jan '24</a>
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

    - The first time I deploy an AWS CDK app into my environment (account/region), I’ll need to install a “bootstrap stack”.

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
    
    - Use `cdk deploy` to deploy the CDK app to my default AWS account/region.

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
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="thu11jan">Thu 11 Jan '24</a>
### Daily Report
- I completed:
    
    | Epic | User Story | Description | Deliverable |
    | - | - | - | - |
    | Exploration | 1: As a team, we want to be clear about the requirements of the application. | You have already received a lot of information. Some requirements are already mentioned in this document, but this list may be incomplete or unclear. It is important to sort out all the uncertainties before you start doing major work. | A point-by-point description of all requirements. |
    | Exploration | 3: As a team, we want to have a clear overview of the Cloud Infrastructure that the application needs. | You have already received a lot of information. And already a design. Only aspects such as IAM/AD are still missing from the design. Identify these additional services you will need and make an overview of all services. | An overview of all services that will be used. |  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="wed10jan">Wed 10 Jan '24</a>
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
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="tue09jan">Tue 09 Jan '24</a>
### Daily Report
- I made a list of questions for our meeting with the product owner tomorrow at 9:15. I also created a clear and structured document where the requirements and questions were categorized.

### Obstacles
- Missing a clear and structured overview of the already known requirements in combination with the questions towards the other not yet known requirements. 

### Solutions
- #### Created a clear and structured [document](https://docs.google.com/drawings/d/1Emfy-G-C1uBrazpZSeBZxsg9z3ydj0bhI2TDCuuZbHs/edit?usp=sharing) for the infrastructure requirements and questions.

### Learnings
- It helps and it is more efficient to create a clear overview for myself and my team of all that we need to go into a meeting prepared.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="mon08jan">Mon 08 Jan '24</a>
### Daily Report
- First day of the project. I read and tried to understand what the project is about and what is expected from me.

- We will be using Jira to track our progress throughout the project. I read and watched a video on what Jira is about. Also made an account.

### Obstacles
- No idea what Jira is about.

### Solutions
- #### Watched an introduction [video](https://www.youtube.com/watch?v=GWxMTvRGIpc) about Jira.

### Learnings
- I have a better understanding why Jira is a handy tool to use during projects.  
<br>

*back to [top](#top)*  
<br>

++++++++++++++++++++
## Log template
Template for easy daily logging  

## ✏️ 📄 <a id="indert-date-here">insert-date-here</a>
### Daily Report
- ...

### Obstacles
- ...

### Solutions
- ...

### Learnings
- ...  
<br>

*back to [top](#top)*  
<br>
++++++++++++++++++++