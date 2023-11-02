# Subnetting
[Geef een korte beschrijving van het onderwerp]

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht
### Gebruikte bronnen
- [How to Design a Basic Subnet in 9 Minutes](https://www.youtube.com/watch?v=SBYNeGIng6I)
- [Subnetting Mastery](https://www.practicalnetworking.net/stand-alone/subnetting-mastery/)
- [IP Subnet Calculator](https://www.calculator.net/ip-subnet-calculator.html)

### Ervaren problemen
- Niet per se een probleem. Maar ik had moeite met visualiseren van de architectuur en of het echt klopt met real world situaties. Uiteindelijk gaat het om het kunnen subnetten en de juiste subnet hanteren.

### Resultaat
1. **Maak een netwerkarchitectuur die voldoet aan de volgende eisen:**
- **1 subnet dat alleen van binnen het LAN bereikbaar is. Dit subnet moet minimaal 15 hosts kunnen plaatsen.**
- **1 subnet dat internet toegang heeft via een router met NAT-functionaliteit. Dit subnet moet minimaal 30 hosts kunnen plaatsen (de 30 hosts is exclusief de router).**
- **1 subnet met een network gateway naar het internet. Dit subnet moet minimaal 5 hosts kunnen plaatsen (de 5 hosts is exclusief de internet gateway).**

Hieronder zie je een visualisatie van mijn netwerkarchitectuur.  
- De private subnet 10.0.0.80 is alleen bereikbaar van binnen het LAN. Eis is minimaal 15 hosts. Met ruimte voor groei kan deze subnet max 30 hosts hebben.  
- De private subnet 10.0.0.16 heeft internet toegang via een router met NAT-functionaliteit. Eis is minimaal 30 hosts. Met ruimte voor groei kan deze subnet max 62 hosts hebben.  
- De public subnet 10.0.0.0 heeft internet toegang via een netwerk gateway. Eis is minimaal 5 hosts. Met ruimte voor groei kan deze subnet max 14 hosts hebben.

![netwerkarchitectuur](/02_Networking/images/06_subnetting1-1.png)<br><br>

Hieronder is te zien welk deel ik van 10.0.0.24 heb gebruikt, en welk deel nog beschikbaar is.

![netwerkarchitectuur](/02_Networking/images/06_subnetting1-2.png)<br><br>