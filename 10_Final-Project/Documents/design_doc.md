# Design Document 📘 👷 🔨
This document contains technical and practical information about my application.  
Diagrams, (N)SG rules, deployment visualization, and more, are listed here.

## v1.1

## v1.0
### Network

- Region: Europe (Frankfurt) --> eu-central-1  
    - VPC: 10.0.0.0/8
        - Availability Zone A: 10.10.10.0 / 24
            - Public Subnet 1: 10.10.10.0 / 29
                - \# IP adresses: 8 (6 usable)
                - Webserver
                - Web Database Server
            - Private Subnet 1: 10.10.10.8 / 29
                - \# IP adresses: 8 (6 usable)
                - Admin Server
            - Private Subnet 2: 10.10.10.16 / 26
                - \# IP adresses: 64 (62 usable)
                - 30+ Workstations
        - Availability Zone B: 10.20.20.0 / 24
            - Used in the future for reliability.
- Security Groups
    - Webserver
    - Web Database server
    - Admin Server
- Network ACL
    - AZ A
        - Public Subnet 1
        - Private Subnet 1
        - Private Subnet 2
    - AZ B