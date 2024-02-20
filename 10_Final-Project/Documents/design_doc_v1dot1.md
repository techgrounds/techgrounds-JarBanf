# <a id="top">Design Document v1.1</a> 📘 👷 🔨
**UNDER CONSTRUCTION**  
This document contains technical and practical information about my application.  
Diagrams, (N)SG rules, deployment visualization, and more, are listed here.

## Table of Contents
- [Architecture Design](#architecture-design)
- [Estimated Monthly Costs](#estimated-monthly-costs)
- [Configurations](#configurations)
    - [VPC-1 Web](#vpc-1-web)
    - [VPC-2 Admin](#vpc-2-admin)
    - [VPC Peering](#vpc-peering)
    - [Security Groups](#security-groups)
        - [SG Admin Webserver](#sg-admin-webserver)
        - [SG Adminserver](#sg-adminserver)
        - [SG AS Webservers (Auto Scaling)](#sg-as-webservers-auto-scaling)
        - [SG Application Load Balancer](#sg-application-load-balancer)
        - [SG Database](#sg-database)
    - [NACLs](#nacls)
        - [VPC-1 Web Public Subnets]()
        - [VPC-1 Web Private Subnets]()
        - [VPC-2 Admin Public Subnet]()
    - [Webserver (for admin)](#webserver-for-admin)
    - [Admin Server](#admin-server)
    - [Auto Scaling](#auto-scaling)
    - [Application Load Balancer](#application-load-balancer)
    - [RDS MySQL Database](#rds-mysql-database)
    - [Backup](#backup)
    - [S3 Buckets](#s3-buckets)
        - [Bucket Webfiles](#bucket-webfiles)
        - [Bucket Scripts](#bucket-scripts)
    - [User Data Webserver](#user-data-webserver)
<br>

*back to [top](#top)*  
<br>

## Architecture Design
![architecture design v1.1](/10_Final-Project/MVP_v1dot1/includes/diagram_v1dot1.drawio.png)  
*Architecture design*
<br>

*back to [top](#top)*  
<br>

## Estimated Monthly Costs
<br>

*back to [top](#top)*  
<br>

## Configurations
### VPC-1 Web
![VPC-1 Web Resource Map](/10_Final-Project/includes/v1dot1-vpc1-web-resource-map.drawio.png)  
*VPC-1 Web Resource Map*

<br>

*back to [top](#top)*  
<br>

### VPC-2 Admin
![VPC-2 Admin Resource Map](/10_Final-Project/includes/v1dot1-vpc2-admin-resource-map.drawio.png)  
*VPC-2 Admin Resource Map*
<br>

*back to [top](#top)*  
<br>

### VPC Peering
![VPC Peering](/10_Final-Project/includes/v1dot1-vpc-peering.drawio.png)  
*VPC Peering*
<br>

*back to [top](#top)*  
<br>

### Security Groups
#### SG Admin Webserver 
| Type | Port | Source / Destination | Description |
| - | - | - | - |
| **Inbound** |  |  |  |
| HTTP | 80 | 10.0.2.4/32 | Allow HTTP traffic from admin server |
| HTTPS | 443 | 10.0.2.4/32 | Allow HTTPS traffic from admin server |
| SSH | 22 | 10.0.2.4/32 | Allow SSH traffic from admin server |
|  |  |  |  |
| **Outbound** |  |  |  |
| All Traffic | All | 0.0.0.0/0 | Allow all outbound traffic by default |
<br>

#### SG Adminserver
| Type | Port | Source / Destination | Description |
| - | - | - | - |
| **Inbound** |  |  |  |
| RDP | 3389 | Admin home/office IP | Allow RDP from Admin home/office IP |
|  |  |  |  |
| **Outbound** |  |  |  |
| All Traffic | All | 0.0.0.0/0 | Allow all outbound traffic by default |
<br>

#### SG AS Webservers (Auto Scaling)
| Type | Port | Source / Destination | Description |
| - | - | - | - |
| **Inbound** |  |  |  |
| HTTPS | 443 | Load Balancer | Load balancer to target |
|  |  |  |  |
| **Outbound** |  |  |  |
| All Traffic | All | 0.0.0.0/0 | Allow all outbound traffic by default |
<br>

#### SG Application Load Balancer
| Type | Port | Source / Destination | Description |
| - | - | - | - |
| **Inbound** |  |  |  |
| HTTP | 80 | 0.0.0.0/0 | Allow from anyone on port 80 |
| HTTPS | 443 | 0.0.0.0/0 | Allow from anyone on port 443 |
|  |  |  |  |
| **Outbound** |  |  |  |
| HTTPS | 443 | Auto Scaling Group | Load balancer to target |
<br>

#### SG Database
| Type | Port | Source / Destination | Description |
| - | - | - | - |
| **Inbound** |  |  |  |
| MYSQL/Aurora | 3306 | 10.0.1.0/24 | Allow MySQL from VPC-1 Web |
|  |  |  |  |
| **Outbound** |  |  |  |
| All Traffic | All | 0.0.0.0/0 | Allow all outbound traffic by default |
<br>

*back to [top](#top)*  
<br>

### NACLs
#### VPC-1 Web Public Subnets
| Rule number | Type | Protocol | Port Range | Source / Destination | Allow / Deny |
| - | - | - | - | - | - |
| **Inbound** |  |  |  |  |  |
| 100 | HTTP (80) | TCP (6) | 80 | 0.0.0.0/0 | Allow |
| 110 | HTTPS (443) | TCP (6) | 443 | 0.0.0.0/0 | Allow |
| 120 | Custom TCP | TCP (6) | 1024 - 65535 | 10.0.1.0/24 | Allow |
| * | All traffic | All | All | 0.0.0.0/0 | Deny |
|  |  |  |  |  |  |
| **Outbound** |  |  |  |  |  |
| 110 | HTTPS (443) | TCP (6) | 443 | 10.0.1.0/24 | Allow |
| 120 | Custom TCP | TCP (6) | 1024 - 65535 | 0.0.0.0/0 | Allow |
| * | All traffic | All | All | 0.0.0.0/0 | Deny |
<br>

#### VPC-1 Web Private Subnets
| Rule number | Type | Protocol | Port Range | Source / Destination | Allow / Deny |
| - | - | - | - | - | - |
| **Inbound** |  |  |  |  |  |
| 100 | SSH (22) | TCP (6) | 22 | 10.0.2.4/32 | Allow |
| 105 | HTTP (80) | TCP (6) | 80 | 10.0.0.0/16 | Allow |
| 110 | HTTPS (443) | TCP (6) | 443 | 10.0.0.0/16 | Allow |
| 115 | MySQL/Aurora (3306) | TCP (6) | 3306 | 10.0.1.0/24 | Allow |
| 120 | Custom TCP | TCP (6) | 1024 - 65535 | 0.0.0.0/0 | Allow |
| * | All traffic | All | All | 0.0.0.0/0 | Deny |
|  |  |  |  |  |  |
| **Outbound** |  |  |  |  |  |
| 100 | HTTP (80) | TCP (6) | 80 | 0.0.0.0/0 | Allow |
| 110 | HTTPS (443) | TCP (6) | 443 | 0.0.0.0/0 | Allow |
| 120 | Custom TCP | TCP (6) | 1024 - 65535 | 0.0.0.0/0 | Allow |
| * | All traffic | All | All | 0.0.0.0/0 | Deny |
<br>

#### VPC-2 Admin Public Subnet
| Rule number | Type | Protocol | Port Range | Source / Destination | Allow / Deny |
| - | - | - | - | - | - |
| **Inbound** |  |  |  |  |  |
| 90 | Custom TCP | TCP (6) | 49152 - 65535 | 0.0.0.0/0 | Allow |
| 100 | RDP (3389) | TCP (6) | 3389 | Admin home/office IP | Allow |
| * | All traffic | All | All | 0.0.0.0/0 | Deny |
|  |  |  |  |  |  |
| **Outbound** |  |  |  |  |  |
| 90 | SSH (22) | TCP (6) | 22 | 10.0.1.52/32 | Allow |
| 100 | HTTP (80) | TCP (6) | 80 | 0.0.0.0/0 | Allow |
| 110 | HTTPS (443) | TCP (6) | 443 | 0.0.0.0/0 | Allow |
| 120 | Custom TCP | TCP (6) | 1024 - 65535 | 0.0.0.0/0 | Allow |
| * | All traffic | All | All | 0.0.0.0/0 | Deny |
<br>

*back to [top](#top)*  
<br>

### Webserver (for admin)
| - | - |
| - | - |
| **Command to SSH to Webserver** | `ssh -i "kp-admin-webserver.pem" ec2-user@10.0.1.52` |
| **Key Pair name** | "kp-admin-webserver" |
| **Private Key**| Stored in Parameter Store |
| **VPC** | [VPC-1 Web](#vpc-1-web) |
| **Availability Zone** | eu-central-1a |
| **Subnet** | Private Subnet 1 |
| **Private IP** | 10.0.1.52 |
| **Security Group** | [SG Admin Webserver](#sg-admin-webserver) |
| **Instance Type** | t2 micro |
| **AMI** | Amazon Linux 2023 |
| **Root Storage** | 8 GB |
| **Encryption** | Enabled |
| **Webfiles** | [S3 Bucket Webfiles](#bucket-webfiles) |
| **Installed Packages** | Apache web server, PHP packages, MySQL 8 |
| **User Data** | [User Data Webserver](#user-data-webserver) |
<br>

*back to [top](#top)*  
<br>

### Admin Server
| - | - |
| - | - |
| **VPC** | [VPC-2 Admin](#vpc-2-admin) |
| **Availability Zone** | eu-central-1b |
| **Subnet** | Public Subnet 1 |
| **Public IP** | Visible in console |
| **Private IP** | 10.0.2.4 |
| **Key Pair name** | "kp-adminserver" |
| **Private Key**| Stored in Parameter Store |
| **Security Group** | [SG Adminserver](#sg-adminserver) |
| **Instance Type** | t3 large |
| **AMI** | Microsoft Windows Server 2022 Full Locale English |
| **Root Storage** | 30 GB |
| **Attached Storage** | 256 GB |
| **Encryption** | Enabled (Root & Attached Storage) |
<br>

*back to [top](#top)*  
<br>

### Auto Scaling
#### WS Launch Template
| - | - |
| - | - |
| **Launch Template name** | "ws-launch-template" |
| **Security Group** | [SG AS Webservers (Auto Scaling)](#sg-as-webservers-auto-scaling) |
| **Instance Type** | t2 micro |
| **AMI** | Amazon Linux 2023 |
| **Root Storage** | 8 GB |
| **Encryption** | Enabled |
| **Webfiles** | [S3 Bucket Webfiles](#bucket-webfiles) |
| **Installed Packages** | Apache web server, PHP packages, MySQL 8 |
| **User Data** | [User Data Webserver](#user-data-webserver) |
<br>

#### Auto Scaling Group
| - | - |
| - | - |
| **Launch Template** | [WS Launch Template](#ws-launch-template) |
| **VPC** | [VPC-1 Web](#vpc-1-web) |
| **Availability Zone** | eu-central-1a, eu-central-1b, eu-central-1c |
| **Subnet** | All public subnets |
| **Desired capacity** | 1 |
| **Minimum capacity** | 1 |
| **Maximum capacity** | 3 |
| **Health check type** | EC2, ELB (if instance fail an ELB health check, the ELB automatically terminates the unhealthy instance and starts up a new instance) |
| **Health check grace period** | 5 minutes. This amount of time after starting up a new instance, it starts performing health checks |
<br>

#### Auto Scaling Policy
| - | - |
| - | - |
| **Metric Type** | Average CPU utilization |
| **Target value** | 75% |
<br>

*back to [top](#top)*  
<br>

### Application Load Balancer
| - | - |
| - | - |
| **Name** | "load-balancer-ws" |
| **VPC** | [VPC-1 Web](#vpc-1-web) |
<br>

#### Target Group
| - | - |
| - | - |
| **VPC** | [VPC-1 Web](#vpc-1-web) |
| **Port** | 443 |
| **Targets** | [Auto Scaling Group](#auto-scaling-group) |
| **Health Check** | Enabled |
<br>

#### HTTPS Listener
| - | - |
| - | - |
| **Protocol** | HTTPS |
| **Port** | 443 |
| **Actions** | Forward traffic to [Target Group](#target-group) |
| **Certificate** | Certificate in Certificate Manager in console. (For test purposes you need to import a self-signed certificate in Certificate Manager using console.) |
| **Security policy** | TLS13-1-2-2021-06 |
<br>

#### HTTP Listener
| - | - |
| - | - |
| **Protocol** | HTTP |
| **Port** | 80 |
| **Actions** | Redirect traffic to port 443 |
<br>

*back to [top](#top)*  
<br>

### RDS MySQL Database
| - | - |
| - | - |
| **Command to connect to database** | `mysql -h <RDS_ENDPOINT> -u <USERNAME> -p` |
| **RDS Endpoint** | Can be found in RDS console |
| **Username** | "admin" |
| **Password** | Stored in Secrets Manager |
| **Port** | 3306 |
| **VPC** | [VPC-1 Web](#vpc-1-web) |
| **Availability Zone** | Multi-AZ |
| **Encryption** | Enabled |
| **Maintenance window** | Region Frankfurt (eu-central-1) -> a 30-minute window between 21:00 - 5:00 <ins>UTC</ins> |
| **Backup window** | Region Frankfurt (eu-central-1) -> a 30-minute window between 20:00 - 4:00 <ins>UTC</ins> |  
<br>

*back to [top](#top)*  
<br>

### Backup
<br>

*back to [top](#top)*  
<br>

### S3 Buckets
#### Bucket Webfiles
#### Bucket Scripts
<br>

*back to [top](#top)*  
<br>

### User Data Webserver
```bash
#!/bin/bash

# WEBSERVER
# perform a quick software update on instance
sudo dnf update -y
# install the latest versions of Apache web server and PHP packages for AL2023
sudo dnf install -y httpd wget php-fpm php-mysqli php-json php php-devel
# get lab files from local S3 bucket for load testing
sudo aws s3 cp s3://cdkbucket-forwebserver-121212/ /var/www/html/ --recursive
# start the Apache web server
sudo systemctl start httpd
# configure the Apache web server to start at each system boot
sudo systemctl enable httpd
# Enable TLS/SSL support, mod_ssl also automatically creates a self-signed certificate.
sudo dnf install mod_ssl -y
# Fully restart Apache
sudo systemctl restart httpd.service

# MYSQL (CLIENT)
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
```