# <a id="top">Design Document v1.1</a> 📘 👷 🔨  
This document contains technical and practical information about my application.  
Architecture Design, Estimated costs, SG & NACL rules, and resource specs are listed here.

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
![architecture design v1.1](/10_Final-Project/includes/v1dot1_architecture_design.drawio.png)  
*Architecture design*
<br>

*back to [top](#top)*  
<br>

## Estimated Monthly Costs
<br>

| Service | Specs | On-Demand no upfront | Savings Plan 1 year upfront | Savings Plan 3 year upfront |
| - | - | - | - | - |
| **NAT Gateway** | amount of NAT gateways: 1 | $ 40,56 | $ 40,56 | $ 40,56 |
| **Webserver** | linux, t3.micro, 40 hours/week | $ 2,09 | $ 2,09 | $ 2,09 |
| **Webserver root EBS** | 8GB, 174 hours/month, daily snapshot, 1GB change/snapshot | $ 0,53 | $ 0,53 | $ 0,53 |
| **Admin server** | windows server, t3.large, 40 hours/week | $ 21,48 | $ 21,48 | $ 21,48 |
| **Admin server root EBS** | 30GB, 174 hours/month, daily snapshot, 1GB change/snapshot | $ 1,44 | $ 1,44 | $ 1,44 |
| **Admin server attached EBS** | 256GB, 174 hours/month, daily snapshot, 1GB change/snapshot | $ 10,82 | $ 10,82 | $ 10,82 |
| **Application Load Balancer** | amount of ALB: 1 | $ 19,95 | $ 19,95 | $ 19,95 |
| **Auto Scaling Webservers** | linux, t3.micro, 8GB root storage, baseline: 1 instance -> 24 hours, peak: 3 instances -> 8hrs on mon, tue, wed, thu, fri | $ 11,56 | $ 5,58 | $ 5,58 |
| **RDS MySQL Database** | db.t3.micro, 20GB gp2, multi-az | $ 34,66 | $ 34,66 | $ 34,66 |
| **S3 storage** | 100GB standard storage, 100000 requests | $ 3,03 | $ 3,03 | $ 3,03 |
|  |  |  |  |  |
|  | **total per month** | $ 146,12 | $ 140,14 | $ 140,14 |
|  | **upfront** | $ 0 | $ 62,20 | $ 118,26 |
|  |  |  |  |  |
|  | **total 1 year cost** | $ 1753,44 | $ 1743,88 | $ 1721,10 |

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
![SG Admin Webserver](/10_Final-Project/includes/v1dot1_SG_admin_webserver.png)  
*SG Admin Webserver*
<br>

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
![SG Adminserver](/10_Final-Project/includes/v1dot1_SG_adminserver.png)  
*SG Adminserver*
<br>

| Type | Port | Source / Destination | Description |
| - | - | - | - |
| **Inbound** |  |  |  |
| RDP | 3389 | Admin home/office IP | Allow RDP from Admin home/office IP |
|  |  |  |  |
| **Outbound** |  |  |  |
| All Traffic | All | 0.0.0.0/0 | Allow all outbound traffic by default |
<br>

#### SG AS Webservers (Auto Scaling)
![SG AS Webservers (Auto Scaling)](/10_Final-Project/includes/v1dot1_SG_as_webservers.png)  
*SG AS Webservers (Auto Scaling)*
<br>

| Type | Port | Source / Destination | Description |
| - | - | - | - |
| **Inbound** |  |  |  |
| HTTPS | 443 | Load Balancer | Load balancer to target |
|  |  |  |  |
| **Outbound** |  |  |  |
| All Traffic | All | 0.0.0.0/0 | Allow all outbound traffic by default |
<br>

#### SG Application Load Balancer
![SG Application Load Balancer](/10_Final-Project/includes/v1dot1_SG_ALB.png)  
*SG Application Load Balancer*
<br>

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
![SG Database](/10_Final-Project/includes/v1dot1_SG_database.png)  
*SG Database*
<br>
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
![NACL VPC-1 Web Public Subnets](/10_Final-Project/includes/v1dot1_NACL_web_public.png)  
*NACL VPC-1 Web Public Subnets*
<br>

| Rule number | Type | Protocol | Port Range | Source / Destination | Allow / Deny |
| - | - | - | - | - | - |
| **Inbound** |  |  |  |  |  |
| 100 | HTTP (80) | TCP (6) | 80 | 0.0.0.0/0 | Allow |
| 110 | HTTPS (443) | TCP (6) | 443 | 0.0.0.0/0 | Allow |
| 120 | Custom TCP | TCP (6) | 1024 - 65535 | 10.0.1.0/24 | Allow |
| * | All traffic | All | All | 0.0.0.0/0 | Deny |
|  |  |  |  |  |  |
| **Outbound** |  |  |  |  |  |
| 100 | HTTP (80) | TCP (6) | 80 | 0.0.0.0/0 | Allow |
| 110 | HTTPS (443) | TCP (6) | 443 | 0.0.0.0/0 | Allow |
| 120 | Custom TCP | TCP (6) | 1024 - 65535 | 0.0.0.0/0 | Allow |
| * | All traffic | All | All | 0.0.0.0/0 | Deny |
<br>

#### VPC-1 Web Private Subnets
![NACL VPC-1 Web Private Subnets](/10_Final-Project/includes/v1dot1_NACL_web_private.png)  
*NACL VPC-1 Web Private Subnets*
<br>

| Rule number | Type | Protocol | Port Range | Source / Destination | Allow / Deny |
| - | - | - | - | - | - |
| **Inbound** |  |  |  |  |  |
| 90 | SSH (22) | TCP (6) | 22 | 10.0.2.4/32 | Allow |
| 100 | HTTP (80) | TCP (6) | 80 | 10.0.0.0/16 | Allow |
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
![NACL VPC-2 Admin Public Subnet](/10_Final-Project/includes/v1dot1_NACL_admin_public.png)  
*NACL VPC-2 Admin Public Subnet*
<br>

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
![Webserver (for admin)](/10_Final-Project/includes/v1dot1_Admin_webserver.png)  
*Webserver (for admin)*
<br>

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
![Admin Server](/10_Final-Project/includes/v1dot1_adminserver.png)  
*Admin Server*
<br>

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
![Auto Scaling](/10_Final-Project/includes/v1dot1_as.png)  
*Auto Scaling*
<br>

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
![Application Load Balancer](/10_Final-Project/includes/v1dot1_alb.png)  
*Application Load Balancer*
<br>

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
![RDS MySQL Database](/10_Final-Project/includes/v1dot1_databse.png)  
*RDS MySQL Database*
<br>

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
![Backup](/10_Final-Project/includes/v1dot1_backup.png)  
*Backup*
<br>

| - | - |
| - | - |
| **Name** | "7-day-Backup-plan" |
| **Backup frequency** | Daily at 01:00 (winter time) / 02:00 (summer time) |
| **Start within** | 1 hour |
| **Complete within** | 2 hours |
| **Total retention** period | 1 week |
|  |  |
| **Resources to backup** |  |
| [**Webserver (for admin)**](#webserver-for-admin) | Root storage |
| [**Admin Server**](#admin-server) | Root & Attached storage |
| **Encryption** | Enabled |
<br>

*back to [top](#top)*  
<br>

### S3 Buckets
#### Bucket Webfiles
![Bucket Webfiles](/10_Final-Project/includes/v1dot1_bucket_webfiles.png)  
*Bucket Webfiles*
<br>

| - | - |
| - | - |
| **Bucket Name** | "cdkbucket-forwebserver-121212" |
| **Content** | Website files (for autoscaling testing purposes I use load/stress-test files as a placeholder which will automatically uploaded to bucket when app deploys) |
| **Encryption** | Enabled |
| **Block all public access** | On |

#### Bucket Post Deployment Scripts
![Bucket Post Deployment Scripts](/10_Final-Project/includes/v1dot1_bucket_scripts.png)  
*Bucket Post Deployment Scripts*
<br>

| - | - |
| - | - |
| **Bucket Name** | "cdkbucket-pdscripts-3434343434" |
| **Content** | Post deployment scripts |
| **Encryption** | Enabled |
| **Block all public access** | On |
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