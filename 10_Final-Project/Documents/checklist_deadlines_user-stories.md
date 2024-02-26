# <a id="top">Checklist, Deadlines, and Epics & User Stories</a> ✅ 📌 📄
An overview of my up-to-date checklist/to-do-list, deadlines, and user stories. This document helps me to keep an overview of what I still need to do.

## Table of Contents
- [Checklist](#checklist)
    - [Exploration, deadline --> 12 Jan '24](#exploration-deadline----12-jan-24)
    - [Presentation V1.0 progress --> 26 Jan '24](#presentation-v10-progress----26-jan-24)
    - [V1.0, deadline --> 02 Feb '24](#v10-deadline----02-feb-24)
    - [Presentation V1.1 progress --> 09 Feb '24](#presentation-v11-progress----09-feb-24)
    - [V1.1, deadline --> 23 Feb '24](#v11-deadline----23-feb-24)
    - [Final Presentation --> 23 Feb '24](#final-presentation----23-feb-24)
- [Epics & User Stories](#epics--user-stories)
    - [Exploration](#exploration) 
    - [V1.0](#v10) 
    - [V1.1](#v11) 
<br>

## Checklist
This checklist is based on the Deliverables in the chapter [Epics & User Stories](#epics--user-stories) below.

🐂 *= yet to start doing*  
🔥 *= under construction*  
🍔 *= (well-)DONE!*  
❌ *= failed to do*

### Exploration, deadline --> 12 Jan '24
- 🍔 1. A point-by-point description of all requirements.  
- 🔥 2. A point-by-point overview of all assumptions.
- 🔥 3. An overview of all services that will be used.  

### Presentation V1.0 progress --> 26 Jan '24
- 🍔 A 10-minute presentation / demonstration of my progress on app V1.0.

### V1.0, deadline --> 02 Feb '24
- 🍔 1. IaC code for the network and all components.
    - 🍔 VPC Webserver
    - 🍔 VPC Adminserver
    - 🍔 VPC Peering
    - 🍔 NACLs
- ❌ 2. IaC code for a web server and all supplies.
    - 🍔 Key Pair
    - 🍔 Security Group
    - 🍔 Security Group rules
        - 🍔 Allow incoming "HTTP" traffic
        - 🍔 Allow incoming traffic from Admin server
    - 🍔 User data as a file
    - 🍔 Instance
    - 🍔 NACL rules update
        - 🍔 Allow incoming "HTTP" traffic
        - 🍔 Allow ephemeral traffic
        - 🍔 Allow incoming traffic from Admin server
    - ❌ Database
- 🍔 3. IaC code for a management server with all the necessities.
    - 🍔 Key Pair
    - 🍔 Security Group
    - 🍔 Security Group rules
        - 🍔 Allow incomming "RDP" traffic from my IP
    - 🍔 Instance
    - 🍔 EBS attached volume
    - 🍔 NACL rules update
        - 🍔 Allow incomming "RDP" traffic from my IP
        - 🍔 Allow ephemeral traffic
        - 🍔 Allow outbound
    - 🍔 Connection with Webserver
- ❌ 4. IaC code for a script storage solution.
    - 🍔 S3 Bucket
    - ❌ Upload scripts automatically
- 🍔 5. IaC code for encryption facilities.
    - 🍔 Web server root volume encrypted
    - 🍔 Admin server root volume encrypted
    - 🍔 Admin server attached volume encrypted
    - 🍔 Backup vault
    - 🍔 S3 script bucket
- 🍔 6. IaC code for backup facilities.
    - 🍔 Backup plan
    - 🍔 Back up Web server
    - 🍔 Back up Admin server
- ❌ 7. Documentation for using the application.
- ❌ 8. Configuration for an MVP deployment.

### Presentation V1.1 progress --> 09 Feb '24
- 🍔 A 10-minute presentation / demonstration of my progress on app V1.1.

### V1.1, deadline --> 22 Feb '24
- 🍔 0. Database feature from v1.0
    - 🍔 Security group
    - 🍔 MySQL Instance
    - 🍔 Security group rules
        - 🍔 Allow traffic on MySQL port
    - 🍔 Configure webserver to connect to database
- ❌ 0.5 Post Deployment Script Storage feature from v1.0
    - 🍔 S3 Bucket
    - ❌ Connection with RDS MySQL database
    - ❌ Test script
- 🍔 1. Webserver not "naked" anymore -> no public IP address
- 🍔 2. HTTPS
    - 🍔 TLS 1.2 or higher
    - 🍔 Automatic HTTP redirect to HTTPS
    - 🍔 Self signed certificate
        - 🍔 for the connection between load balancer and webservers
        - 🍔 for the connectiom between clients and load balancer
- 🍔 3. Autoscaling
    - 🍔 Launch Template
    - 🍔 Scaling policy
    - 🍔 Max 3 webservers
- 🍔 4. Loadbalancer
    - 🍔 Loadbalancer itself
    - 🍔 Target Group
    - 🍔 Listeners
        - 🍔 port 80
        - 🍔 port 443
- 🍔 5. Healthchecks
    - 🍔 Auto Scaling -> EC2: always enabled.
    - 🍔 Auto Scaling -> ELB: monitors whether intances are available to handle requests. When it reports an unhealthy instance, EC2 Auto Scaling can replace it on its next periodic check.
    - 🍔 Target Group: If the target type is instance or ip, health checks are always enabled and cannot be disabled.
- 🍔 6. Keep NACLs up-to-date.
- 🍔 7. Design Documentation for using the application.
    - 🍔 Architecture Design
    - 🍔 Estimated monthly costs
    - 🍔 Configurations
        - 🍔 VPCs
            - 🍔 VPC web
            - 🍔 VPC admin
            - 🍔 VPC peering
        - 🍔 Security Groups
        - 🍔 NACLs
        - 🍔 Admin Webserver
        - 🍔 Admin Server
        - 🍔 Autoscaling
        - 🍔 Application Load Blancer
        - 🍔 Database
        - 🍔 Backups
        - 🍔 S3 Buckets
            - 🍔 Webfiles
            - 🍔 Scripts
- 🐂 8. Configuration for an MVP deployment.

### Final Presentation --> 22 Feb '24
- 🍔 A 30-minute presentation of my v1.1 delivery.  
<br>

*back to [top](#top)*  
<br>

## Epics & User Stories
The Product Owners have already had a meeting and have drawn up the following epics and backlog. You will work on these epics and user stories as a team.

If you and your team identify user stories that need to be split into smaller stories, your team is free to do so.

The following epics apply to the project:

| Epic | Description | Deadline |
| - | - | - |
| Exploration | The exploration epic is intended to make choices about the project. Once you've finished this epic, make sure you don't have to come back to it. You don't have enough time to make major adjustments. | 12 Jan '24 |
| v1.0 | Epic v1.0 is the delivery of the Infrastructure as Code and all required documentation to the requirements you discovered during the exploration. | 02 Feb '24 |
| v1.1 | Version 1.1 is the delivery of the Infrastructure as Code and all required documentation according to the requirements that will become available later. | 23 Feb '24 |
<br>

### Exploration
Here are the user stories for the epic Exploration.

|  | User Story | Description | Deliverable |
| - | - | - | - |
| 1 | As a team, we want to be clear about the requirements of the application. | You have already received a lot of information. Some requirements are already mentioned in this document, but this list may be incomplete or unclear. It is important to sort out all the uncertainties before you start doing major work. | A point-by-point description of all requirements. |
| 2 | As a team, we want a clear overview of the assumptions we have made. | You have already received a lot of information. There may be questions that none of the stakeholders have been able to answer. Your team should be able to produce an overview of the assumptions you are making as a result. | A point-by-point overview of all assumptions. |
| 3 | As a team, we want to have a clear overview of the Cloud Infrastructure that the application needs. | You have already received a lot of information. And already a design. Only aspects such as IAM/AD are still missing from the design. Identify these additional services you will need and make an overview of all services. | An overview of all services that will be used. |
<br>

### V1.0
Here are the user stories for the epic V1.0.

|  | User Story | Description | Deliverable |
| - | - | - | - |
| 1 | As a customer, I want a working application with which I can deploy a secure network. | The application must build a network that meets all requirements. An example of a stated requirement is that only traffic from trusted sources may access the management server. | IaC code for the network and all components. |
| 2 | As a customer I want a working application with which I can deploy a working web server. | The application must start a web server and make it available to the general public. | IaC code for a web server and all supplies. |
| 3 | As a customer, I want a working application with which I can deploy a working management server. | The application must start a management server and make it available to a limited audience. | IaC code for a management server with all the necessities. |
| 4 | As a customer I want a storage solution in which bootstrap/post-deployment script can be stored. | There must be a location available where bootstrap scripts become available. This script should not be publicly accessible. | IaC code for a script storage solution. |
| 5 | As a customer, I want all my data in the infrastructure to be encrypted. | Much value is attached to the security of data at rest and in motion. All data must be encrypted. | IaC code for encryption facilities. |
| 6 | As a customer, I want to have a backup every day that is retained for 7 days. | The customer would like to have a backup available should it be necessary to restore the servers to a previous state. (Make sure the Backup actually works) | IaC code for backup facilities. |
| 7 | As a customer I want to know how I can use the application. | Make sure the customer can understand how to use the application. Make sure it is clear what the customer must configure before the deployment can start and which arguments the program needs. | Documentation for using the application. |
| 8 | As a customer, I want to be able to deploy an MVP for testing. | The customer wants to test your architecture internally before using the code in production. Ensure that configuration is available that allows the customer to deploy an MVP. | Configuration for an MVP deployment. |
<br>

### V1.1
Here are the user stories for the epic V1.1.

|  | User Story | Description | Deliverable |
| - | - | - | - |
| 1 | ... | The web server must no longer be "naked" on the internet. The customer would prefer to see a proxy intervene. The server will also no longer need to have a public IP address. | IaC code |
| 2 | ... | If a user connects to the load balancer via HTTP, this connection should be automatically upgraded to HTTPS. | IaC code |
| 3 | ... | The connection must be secured with at least TLS 1.2 or higher. | IaC code |
| 4 | ... | The web server must undergo a health check on a regular basis. If the web server fails this health check, the server should be automatically restored. | IaC code |
| 5 | ... | If the web server comes under persistent load, a temporary additional server should be started. | IaC code |
| 6 | As a customer I want to know how I can use the application. | Make sure the customer can understand how to use the application. Make sure it is clear what the customer must configure before the deployment can start and which arguments the program needs. | Documentation for using the application. |
| 7 | As a customer, I want to be able to deploy an MVP for testing. | The customer wants to test your architecture internally before using the code in production. Ensure that configuration is available that allows the customer to deploy an MVP. | Configuration for an MVP deployment. |
<br>

*back to [top](#top)*  
<br>