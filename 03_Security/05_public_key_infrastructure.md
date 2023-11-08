# Public key infrastructure
Public key infrastructure (PKI) is a technology for authenticating users and devices in the digital world. The basic idea is to have one or more trusted parties digitally sign documents certifying that a particular cryptographic key belongs to a particular user or device. The key can then be used as an identity for the user in digital networks.

Most public key infrastructure use a standardized machine-readable certificate format for the certificate documents. The standard is called X.509v3.

<ins>Common uses of certificates</ins>  
- Secure Web Sites - HTTPS
- Authenticating users and computers - SSH
- Email signing and encryption

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Assignment
1. Create a self-signed certificate on your VM.
2. Analyze some certification paths of known websites (ex. techgrounds.nl / google.com / ing.nl).
3. Find the list of trusted certificate roots on your pc/laptop (bonus points if you also find it in your VM).

### Used sources
[Plaats hier de bronnen die je hebt gebruikt.]

### Encountered problems
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Result
**1. Create a self-signed certificate on your VM.**

- Step 1: Check status Apache2.
```
systemctl status apache2
```
Apache is enabled and active.

![check apache2 actief](/03_security/images/05_public-key-infrastructure1-1.png)<br><br>

- Step 2: Check if firewall is set up to allow incoming connections on port 80/http and port 443/https. 
```
sudo ufw status
```
Not allowed yet.

![check apache2 actief](/03_security/images/05_public-key-infrastructure1-2.png)<br><br>

- Step 3: Allow incoming connections on port 80/http and port 443/https and check status again.
```
sudo ufw allow "Apache Full"
```
```
sudo ufw status
```
![check apache2 actief](/03_security/images/05_public-key-infrastructure1-3.png)<br><br>

**2. Analyze some certification paths of known websites (ex. techgrounds.nl / google.com / ing.nl).**


**3. Find the list of trusted certificate roots on your pc/laptop (bonus points if you also find it in your VM).**

