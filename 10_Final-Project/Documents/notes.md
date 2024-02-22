### <ins>NOT optimized to be actively viewed as a .md file</ins>
# Notes
My digital scribbles.

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


## User data v1.0

#!/bin/bash
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
sudo su
echo '<h1>Hello From Jared's CDK created Web Server!</h1>' > /var/www/html/index.html

## User data v1.1

#!/bin/bash
# perform a quick software update on instance
sudo dnf update -y
# install the latest versions of Apache web server and PHP packages for AL2023
sudo dnf install -y httpd wget php-fpm php-mysqli php-json php php-devel
# download lab files for load testing
wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
# unzip files to html directory
sudo unzip lab-app.zip -d /var/www/html/
# start the Apache web server
sudo systemctl start httpd
# configure the Apache web server to start at each system boot
sudo systemctl enable httpd

# Download MySQL Yum repository
wget https://dev.mysql.com/get/mysql80-community-release-el9-3.noarch.rpm
# Install MySQL Yum repository
sudo dnf install mysql80-community-release-el9-3.noarch.rpm -y
# Update Al2023 Packages
sudo dnf update -y
# Install MySQL 8 on Amazon Linux 2023
sudo dnf install mysql-community-server -y
# Start the service of MySQL
sudo systemctl start mysqld
# Enable it to activate automatically with the system boot or crash
sudo systemctl enable mysqld


## Command to connect to RDS MySQL Database

# mysql -h <RDS_ENDPOINT> -u <USERNAME> -p
mysql -h cdkvpcteststack-databasewebserver14fd81e3-sofmriuerbnw.coxnyfceatsl.eu-central-1.rds.amazonaws.com -u admin -p