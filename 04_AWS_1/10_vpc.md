# VPC
[Geef een korte beschrijving van het onderwerp]

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

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

![shared responsibility model](/04_AWS_1/images/10_vpc.png)<br><br>

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
[Plaats hier de bronnen die je hebt gebruikt.]

### Encountered problems
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Result
[Omschrijf hoe je weet dat je opdracht gelukt is (gebruik screenshots waar nodig).]