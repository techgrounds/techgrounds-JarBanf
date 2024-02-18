# Design Document 📘 👷 🔨
This document contains technical and practical information about my application.  
Diagrams, (N)SG rules, deployment visualization, and more, are listed here.

## v1.1
Under Construction.

### Estimated Monthly Costs

### Security Groups
#### Webserver
##### Inbound
| Type | Port | Source | Description |
| - | - | - | - |
| HTTP | 80 | 10.0.2.4/32 | Allow HTTP traffic from admin server |
| HTTPS | 443 | 10.0.2.4/32 | Allow HTTPS traffic from admin server |
| SSH | 22 | 10.0.2.4/32 | Allow SSH traffic from admin server |
##### Outbound 
| Type | Port | Source | Destination |
| - | - | - | - |
| All Traffic | All | 0.0.0.0/0 | Allow all outbound traffic by default |

#### Admin Webserver
#### Application Load Balancer
#### Auto Scaling Webservers
#### RDS MySQL Database

### NACL

### RDS MySQL Database
- **Command to connect to database**: `mysql -h <RDS_ENDPOINT> -u <USERNAME> -p`
- **RDS Endpoint**: Can be found in RDS console
- **Username**: "admin"
- **Password**: Stored in Secrets Manager
- **Port**: 3306
- **Availability Zone**: Multi-AZ
- **Encryption**: Enabled
- **Maintenance window**: Region Frankfurt (eu-central-1) -> a 30-minute window between 21:00 - 5:00 <ins>UTC</ins>
- **Backup window**: Region Frankfurt (eu-central-1) -> a 30-minute window between 20:00 - 4:00 <ins>UTC</ins>