# <a id="top">Decisions Document</a> 📗 💭 💡 
While implementing the infrastructure design, I will make decisions about, among other things, the services I will use.   
In this document I write down my considerations and explain my decisions. This document also contain my assumptions and improvements.  
This serves as the basis for my design documentation.  
<br>

## Table of Contents
- [Customer Background Information](#cbi)
- [Cloud Infrastructure Requirements](#cir)
- [Assumptions](#ass)
- [Services](#ser)
- Appendix
    - [1: Provided non-definite Architecture Design](#1-provided-non-definite-architecture-design)  
<br>

## <a id="cbi">Customer Background Information</a> 🏢 👔 ℹ️
Background information about the customer that can be useful when designing the cloud infrastructure.  

### Organization
- Based in NL
- Small office, including administration department
- One IT administrator who has yet to join the team
- The IT administrator is a senior with good knowledge of the cloud services and will be updating and patching the infrastructure and services him/her-self after deployment.

### Customer Goals
- A working website which can be accessed from the internet
- An admin / management server
- Only the cloud infrastructure is needed, migration of data will be done in-house.
- No support plans wanted.
- In the future: 30+ virtual windows workstations. (at the moment 30 on-premise workstations)

### Webserver
- Simple website, nothing fancy
- Attached to a database
- 99% of traffic from NL
- During office hours more traffic to the website
- Expecting a bit of traffic growth but nothing relevant
- Current on-premise webserver way too big for their usage

### Admin / Management server
- Only the one IT administrator will be accessing the server.
- From this server will the future 30+ virtual workstations be administered.

### Security
- Protection against attacks and hacking will be done in-house.  
<br>

*back to [top](#top)*  
<br>

## <a id="cir">Cloud Infrastructure Requirements</a> ☁️ 📋 ✅  
A description of all necessary requirements.  
<br>

🔵 = *Initial necessary requirements.*  
🟠 = *Additional necessary requirements following meeting with product owner on Wed 10 Jan ’24.*

### Network
- 🔵 The following IP ranges are used: 10.10.10.0/24 & 10.20.20.0/24.
- 🟠 Subnet where future workstations will be located must have at least 30 usable IP addresses, excluding room for possible growth. Large growth is not expected in the short term.

### Web server & Database
- 🟠 Website 24/7 online.
- 🔵 The web server must be installed in an automated manner.
- 🟠 SQL database needed for the website; post script deployment must be able to run.
- 🟠 We do not need to connect the database to the website, but we do need to ensure that connection can be made.
- 🟠 Scalability of the webserver; is not clear whether the customer wants this, but it does sound interesting according to the product owner.

### Admin / management server
- 🔵 The admin / management server must be reachable with a public IP.
- 🔵 The admin / management server must only be accessible from trusted locations (office/admin’s home).
- 🟠 Admin / management server must run on windows
- 🟠 Admin server may not go down together with the workstations in the event of a malfunction.
- 🟠 Access to admin / management server: use my own IP address during development. In production this will be the IP address of the admin’s trusted location.

### Storage
- 🔵 There must be a location available where bootstrap scripts become available. This script should not be publicly accessible.	
- 🟠 Scripts:
    - Installation scripts
    - Configuration scripts
    - Post deployment scripts
    - No expiration date for the stored scripts
    - Access to the scripts: admin & machines/processes that call the scripts

### Backup
- 🔵 The web server must be backed up daily. The backups must be retained for 7 days.
- 🔵 Backup available should it be necessary to restore the servers to a previous state.
- 🟠 Recovery Point Objective (RPO): 24 hours.
- 🟠 Recovery Time Objective (RTO): 1 hour.
- 🟠 Back-up should preferably take place at a time that it is not busy. 4 AM for example.

### Security
- 🔵 Much value is attached to the security of data at rest and in motion. All data must be encrypted.
- 🔵 All VM disks must be encrypted.
- 🟠 VM encryption: industry standard.
- 🔵 All subnets must be protected by a firewall at subnet level.
- 🔵 SSH or RDP connections to the web server may only be established from the admin server.

### Budget
- 🟠 As cheaply as possible within the necessary requirements.
- 🟠 Development: maximum €10.
- 🟠 Production: maximum €150.

### Global
- 🔵 Don’t be afraid to propose or implement improvements in the architecture, but make hard choices so you can meet the deadline.  
<br>

*back to [top](#top)*  
<br>

## <a id="ass">Assumptions</a> 🚦 🔀 ❓
An overview of all my assumptions.

I will be referring to [Appendix 1: Provided non-definite Architecture Design](#appendix-1-provided-non-definite-architecture-design) in this document.  
<br>

- **Only 1 region**: In the provided architecture design, the solutions architect chose to implement 2 regions. I can’t find a reason why this is necessary. I will adjust the design and use only 1 region.
- **No VPC Peering**: Because I will use only one region, I will be deploying the resources in only 1 VPC as well. This eliminates the need for VPC Peering.
- **Private subnets**: In the provided architecture design, there is no private subnet. I will be creating private subnets where the future workstation can be placed.
- **NAT gateway**: A NAT gateway will be needed to provide internet access to the workstation-private-subnet and the server-private-subnet via the admin-public-subnet. The admin-public-subnet is where the admin server will pe placed.  
<br>

*back to [top](#top)*  
<br>

## <a id="ser">Services</a> 🟧 🟩 🟥
An overview of all services that will be used.

### Cloud Financial Management
- 🟩 Billing and Cost Management: View and pay bills, analyze and govern your spending, and optimize your costs.

### Compute
- 🟧 EC2: Virtual servers in the cloud.

### Database
- 🟦 ~~RDS: Managed Relational Database Service~~.
    - I will not be implementing a RDS database in my design. The admin has knowledge on setting up and maintaining a database. So I will setup a EC2-instance as a database server.

### Management & Governance
- 🟥 ~~CloudTrail: Track User Activity and API Usage~~.  
    - I will NOT be implementing this service in to the infrastructure (yet).  
    It is best practice to use this service, but seen that it is not defined in the necessary requirements, I will not dedicate time and energy on it (yet). It is not a priority right now.

### Networking & Content Delivery
- 🟪 VPC: Isolated Cloud Resources.

### Security, Identity, & Compliance
- 🟥 ~~Certificate Manager: Provision, Manage, and Deploy SSL/TLS Certificates.~~
    - I will NOT be implementing this service in to the infrastructure (yet).  
    Ideally, I will need to apply for an official SSL certificate to be able to provide encrypted connection to the website. Seen that this is not in the necessary requirements, I will not dedicate time and energy on it (yet). It is not a priority right now.
- 🟥 IAM: Manage access to AWS resources.
- 🟥 Key Management Service: Securely Generate and Manage AWS Encryption Keys

### Storage
- 🟩 S3: Scalable Storage in the Cloud  
<br>

*back to [top](#top)*  
<br>

## Appendix 📎
### 1: Provided non-definite Architecture Design
This is the provided non-definite architecture that the Solutions Architecture designed.  
I have been told that the Solutions Architect did not deliver a solid solution and is also no longer employed.  

I am free to make changes and implement improvements as I see fit.

![provided architecture design](/10_Final-Project/includes/provided%20architecture%20design%20AWS.png) 
*Provided non-definite architecture designed by the Solutions Architect*  
<br>

*back to [top](#top)*  
<br>