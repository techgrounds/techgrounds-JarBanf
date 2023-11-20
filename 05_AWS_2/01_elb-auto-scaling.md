# ELB & Auto Scaling
[Geef een korte beschrijving van het onderwerp]

## Key-terms

## Assignment

<ins>Exercise 1</ins>

- Launch an EC2 instance with the following requirements:
    - Region: Frankfurt (eu-central-1)
    - AMI: Amazon Linux 2
    - Type: t3.micro
    - User data:

    ```bash
    #!/bin/bash
    # Install Apache Web Server and PHP
    yum install -y httpd mysql php unzip
    # Download Lab files
    wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
    unzip lab-app.zip -d /var/www/html/
    # Turn on web server
    chkconfig httpd on
    service httpd start
    ```
    - Security Group: Allow HTTP
- Wait for the status checks to pass.
- Create an AMI from your instance with the following requirements:
    - Image name: Web server AMI

<ins>Exercise 2</ins>

- Create an application load balancer with the following requirements:
    - Name: LabELB
    - Listener: HTTP on port 80
    - AZs: eu-central-1a and eu-central-1b
    - Subnets: must be public
    - Security Group:
        - Name: ELB SG
        - Rules: allow HTTP access
    - Target Group:
        - Name: LabTargetGroup
        - Targets: to be registered by Auto Scaling

<ins>Exercise 3</ins>

- Create a launch configuration for the Auto Scaling group. It has to be identical to the server that is currently running.
- Create an auto scaling group with the following requirements:
    - Name: Lab ASG
    - Launch Configuration: Web server launch configuration
    - Subnets: must be in eu-central-1a and eu-central-1b
    - Load Balancer: LabELB
    - Group metrics collection in CloudWatch must be enabled
    - Group Size:
        - Desired Capacity: 2
        - Minimum Capacity: 2
        - Maximum Capacity: 4
    - Scaling policy: Target tracking with a target of 60% average CPU utilisation

<ins>Exercise 4</ins>

- Verify that the EC2 instances are online and that they are part of the target group for the load balancer.
- Access the server via the ELB by using the DNS name of the ELB.
- Perform a load test on your server(s) using the website on your server to activate auto scaling. There might be a delay on the creation of new servers in your fleet, depending on the settings on your Auto Scaling Group.

### Used sources
- [Create an Amazon EBS-backed Linux AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html)
- [Getting started with Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancer-getting-started.html)

### Encountered problems
None

### Result

**<ins>Exercise 1</ins>**

**- Launch an EC2 instance and wait for the status checks to pass.**

![launch ec2 instance](/05_AWS_2/includes/01_elb-auto-scaling1-1-1.png)<br>

![launch ec2 instance](/05_AWS_2/includes/01_elb-auto-scaling1-1-2.png)<br><br>

**- Create an AMI from your instance**

![create ami](/05_AWS_2/includes/01_elb-auto-scaling1-3-1.png)<br><br>

**<ins>Exercise 2</ins>**

**- Create an application load balancer**

- Step 1: Create a target group.

![create target group](/05_AWS_2/includes/01_elb-auto-scaling2-1-1.png)<br>

![create target group](/05_AWS_2/includes/01_elb-auto-scaling2-1-2.png)<br><br>

- Step 2: Create security group.

![create security group](/05_AWS_2/includes/01_elb-auto-scaling2-2-1.png)<br><br>