# <a id="top">Design Document v1.1</a> 📘 👷 🔨
**UNDER CONSTRUCTION**  
This document contains technical and practical information about my application.  
Diagrams, (N)SG rules, deployment visualization, and more, are listed here.

## Table of Contents
- [Architecture Design](#architecture-design)
- [Estimated Monthly Costs](#estimated-monthly-costs)
- [Configurations](#configurations)
    - [Security Groups](#security-groups)
        - [Admin Web-Server](#admin-web-server)
        - [Admin Server](#admin-server)
        - [Application Load Balancer](#application-load-balancer)
        - [Auto Scaling Webservers](#auto-scaling-webservers)
        - [RDS MySQL Database](#rds-mysql-database)
    - [NACLs](#nacls)
        - [VPC Webserver Public Subnets](#vpc-webserver-public-subnets)
        - [VPC Webserver Private Subnets](#vpc-webserver-private-subnets)
        - [VPC Admin Public Subnets](#vpc-admin-public-subnets)
    - [RDS MySQL Database](#rds-mysql-database-1)
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
### Security Groups
#### Admin Web-Server
##### Inbound
| Type | Port | Source | Description |
| - | - | - | - |
| HTTP | 80 | 10.0.2.4/32 | Allow HTTP traffic from admin server |
| HTTPS | 443 | 10.0.2.4/32 | Allow HTTPS traffic from admin server |
| SSH | 22 | 10.0.2.4/32 | Allow SSH traffic from admin server |
##### Outbound 
| Type | Port | Destination | Description |
| - | - | - | - |
| All Traffic | All | 0.0.0.0/0 | Allow all outbound traffic by default |

#### Admin Server
##### Inbound
| Type | Port | Source | Description |
| - | - | - | - |
| RDP | 3389 | Admin home/office IP | Allow RDP from Admin home/office IP |

##### Outbound 
| Type | Port | Destination | Description |
| - | - | - | - |
| All Traffic | All | 0.0.0.0/0 | Allow all outbound traffic by default |

#### Application Load Balancer
##### Inbound
| Type | Port | Source | Description |
| - | - | - | - |
| - | - | - | - |
| - | - | - | - |

##### Outbound 
| Type | Port | Destination | Description |
| - | - | - | - |
| All Traffic | All | 0.0.0.0/0 | Allow all outbound traffic by default |

#### Auto Scaling Webservers
##### Inbound
| Type | Port | Source | Description |
| - | - | - | - |
| - | - | - | - |
| - | - | - | - |

##### Outbound 
| Type | Port | Destination | Description |
| - | - | - | - |
| All Traffic | All | 0.0.0.0/0 | Allow all outbound traffic by default |

#### RDS MySQL Database
##### Inbound
| Type | Port | Source | Description |
| - | - | - | - |
| MYSQL/Aurora | 3306 | 10.0.1.0/24 | Allow MySQL from VPC |

##### Outbound 
| Type | Port | Destination | Description |
| - | - | - | - |
| All Traffic | All | 0.0.0.0/0 | Allow all outbound traffic by default |
<br>

*back to [top](#top)*  
<br>

### NACLs
#### VPC Webserver Public Subnets
##### Inbound
##### Outbound 

#### VPC Webserver Private Subnets
#### VPC Admin Public Subnets
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
| **Availability Zone** | Multi-AZ |
| **Encryption** | Enabled |
| **Maintenance window** | Region Frankfurt (eu-central-1) -> a 30-minute window between 21:00 - 5:00 <ins>UTC</ins> |
| **Backup window** | Region Frankfurt (eu-central-1) -> a 30-minute window between 20:00 - 4:00 <ins>UTC</ins> |  
<br>

*back to [top](#top)*  
<br>