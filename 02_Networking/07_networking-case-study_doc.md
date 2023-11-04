# Networking Case Study
In this case study you take the role of a network administrator setting up a network in the new office of a small e-commerce company. Of course there are multiple ways to go about this problem, but this company has specifically said that network security is extremely important to them.

The office contains the following devices:
- A web server where our webshop is hosted
- A database with login credentials for users on the webshop
- 5 workstations for the office workers
- A printer
- An AD server
- A file server containing internal documents

## Key-terms
- **DMZ**: a DMZ (demilitarized zone) network functions as a subnetwork containing an organization's exposed, outward-facing services. It acts as the exposed point to an untrusted network, commonly the internet.
## Opdracht
### Gebruikte bronnen
- [Beer:30 - Network Architecture Review](https://www.youtube.com/watch?v=oopkClg1kxM)
- [What is a DMZ network?](https://www.barracuda.com/support/glossary/dmz-network)

### Ervaren problemen
Geen

### Resultaat
- **Design a network architecture for the above use case.**
- **Explain your design decisions.**

Hieronder zie je mijn ontwerk van de netwerk architectuur.

![netwerkarchitectuur](/02_Networking/images/07_networking-case-study1-1.png)<br><br>

Het netwerk heb ik verdeeld in sub-netwerken. Twee interne sub-netwerken en één DMZ (demilitarized zone) sub-netwerk.  
Het doel van een DMZ is om een ​​extra beveiligingslaag toe te voegen aan het lokale netwerk van een organisatie. Een beschermd en bewaakt netwerk dat zich buiten het interne netwerk bevindt. Het internet heeft toegang tot wat zichtbaar is in de DMZ, terwijl de rest van het netwerk van de organisatie veilig achter een firewall zit.

In de DMZ heb ik de webserver (webshop) en database (server met login credentiels) geplaatst. Verkeer (een potentiële klant of hacker) komt vanuit het internet ons netwerk binnen. De firewall blokkeert of leidt dit verkeer om naar de DMZ. Verder zal dit binnenkomende verkeer geen toegang hebben tot het interne netwerk.

Intern heb ik een router geplaatst die het verkeer beheert tussen de twee interne sub-netwerken zowel met elkaar als met de firewall.

In één van de interne netwerk bevinden zich de file server en de active directory server. Deze servers met hoogwaardige data zijn alleen toegankelijk vanuit het interne netwerk. Ook hoeven ze niet toegankelijk te zijn voor iedereen binnen het netwerk. Ze zijn dus afgeschermd met hun eigen subnetwerk.

In de andere interne netwerk bevinden zich de workstations en printer. De apparaten binnen dit netwerk hebben toegang tot het internet maar zijn niet toegankelijk vanuit het internet.

In alle 3 sub-netwerken heb ik rekening gehouden met het aantal hosts die geplaatst moeten worden maar ook met toekomstige groei.  
Zo zijn er in de DMZ 6 bruikbare IP-adressen waarvan er nog 4 vrij zijn.
In de server sub-netwerk zijn er 6 bruikbare IP-adressen waarvan er nog 4 vrij zijn.
In het workstation sub-netwerk zijn er 14 IP-adressen waarvan er nog 8 vrij zijn.
