# Public key infrastructure
Public key infrastructure (PKI) is a technology for authenticating users and devices in the digital world. The basic idea is to have one or more trusted parties digitally sign documents certifying that a particular cryptographic key belongs to a particular user or device. The key can then be used as an identity for the user in digital networks.

Most public key infrastructure use a standardized machine-readable certificate format for the certificate documents. The standard is called X.509v3.

<ins>Common uses of certificates</ins>  
- Secure Web Sites - HTTPS
- Authenticating users and computers - SSH
- Email signing and encryption

## Key-terms


## Assignment
1. Create a self-signed certificate on your VM.
2. Analyze some certification paths of known websites (ex. techgrounds.nl / google.com / ing.nl).
3. Find the list of trusted certificate roots on your pc/laptop (bonus points if you also find it in your VM).

### Used sources
- [What is PKI (Public Key Infrastructure)?](https://www.ssh.com/academy/pki)
- [How To Create a Self-Signed SSL Certificate for Apache in Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-22-04)

### Encountered problems
None

### Result
**1. Create a self-signed certificate on your VM.**

- Step 1: Check status Apache2.
```
systemctl status apache2
```
Apache is enabled and active.

![check apache2 actief](/03_Security/images/05_public-key-infrastructure1-1.png)<br><br>

- Step 2: Check if firewall is set up to allow incoming connections on port 80/http and port 443/https. 
```
sudo ufw status
```
Not allowed yet.

![check port 80 and 443 if open](/03_Security/images/05_public-key-infrastructure1-2.png)<br><br>

- Step 3: Allow incoming connections on port 80/http and port 443/https and check status again.
```
sudo ufw allow "Apache Full"
```
```
sudo ufw status
```
![open port 80 and 443 and check again](/03_Security/images/05_public-key-infrastructure1-3.png)<br><br>

- Step 4: Enable mod_ssl, an apache module that provides support for SSL encryption.
```
sudo a2enmod ssl
```
![enable mod_ssl](/03_Security/images/05_public-key-infrastructure1-4.png)<br><br>

- Step 5: Restart apache to activate the module:
```
sudo systemctl restart apache2
```

- Step 6: Create the TLS Certificate.
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```
What is happening in the command?
- `openssl`: This is the command line tool for creating and managing OpenSSL certificates, keys, and other files.
- `req -x509`: This specifies that we want to use X.509 certificate signing request (CSR) management. X.509 is a public key infrastructure standard that TLS adheres to for key and certificate management.
- `-nodes`: This tells OpenSSL to skip the option to secure our certificate with a passphrase. We need Apache to be able to read the file, without user intervention, when the server starts up. A passphrase would prevent this from happening, since we would have to enter it after every restart.
- `-days 365`: This option sets the length of time that the certificate will be considered valid. We set it for one year here. Many modern browsers will reject any certificates that are valid for longer than one year.
- `-newkey rsa:2048`: This specifies that we want to generate a new certificate and a new key at the same time. We did not create the key that is required to sign the certificate in a previous step, so we need to create it along with the certificate. The `rsa:2048` portion tells it to make an RSA key that is 2048 bits long.
- `-keyout`: This line tells OpenSSL where to place the generated private key file that we are creating.
- `-out`: This tells OpenSSL where to place the certificate that we are creating.

After entering the command, I will be taken to a prompt where I can enter information about my website.  
The most important line is the one that requests the `Common Name`. I need to enter either the hostname I will use to access the server by, or the public IP of the server. It’s important that this field matches whatever I will put into my browser’s address bar to access the site, as a mismatch will cause more security errors.

![create tls cert](/03_Security/images/05_public-key-infrastructure1-6.png)<br><br>

**2. Analyze some certification paths of known websites (ex. techgrounds.nl / google.com / ing.nl).**
- techgrounds.nl:

![cert techgrounds](/03_Security/images/05_public-key-infrastructure2-1.png)<br><br>

- google.com

![cert google](/03_Security/images/05_public-key-infrastructure2-2.png)<br><br>

- ing.nl

![cert ing.nl](/03_Security/images/05_public-key-infrastructure2-3.png)<br><br>

**3. Find the list of trusted certificate roots on your pc/laptop (bonus points if you also find it in your VM).**

- My laptop: In the Keychain Access app.

![cert ing.nl](/03_Security/images/05_public-key-infrastructure3-1.png)<br><br>

- My VM: `/etc/ssl/certs`.

![cert ing.nl](/03_Security/images/05_public-key-infrastructure3-2.png)<br><br>