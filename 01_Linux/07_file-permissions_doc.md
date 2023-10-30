# File permissions
In Linux bepalen "file permissions", "attributes", and "ownership" het toegangsniveau dat de systeemprocessen en gebruikers hebben voor bestanden. Dit zorgt ervoor dat alleen geautoriseerde gebruikers en processen toegang hebben tot specifieke bestanden en mappen.

Het basismodel voor Linux-machtigingen werkt door elk systeembestand te associëren met een eigenaar en een groep en toegangsrechten toe te wijzen aan drie verschillende klassen gebruikers:

- De "file owner".
- De "group members".
- "Others (everybody else)".

Er zijn drie typen bestandsrechten van toepassing op elke gebruikersklasse:

- De "read permission".
- De "write permission".
- De "execute permission".

Met dit concept kunt u bepalen welke gebruikers het bestand kunnen lezen, naar het bestand kunnen schrijven of het bestand kunnen uitvoeren.

Voorbeeld van een "file permission".
```
-rw-r--r-- 12 user1 users
|[-][-][-]  - [---] [---]
| |  |  |   |   |     |
| |  |  |   |   |     +--------------> 7. Group
| |  |  |   |   +--------------------> 6. Owner
| |  |  |   +------------------------> 5. Alternate Access Method
| |  |  +----------------------------> 4. Others Permissions
| |  +-------------------------------> 3. Group Permissions
| +----------------------------------> 2. Owner Permissions
+------------------------------------> 1. File Type
```

## Key-terms
1. 

## Opdracht
### Gebruikte bronnen
1. [Understanding Linux File Permissions](https://linuxize.com/post/understanding-linux-file-permissions/)
2. [File Permissions in Linux / Unix: How to Read, Write & Change?](https://www.guru99.com/file-permissions.html)

### Ervaren problemen
Geen

### Resultaat
1. Het teksbestand die ik heb gemaakt heet `testpermission.txt`. <br> 
`Owner` is `jared_`.<br> 
`Group` is `jared_`.<br> 
`Owner` heeft `read/write` permissions.<br> 
`Group` heeft `read/write` permissions.<br> 
`Others` hebben alleen `read` permissions.

<img width="" alt="ls -l testpermission.txt" src="https://github.com/techgrounds/techgrounds-JarBanf/blob/main/00_includes/01_Linux/w1_7_file-permissions1.png?raw=true">
<br/><br/>

2. Om het bestand executable te maken voor de user heb ik de `chmod 764 testpermission.txt` commando nodig.

<img width="" alt="make executable" src="https://github.com/techgrounds/techgrounds-JarBanf/blob/main/00_includes/01_Linux/w1_7_file-permissions2.png?raw=true">
<br/><br/>

3. De `read` en `write` permissions verwijderen voor `group` en `others` doe ik met de `chmod 700 testpermission.txt` commando.<br> 
De `user` kan nog wel het bestand lezen.

<img width="" alt="change permissions" src="https://github.com/techgrounds/techgrounds-JarBanf/blob/main/00_includes/01_Linux/w1_7_file-permissions3.png?raw=true">
<br/><br/>

4. De `owner` van het bestand te veranderen naar een ander `user` doe ik met de `sudo chown jared2_ testpermission.txt` commando.<br>
Alleen met `sudo` kan `jared_` nog het bestand lezen.

<img width="" alt="change user ownership" src="https://github.com/techgrounds/techgrounds-JarBanf/blob/main/00_includes/01_Linux/w1_7_file-permissions4.png?raw=true">
<br/><br/>

5. De `group` ownership verander ik met de `sudo chgrp admin testpermission.txt` commando.

<img width="" alt="change group ownership" src="https://github.com/techgrounds/techgrounds-JarBanf/blob/main/00_includes/01_Linux/w1_7_file-permissions5.png?raw=true">
<br/><br/>