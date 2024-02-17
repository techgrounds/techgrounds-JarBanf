# Design Document 📘 👷 🔨
This document contains technical and practical information about my application.  
Diagrams, (N)SG rules, deployment visualization, and more, are listed here.

## v1.1
Under Construction.

### Security Groups

### NACL

### Database
- **Username**: "Admin"
- **Password**: Stored in Secrets Manager
- **Availability Zone**: Multi-AZ
- **Encryption**: Enabled
- **Maintenance window**: Region Frankfurt (eu-central-1) -> a 30-minute window between 21:00 - 5:00 <ins>UTC</ins>
- **Backup window**: Region Frankfurt (eu-central-1) -> a 30-minute window between 20:00 - 4:00 <ins>UTC</ins>