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

### Resultaat
- **Design a network architecture for the above use case.**
- **Explain your design decisions.**

Hieronder zie je mijn ontwerk van de netwerk architectuur.

![netwerkarchitectuur](/02_Networking/images/07_networking-case-study1-1.png)<br><br>

Het netwerk heb ik verdeeld in drie zones. Twee interne zones en één DMZ (demilitarized zone).  
Het doel van een DMZ is om een ​​extra beveiligingslaag toe te voegen aan het lokale netwerk van een organisatie. Een beschermd en bewaakt netwerk dat zich buiten het interne netwerk bevindt. Het internet heeft toegang tot wat zichtbaar is in de DMZ, terwijl de rest van het netwerk van de organisatie veilig achter een firewall zit.

In de DMZ heb ik de webserver (webshop) en database (server met login credentiels) geplaatst. Iemand (een potentiële klant of hacker) komt vanuit het internet ons netwerk binnen. De firewall blokkeert of leidt dit verkeer om naar de DMZ. Verder zal dit binnenkomende verkeer geen toegang hebben tot het interne netwerk.

