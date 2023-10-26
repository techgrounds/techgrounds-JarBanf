# File permissions


## Key-terms
1. 

## Opdracht
### Gebruikte bronnen
1. [File Permissions in Linux / Unix: How to Read, Write & Change?](https://www.guru99.com/file-permissions.html)
2. 

### Ervaren problemen
1. 

### Resultaat
1. Het teksbestand die ik heb gemaakt heet `testpermission.txt`. <br> 
`Owner` is `jared_`.<br> 
`Group` is `jared_`.<br> 
`Owner` heeft `read/write` permissions.<br> 
`Group` heeft `read/write` permissions.<br> 
`Others` hebben alleen `read` permissions.

2. Om het bestand executable te maken voor de user heb ik de `chmod 764 testpermission.txt` commando nodig.

3. De `read` en `write` permissions verwijderen voor `group` en `others` doe ik met de `chmod 700 testpermission.txt` commando.<br> 
De `user` kan nog wel het bestand lezen.

4. De owner van het bestand te veranderen naar een ander user doe ik met de `sudo chown jared2_ testpermission.txt` commando.<br>
Alleen met `sudo` kan jared_ nog het bestand lezen.

5. De group ownership verander ik met de `sudo chgrp admin testpermission.txt` commando.