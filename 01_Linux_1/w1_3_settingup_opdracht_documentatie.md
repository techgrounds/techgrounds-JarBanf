# SSH to Virtual Server
The VM is Located in Frankfurt, so you will need to create a remote connection to your machine. Remote connections to a Linux machine are usually done using the Secure Shell (SSH) protocol.

## Key-terms
VM: Virtual Machine
SSH: Secure Shell protocol

## Opdracht
### Gebruikte bronnen
[File Permissions in Linux / Unix: How to Read, Write & Change?](https://www.guru99.com/file-permissions.html)

[How to connect to an EC2 instance using SSH using Linux](https://www.clickittech.com/aws/connect-ec2-instance-using-ssh/)

[How to run the SSH server on a port other than 22](https://askubuntu.com/questions/264046/how-to-run-the-ssh-server-on-a-port-other-than-22)

### Ervaren problemen
1. Bad permissions van mijn .pem file. Opzoeken hoe permissions veranderen. chmod 400 commando.
2. Ik kwam alsnog niet binnen op de VM. Schijnt dus dat ik de juiste ssh portnr. moet declareren. -p commando.

### Resultaat
Hieronder zie je dat ik een "warning" krijg omdat mijn .pem file unprotected is.

<img width="" alt="bad permissions .pem file" src="https://github.com/techgrounds/techgrounds-JarBanf/blob/main/00_includes/01_Linux/w1_3_setting_up1.png?raw=true">
<br/><br/><br/>


Met `chmod 400 naampemfile.pem` verander ik de permissions waardoor alleen ik als user dit bestand kan lezen (read-en). Je ziet ook na het chmod-en dat alleen de user een 'r' heeft, vergeleken met vóór het chmod-en. Zie hieronder.

<img width="" alt="chmod 400 .pem file" src="https://github.com/techgrounds/techgrounds-JarBanf/blob/main/00_includes/01_Linux/w1_3_setting_up2.png?raw=true">
<br/><br/><br/>

Ik heb alsnog geen toegang tot de server omdat ik niet declareer welke port nummer ik nodig heb op de VM. Na deze te declareren is het mij gelukt om in te loggen. Zie hieronder.

<img width="" alt="ssh-en naar vm met portnummer" src="https://github.com/techgrounds/techgrounds-JarBanf/blob/main/00_includes/01_Linux/w1_3_setting_up3.png?raw=true">
<br/>
