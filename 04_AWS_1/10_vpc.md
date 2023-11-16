# VPC
With Amazon Virtual Private Cloud (Amazon VPC), you can launch AWS resources in a logically isolated virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

## Key-terms

## Assignment

<ins>Exercise 1:</ins>
- Allocate an Elastic IP address to your account.
- Create a new VPC with the following requirements:
    - Region: Frankfurt (eu-central-1)
    - VPC with a public and a private subnet
    - Name: Lab VPC
    - CIDR: 10.0.0.0/16
- Requirements for the public subnet:
    - Name: Public subnet 1
    - CIDR: 10.0.0.0/24
    - AZ: eu-central-1a
- Requirements for the private subnet:
    - Name: Private subnet 1
    - CIDR: 10.0.1.0/24
    - AZ: eu-central-1a
- Your network should now look like this:

![infrastructure](/04_AWS_1/images/10_vpc.png)<br><br>

<ins>Exercise 2:</ins>
- Create an additional public subnet with the following requirements:
    - VPC: Lab VPC
    - Name: Public Subnet 2
    - AZ: eu-central-1b
    - CIDR: 10.0.2.0/24
- Create an additional private subnet with the following requirements:
    - VPC: Lab VPC
    - Name: Private Subnet 2
    - AZ: eu-central-1b
    - CIDR: 10.0.3.0/24
- View the main route table for Lab VPC. It should have an entry for the NAT gateway. Rename this route table to Private Route Table.
- Explicitly associate the private route table with your two private subnets.
- View the other route table for Lab VPC. It should have an entry for the internet gateway. Rename this route table to Public Route Table.
- Explicitly associate the public route table to your two public subnets.

<ins>Exercise 3:</ins>
- Create a Security Group with the following requirements:
    - Name: Web SG
    - Description: Enable HTTP Access
    - VPC: Lab VPC
    - Inbound rule: allow HTTP access from anywhere
    - Outbound rule: Allow all traffic

<ins>Exercise 4:</ins>
- Launch an EC2 instance with the following requirements:
    - AMI: Amazon Linux 2
    - Type: t3.micro
    - Subnet: Public subnet 2
    - Auto-assign Public IP: Enable
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
    - Tag:
        - Key: Name
        - Value: Web server
    - Security Group: Web SG
    - Key pair: no key pair
- Connect to your server using the public IPv4 DNS name.

### Used sources
- [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [Associate Elastic IP addresses with resources in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html)
- [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html)
- [Create a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/create-subnets.html)

### Encountered problems
None

### Result

**<ins>Exercise 1:</ins>**

**- Allocate an Elastic IP address to your account.**

To use an Elastic IP address, you first allocate it for use in your account. Then, you can associate it with an instance or network interface in your VPC. Your Elastic IP address remains allocated to your AWS account until you explicitly release it.

![allocate elastic ip address](/04_AWS_1/images/10_vpc1-1-1.png)<br>

![allocate elastic ip address](/04_AWS_1/images/10_vpc1-1-2.png)<br><br>

**- Create a new VPC.**

![create vpc](/04_AWS_1/images/10_vpc1-2-1.png)<br>

![infrastructure](/04_AWS_1/images/10_vpc.png)<br><br>

**<ins>Exercise 2:</ins>**

**- Create an additional public subnet.**

![create additional public subnet](/04_AWS_1/images/10_vpc2-1-1.png)<br><br>

**- Create an additional private subnet.**

![create additional private subnet](/04_AWS_1/images/10_vpc2-2-1.png)<br><br>

**- View the main route table for Lab VPC. It should have an entry for the NAT gateway. Rename this route table to Private Route Table.**

![rename private route table](/04_AWS_1/images/10_vpc2-3-1.png)<br><br>

**- Explicitly associate the private route table with your two private subnets.**

![associate private route table with the private subnets](/04_AWS_1/images/10_vpc2-4-1.png)<br>

![associate private route table with the private subnets](/04_AWS_1/images/10_vpc2-4-2.png)<br><br>

**- View the other route table for Lab VPC. It should have an entry for the internet gateway. Rename this route table to Public Route Table.**

![rename public route table](/04_AWS_1/images/10_vpc2-5-1.png)<br><br>

**- Explicitly associate the public route table to your two public subnets.**

![associate public route table with the public subnets](/04_AWS_1/images/10_vpc2-6-1.png)<br>

![associate public route table with the public subnets](/04_AWS_1/images/10_vpc2-6-2.png)<br><br>

**<ins>Exercise 3:</ins>**

**- Create a Security Group**

![create security group](/04_AWS_1/images/10_vpc3-1-1.png)<br><br>

**<ins>Exercise 4:</ins>**

**- Launch an EC2 instance**

![launch instance](/04_AWS_1/images/10_vpc4-1-1.png)<br>
![launch instance](/04_AWS_1/images/10_vpc4-1-2.png)<br>
![launch instance](/04_AWS_1/images/10_vpc4-1-3.png)<br>
![launch instance](/04_AWS_1/images/10_vpc4-1-4.png)<br><br>

**- Connect to your server using the public IPv4 DNS name.**

![connect to server](/04_AWS_1/images/10_vpc4-2-1.png)<br><br>

The following infrastructure is what I just built in this assignment.

![infrastructure](/04_AWS_1/images/10_vpc4-2-2.png)<br><br>