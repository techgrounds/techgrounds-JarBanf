# Detection, response & analysis
Threat detection, response and analysis are crucial elements of a cybersecurity strategy aimed at safeguarding an organization's digital environment. Various cyber threats can compromise an organization's security posture, leading to data breaches or network downtime.

<ins>Detection</ins>  
Threat detection is the process of identifying, analyzing and mitigating potential and current cyber threats to an organization's network. It is an essential aspect of an organization's security posture.  
Effective threat detection requires continuous monitoring
and analysis of network activity, using various tools and techniques to indentify, prioritize, and respond to potential threats.

<ins>Response</ins>  
Threat response is the process of mitigating and eliminating threats to an organization's netowrk. It involves taking appropriate actions to identify, contain, and remove existing threats, as well as protect against future attacks.  
Effective threat response requires rapid decision-making based on detailed analysis and understanding of the threat environment.

<ins>Analysis/Investigation</ins>  
Threat investigation is the process of analyzing detected threats to understand their impact on an organization and to develop an incident response plan. Once a threat is detected, security teams conduct analysis and triage to determine the nature and severity of the threat. This process may involve forensic analysis of network resources, systems, and applications.

## Key-terms


## Assignment
<ins>Study:</ins>
- IDS and IPS
- Hack response strategies
- The concept of systems hardening
- Different types of disaster recovery options

<ins>Exercise:</ins>
1. A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?
2. An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?

### Used sources
- [What is Threat Detection, Investigation, and Response?](https://www.anomali.com/resources/what-is-threat-detection-investigation-and-response)
- [IDS vs. IPS: What Organizations Need to Know](https://www.varonis.com/blog/ids-vs-ips)
- [What Is System Hardening?](https://blog.netwrix.com/2023/02/22/system-hardening/)
- [Understanding the Different Types of Disaster Recovery Plans](https://www.empowerit.com.au/blog/it-planning/different-types-disaster-recovery-plans/)
- [What is the difference between RPO and RTO](https://www.acronis.com/en-eu/blog/posts/rto-rpo/)

### Encountered problems
None

### Result
**- IDS and IPS**

Network administrators need to employ tools to protect their network and prevent malicious actors from gaining access. Intrusion detection systems (IDS) and intrusion prevention systems (IPS) are catogories of tools commonly used for this purpose.  

<ins>IDS</ins>  
An IDS monitors and detects behavior across a network and should be considered a diagnostic solution. The system, if it detects something problematic, it will alert the security team so they can investigate.  
An IDS is more of an alerting system that lets an organization know if anomalous or malicious activity is detected. 

<ins>IPS</ins>  
An IPS has the same functionality as IDS systems in terms of detection but also contains response capabilties.   
An IPS takes the IDS a step forward and shuts down the network before access can be gained or to prevent further movement in a network.
<br><br>

**- Hack response strategies**

Depending on the type of threat, threat response activities may include:  
- patching vulnerable systems
- eliminating malware
- blocking malicious actors from accessing networks
- contact law enforcements or other relevant authorities to investigate and prosecute cybercrimes.
- implementing additional security controls, such as: 
- --> IPS, intrusion prevention system
- --> two-factor authentication
- --> conducting vulnerability assessments
- --> educating users on best security practices

By taking proactive steps, organizations can minimize the risk of future attacks and improve their overall security posture.
<br><br>

**- The concept of systems hardening**

System hardening is also known as server hardening, security hardening and operation systems hardening. System hardening is a suite of techniques, tools, and methodologies for reducing vulnerability in servers and computers. System hardening aims to reduce network and IT security risks by eliminating unnecessary services and applications as well as activating build-in security features. The fewer attack vectors, the fewer opportunities attackers have for entering your IT ecosystem.

We can split hardening activities on functional level:
- **Operating system hardening**: reducing vulnerability in operating systems on servers and endpoints by removing unnecessary services, disabling unnecessary accounts, and adjusting security settings to meet industry standards.
- **Network hardening**: fortifying network infrastructure by configuring firewalls (both hardware and software), implementing intrusion detection systems (IDS) and intrusion prevention systems (IPS), and conducting regular vulnerability assessments.
- **Database hardening**: enhancing security of databases by emplementing access controls, encrypting sensitive data, and adjusting security settings.
- **Application hardening**: adjusting the settings of applications like MS Exchange or MS Office for increased security against exploitation using macros or similar scripting attacks.
- **Remote systems hardening**: protecting remote systems and devices by implementing secure access controls, and monitoring for vulnerabilities and threats.
<br><br>

**- Different types of disaster recovery options**

Businesses rely on documents, files, servers, and applications for their daily operations. If sensitive data or a critical system is lost or goes offline, this can have major impact on an organization, leading to financiel losses, reputation loss, and even legal exposure. 

A disaster is an unexpected problem that can slow, disrupt, or destroy IT systems. This could be an earthquake or other natural disaster, a technical malfunction or equipment failure, human error, or an attack by malicious parties, either inside or outside the organization.

<ind>Different types of disaster recovery:</ins>
- **Backup-only disaster recovery**: your files are copied to different locations. Onsite, on a removable drive, and/or secure data centers.  
But as far as disaster recovery goes, back-up-only strategies are not enough because they're focused solely on securing files rather than the entire IT infrastructure. This isn't necessarily a bad thing since you need your data to work, but you also need your servers, computers, and apps to be operational too.
- **Cold site disaster recovery**: involves renting out space in a secondary facility where you can set up a temporary office in the event of a disaster. These facilities have the basic infrastructure required to get servers and data online, including power, cooling, and network connecticity.  
Because you will need to install the hardware, reinstall software, and reload data when disaster strikes, recovery ussually takes 3-5 days.
- **Hot site disaster recovery**: where an identical facility is set up in a remote location, fully equipped with systems preloaded with apps, data, and security software. Hot sites are active and have up-to-date copies of data at all times, so if the primary site fails, employees can simply move to the hot site and work as if nothing happened.
- **Virtual disaster recovery**: managed service providers create a working replica of your entire computing environment, including servers, storage space, operating system, apps, and data. So in the event of a major disaster like a ransomware attack that locks down your user's computers, you can run a VM on those machines and it will be as if the incident never occured.
<br><br>

**1. A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?**

RPO, recovery point objective, generally refers to calculating how much data loss a company can experience within a period most relevant to its business before significant harm occurs, from the point of a disruptive event to the last data backup.
RPO helps determine how much data a company can tolerate losing during an unforeseen event.

Since the company makes daily backups (once per 24 hours), the database's RPO is counted for 24 hours of data loss.

**2. An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?**

RTO, recovery time objective, often refers to the amount of time that an application, system and process can be down without causing significant damage to the business and the time spent restoring the application and it data to resume normal business operations after a significant incident.

Since the recovery time takes about 8 minutes, the website's RTO is minimum 8 minutes.