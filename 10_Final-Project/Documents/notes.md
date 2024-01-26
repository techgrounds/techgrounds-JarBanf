
## VPC console choices
- vpc only
    - name tag: optional
    - IPv4 CIDR: between /16 and /28
    - IPv6 needed? default: no
    - Tenancy: Default
- VPC and more
    - name tag (auto-generation default): auto genereation OR manually assign name to VPC, Subnets, Route tables, Network connections (IGW, NATGW, VPC enpoint)
    - IPv4 CIDR: between /16 and /28
    - IPv6 needed? default: no
    - Tenancy: Default
    - Number of AZ: 1, 2 or 3
        - Also choose which AZ I want
    - Number of public subnets per AZ: 0 or 1
    - Number of private subnets per AZ: 0, 1 or 2
    - Customize subnets CIDR blocks.
    - NAT gateway: None, In 1 AZ, 1 per AZ
    - VPC endpoints: None or S3 GW
    - DNS options
        - Enable DNS hostnames: default = on
        - Enable DNS resolution: default = on

## Instance
- Name
- AMI
- Instance Type
- Key Pair name
- Network Settings
    - VPC
    - Subnet
    - Auto-assign public IP
    - Firewall (security group)
- Configure Storage
    - Root volume
    - EBS volume


## User data

#!/bin/bash
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
sudo su
echo '<h1>Hello From Jared's CDK created Web Server!</h1>' > /var/www/html/index.html