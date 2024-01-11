# <a id="top">Decisions Document</a> 📗 💭 💡 🔨
While implementing the infrastructure design, I will make decisions about, among other things, the services I will use.   
In this document I will write down my considerations and explain my decisions. This document will also contain my assumptions and improvements.  
This serves as the basis for my design documentation. 

## Table of Contents
- [Customer Background Information](#customer-background-information)
- [Cloud Infrastructure Requirements](#cloud-infrastructure-requirements)
- 
- 

## Customer Background Information
### 🏫 🏢 🏦 🏤
### Organization
-	Based in NL
-	Small office, including administration department
-	One IT administrator who has yet to join the team
-	The IT administrator is a senior with good knowledge of the cloud services and will be updating and patching the infrastructure and services him/her-self after deployment.

### Customer Goals
-	Working website with database which can be accessed from the internet
-	Administrator server
-	Only the cloud infrastructure is needed, migration of data will be done in-house.
-	No support plans wanted.
-	In the future: 30+ virtual windows workstations. (at the moment 30 on-premise workstations)

### Webserver
-	Simple website, nothing fancy
-	99% of traffic from NL
-	During office hours more traffic to the website
-	Expecting a bit of traffic growth but nothing relevant
-	Current on-premise webserver way too big for their usage

### Administrator server
-	Only the one IT administrator will be accessing the server.
-	From this server will the future 30+ virtual workstations be administered.

### Security
-	Protection against attacks and hacking will be done in-house

### Budget
-	As cheap as possible while meeting the necessary requirements
-	Development: maximum €10
-	Production: maximum €150 / month

*back to [top](#top)* 

## Cloud Infrastructure Requirements
### ☁️

🔵 = Initial requirements.  
🟠 = Additional requirements following meeting with product owner on Wed 10 Jan ’24.

:large_blue_circle:  
:small_blue_circle:  
:small_blue_diamond:  
:small_orange_diamond:  
:small_red_diamond:  
:small_purple_diamond:  

*back to [top](#top)* 