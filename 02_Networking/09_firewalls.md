# Firewalls
Een firewall is een computernetwerk beveiligingssysteem dat internetverkeer naar, van, en binnen een privé netwerk beperkt.  
Deze software of hardware-software eenheid functioneert door het selectief blokkeren of toestaan van datapakketten. In de praktijk worden er zowel software als hardware firewall opgenomen in een privé netwerk.

<ins>Software firewall</ins>  
Een software firewall is een soort computersoftware dat op een computer/server draait. Zijn hoofdfunctie is de computer/server beveiligen tegen pogingen van buitenaf om toegang of controle te krijgen van het systeem. Een software firewall kan ook ingesteld worden om te controleren op verdacht uitgaand verzoeken.

<ins>Hardware firewall</ins>  
Een hardware firewall is een fysiek apparaat dat firewall taken uitvoert. Het kan een computer zijn maar ook een toegewijd apparaat dat als een firewall dient. Hardware firewall bevindt zich in het netwerk tussen het internet en privé netwerk.

Firewalls kunnen ook verschillende karakter hebben, zoals stateless en statefull.

<ins>Stateless firewall</ins>  
Een stateless firewall begrijpt niet wat de staat zijn van verbindingen. Die ziet een verzoek en het antwoord op die verzoek als twee aparte verbindingen. Er moet dus twee aparte regels geconfigureerd worden. Één voor het verzoek en één voor het antwoord op die verzoek.

<ins>Statefull firewall</ins>  
Een statefull firewall heeft wat meer intelligentie om te kunnen identificeren dat een verzoek en het antwoord op die verzoek met elkaar gerelateerd zijn.  Er hoeft dus maar één regel geconfigureerd te worden voor het verzoek. Het antwoord op dit verzoek wordt automatisch toegestaan.


## Key-terms
 

## Opdracht
1. Installeer een webserver op je VM.
2. Bekijk de standaardpagina die met de webserver geïnstalleerd is via je browser op je pc/laptop.
3. Stel de firewall zo in dat je webverkeer blokkeert, maar wel ssh-verkeer toelaat.
4. Controleer of de firewall zijn werk doet.

### Gebruikte bronnen
- [What is a Firewall?](https://www.youtube.com/watch?v=kDEX1HXybrU)
- [What is a firewall? Definition and explanation](https://www.kaspersky.com/resource-center/definitions/firewall)
- [Difference between Hardware Firewall and Software Firewall](https://www.geeksforgeeks.org/difference-between-hardware-firewall-and-software-firewall/)
- [Stateful vs Stateless Firewalls - You NEED to know the difference](https://www.youtube.com/watch?v=rL4-vbsN35w)
- [Linux Security - UFW Complete Guide (Uncomplicated Firewall)](https://www.youtube.com/watch?v=-CzvPjZ9hp8)
- [How to Use UFW (Uncomplicated Firewall)](https://www.baeldung.com/linux/uncomplicated-firewall)

### Ervaren problemen
Geen

### Resultaat
1. **Installeer een webserver op je VM.**  
Geïnstalleerd en geactiveerd.

![apache2 actief](/02_Networking/images/09_firewalls1.png)<br><br>

2. **Bekijk de standaardpagina die met de webserver geïnstalleerd is via je browser op je pc/laptop.**  
De public IPv4 adddress van mijn webserver is `3.121.40.175` en de webport is `58015`.
```
http://3.121.40.175:58015/
```

![apache2 actief](/02_Networking/images/09_firewalls2.png)<br><br>

3. **Stel de firewall zo in dat je webverkeer blokkeert, maar wel ssh-verkeer toelaat.**

Het gewenste gedrag van de firewall is om inkomende verbindingen toe te laten alleen op eerder geautoriseerde poorten, en alle andere porten blokkeren. Daarom is de standaard policy “deny incoming traffic” en “allow outgoing traffic”. Dus het system kan verzoeken sturen naar de buitenwereld en antwoorden ontvangen. Tegelijkertijd blokkeert de firewall alle ongevraagde inkomende verbindingen.  
Dit doen we met 2 commando’s. 
```
sudo ufw default deny incoming
```
```
sudo ufw default allow outgoing
```
Om ervoor te zorgen dat ik ten aller tijden in de VM kan ssh-en zal ik een regel toevoegen om dat toe te staan.
```
sudo ufw allow "OpenSSH"
```
Met de volgende commando activeer ik de firewall
```
sudo ufw enable
```
We checken de status met het volgende commando.
```
sudo ufw status
```
![apache2 actief](/02_Networking/images/09_firewalls3.png)<br><br>
We zien dat de firewall alleen inkomende verkeer via SSH toestaat. Inkomende verkeer via HTTP is niet toegestaan.

4. **Controleer of de firewall zijn werk doet.**

![apache2 actief](/02_Networking/images/09_firewalls4.png)<br><br>