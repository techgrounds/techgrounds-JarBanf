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
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

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

### Encountered problems
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Result
**- IDS and IPS**  
Network administrators need to employ tools to protect their network and prevent malicious actors from gaining access. Intrusion detection systems (IDS) and intrusion prevention systems (IPS) are catogories of tools commonly used for this purpose.  

<ins>IDS</ins>  
An IDS monitors and detects behavior across a network and should be considered a diagnostic solution. The system, if it detects something problematic, it will alert the security team so they can investigate.  
An IDS is more of an alerting system that lets an organization know if anomalous or malicious activity is detected. 

<ins>IPS</ins>  
An IPS has the same functionality as IDS systems in terms of detection but also contains response capabilties.   
An IPS takes the IDS a step forward and shuts down the network before access can be gained or to prevent further movement in a network.<br><br>

**- Hack response strategies**  
Depending on the type of threat, threat response activities may include:  
- patching vulnerable systems
- eliminating malware
- blocking malicious actors from accessing networks
- contact law enforcements or other relevant authorities to investigate and prosecute cybercrimes.
- implementing additional security controls, such as: 
- --> IPS, intrusion prevention system
- --> two-facor authentication
- --> conducting vulnerability assessments
- --> educating users on best security practices

By taking proactive steps, organizations can minimize the risk of future attacks and improve their overall security posture.

**- The concept of systems hardening**


**- Different types of disaster recovery options**

**1. A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?**


**2. An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?**

