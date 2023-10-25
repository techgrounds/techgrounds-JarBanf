# User & Groups
Linux heeft users, net zoals in Windows en MacOS. Alle users hebben hun eigen home-directory. Users kunnen ook onderdeel zijn van groups. Er is een speciaal user die "root" heet. Hij heeft toegang om alles te doen.

Om tijdelijk toegang te krijgen tot de root-permissions, kan ik `sudo` gebriuiken vóór de commando's, maar alleen als ik dat mag.

Sommige acties eisen specifieke permissions zoals de root-permissions.

Users, passwords en groups zijn allemaal opgeslagen in verschillende bestanden in het systeem.

## Key-terms
1. 

## Opdracht
### Gebruikte bronnen
1. [How to Create Users in Linux (useradd Command)](https://linuxize.com/post/how-to-create-users-in-linux-using-the-useradd-command/)
2. [How to Add User to Sudoers in Ubuntu](https://linuxize.com/post/how-to-add-user-to-sudoers-in-ubuntu/)
3. [Where are the passwords of the users located in Linux?](https://www.cyberciti.biz/faq/where-are-the-passwords-of-the-users-located-in-linux/)
4. [How To View System Users in Linux on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-view-system-users-in-linux-on-ubuntu)

### Ervaren problemen
1. Commando's opzoeken.

### Resultaat
1. Nieuwe gebruiker aanmaken die onderdeel is van `admin`-group.<br>
`sudo useradd -g users -G admin jared2_`

2. De nieuwe user een password geven.<br>
`sudo passwd jared2_`

3. De nieuwe user toevoegen aan de `sudo`-group. Hierdoor heeft hij `sudo`-rechten.<br>
`sudo usermod -aG sudo jared2_`

4. Bestand waar de users worden bewaard is `/etc/passwd`.<br> Bestand waar de passwords worden bewaard is `/etc/shadow`.<br>
Bestand waar de groups worden bewaard is `/etc/group`.<br>