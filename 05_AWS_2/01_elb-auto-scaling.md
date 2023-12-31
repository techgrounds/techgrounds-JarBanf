# ELB & Auto Scaling

<ins>ELB</ins>  

Elastic Load Balancing automatically distributes your incoming traffic across multiple targets,such as EC2 instances, containers, and IP addresses, in one or more Availability Zones. It monitors the health of its registerd targets, and routes traffic only to the healthy targets. ELB scales your load balancer capacity automatically in response to changes in incoming traffic.
ELB supports the following load balancers:
- Application Load Balancers 
- Network Load Balancers
- Gateway Load Balancers
- Classic Load Balancers

![elb](/05_AWS_2/includes/01_elb-auto-scaling0-1.png)<br><br>

<ins>Auto Scaling</ins>

EC2 Auto Scaling helps you ensure that you have the correct number of EC2 instances available to handle the load for your application. You create collections collections of EC2 instances, called Auto Scaling Groupes.  
You can specify the minimum number of instances in each Auto Scaling Group, and EC2 Auto Scaling ensures that your group never goes below this size.  
Also you can specify the maximum number of instances in each Auto Scaling group, and and EC2 Auto Scaling ensures that your group never goes above this size.  
If you specify the desired capacity, either when you create the group or at any time thereafter, EC2 Auto Scaling ensures that your group has this many instances.  
If you specify scaling policies, then EC2 Auto Scaling can launch or terminate instances as demand on your applications increases or decreases.

![ec2 auto scaling](/05_AWS_2/includes/01_elb-auto-scaling0-2.png)<br>

![ec2 auto scaling](/05_AWS_2/includes/01_elb-auto-scaling0-3.png)<br><br>


<ins>AMI</ins>

An Amazon Machine Image (AMI) is a supported and maintained image provided by AWS that provides the information required to launch an instance. You must specify an AMI when you launch an instance. You can launch multiple instances from a single AMI when you require multiple instances with the same configuration.  

![ec2 auto scaling](/05_AWS_2/includes/01_elb-auto-scaling0-4.png)<br><br>

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
- [What is Elastic Load Balancing?](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
- [What is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
- [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
- [Create an Amazon EBS-backed Linux AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html)
- [Getting started with Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancer-getting-started.html)
- [Create a launch template for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html)
- [Create an Auto Scaling group using a launch template](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template.html)

### Encountered problems
None

### Result

**<ins>Exercise 1</ins>**

**- Launch an EC2 instance and wait for the status checks to pass.**

![launch ec2 instance](/05_AWS_2/includes/01_elb-auto-scaling1-1-1.png)<br>

![launch ec2 instance](/05_AWS_2/includes/01_elb-auto-scaling1-1-2.png)<br><br>

**- Create an AMI from your instance.**

![create ami](/05_AWS_2/includes/01_elb-auto-scaling1-3-1.png)<br><br>

**<ins>Exercise 2</ins>**

**- Create an application load balancer.**

- Step 1: Create a target group.

![create target group](/05_AWS_2/includes/01_elb-auto-scaling2-1-1.png)<br>

![create target group](/05_AWS_2/includes/01_elb-auto-scaling2-1-2.png)<br><br>

- Step 2: Create security group.

![create security group](/05_AWS_2/includes/01_elb-auto-scaling2-2-1.png)<br><br>

- Step 3: Create load balancer.

![create load balancer](/05_AWS_2/includes/01_elb-auto-scaling2-3-1.png)<br>

![create load balancer](/05_AWS_2/includes/01_elb-auto-scaling2-3-2.png)<br><br>

- Step 4: Test load balancer.

![test load balancer](/05_AWS_2/includes/01_elb-auto-scaling2-4-1.png)<br><br>

**<ins>Exercise 3</ins>**

**- Create a launch configuration for the Auto Scaling group. It has to be identical to the server that is currently running.  
<ins>EDIT: launch configuration is not supported anymore, I have to choose Launch Template.</ins>**

![create launch template](/05_AWS_2/includes/01_elb-auto-scaling3-1-1.png)<br>

![create launch template](/05_AWS_2/includes/01_elb-auto-scaling3-1-2.png)<br><br>

**- Create an auto scaling group.**

![create auto scaling group](/05_AWS_2/includes/01_elb-auto-scaling3-2-1.png)<br>

![create auto scaling group](/05_AWS_2/includes/01_elb-auto-scaling3-2-2.png)<br>

![create auto scaling group](/05_AWS_2/includes/01_elb-auto-scaling3-2-3.png)<br><br>

**<ins>Exercise 4</ins>**

**- Verify that the EC2 instances are online and that they are part of the target group for the load balancer.**

![verify 2 running ec2 instances](/05_AWS_2/includes/01_elb-auto-scaling4-1-1.png)<br>

![verify 2 running ec2 instances](/05_AWS_2/includes/01_elb-auto-scaling4-1-2.png)<br>

![verify 2 running ec2 instances](/05_AWS_2/includes/01_elb-auto-scaling4-1-3.png)<br><br>

**- Access the server via the ELB by using the DNS name of the ELB.**

![access server via elb](/05_AWS_2/includes/01_elb-auto-scaling4-2-1.png)<br>

![access server via elb](/05_AWS_2/includes/01_elb-auto-scaling4-2-2.png)<br><br>

**- Perform a load test on your server(s) using the website on your server to activate auto scaling. There might be a delay on the creation of new servers in your fleet, depending on the settings on your Auto Scaling Group.**

![perform load test](/05_AWS_2/includes/01_elb-auto-scaling4-3-1.png)<br>

![perform load test](/05_AWS_2/includes/01_elb-auto-scaling4-3-2.png)<br>

![perform load test](/05_AWS_2/includes/01_elb-auto-scaling4-3-3.png)<br><br>