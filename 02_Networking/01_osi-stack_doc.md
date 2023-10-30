# OSI Stack
- OSI model en zijn functies
- TCP/IP model

**OSI model en zijn functies**  
OSI staat voor Open Systems Interconnection. Het is een architectuur met zeven lagen, waarbij elke laag een specifieke functionaliteit moet vervullen. Al deze zeven lagen werken samen om de gegevens van de ene persoon naar de andere over de hele wereld te verzenden.

<u>Wat is het OSI-model?</u>  
Het OSI-model, gecreëerd in 1984 door ISO, is een referentiekader dat het proces van gegevensoverdracht tussen computers uitlegt. Het is verdeeld in zeven lagen die samenwerken om gespecialiseerde netwerkfuncties uit te voeren, waardoor een meer systematische benadering van netwerken mogelijk is.

![OSI model](/02_Networking/images/01_osi-stack1-1.png)<br>

<u>Wat zijn de 7 lagen van het OSI-model?</u>  
Het OSI-model bestaat uit zeven abstractielagen, gerangschikt in top-down volgorde:
1. Physical Layer
2. Data Link Layer
3. Network Layer
4. Transport Layer
5. Session Layer
6. Presentation Layer
7. Application Layer

![osi model in a nutshell](/02_Networking/images/01_osi-stack1-2.png)<br>

<u>Meer informatie over de layers en wat hun functies zijn, lees je [hier](https://www.geeksforgeeks.org/open-systems-interconnection-model-osi/).</u><br><br>

**TCP/IP model**  
Staat voor Transmission Control Protocol/Internet Protocol. Het TCP/IP-model is een beknopte versie van het OSI-model. Het bevat vier lagen, in tegenstelling tot de zeven lagen in het OSI-model.

Het aantal lagen wordt soms vijf of vier genoemd. De fysieke laag en de datalinklaag worden in de verwijzing naar vier lagen als één enkele laag aangeduid als de ‘fysieke laag’ of ‘netwerkinterfacelaag’. 

<u>Wat doet TCP/IP?</u>  
Het belangrijkste werk van TCP/IP is het overbrengen van gegevens van een computer van het ene apparaat naar het andere. De belangrijkste voorwaarde van dit proces is dat de gegevens betrouwbaar en nauwkeurig zijn, zodat de ontvanger dezelfde informatie ontvangt als de afzender. Om ervoor te zorgen dat elk bericht zijn eindbestemming nauwkeurig bereikt, verdeelt het TCP/IP-model de gegevens in pakketten en combineert deze aan de andere kant, wat helpt bij het handhaven van de nauwkeurigheid van de gegevens tijdens de overdracht van het ene uiteinde naar het andere uiteinde.

<u>Wat is het verschil tussen TCP en IP?</u>  
TCP en IP zijn verschillende protocollen van computernetwerken. Het fundamentele verschil tussen TCP (Transmission Control Protocol) en IP (Internet Protocol) zit in de overdracht van gegevens. In eenvoudige woorden: IP vindt de bestemming van de e-mail en TCP heeft het werk om de e-mail te verzenden en te ontvangen. UDP is een ander protocol waarvoor geen IP nodig is om met een andere computer te communiceren. IP is alleen vereist voor TCP. Dit is het fundamentele verschil tussen TCP en IP.  

![verchil TCP/IP en OSI model](/02_Networking/images/01_osi-stack2-1.png)<br>

<u>Hoe werkt het TCP/IP-model?</u> 
Wanneer we iets via internet willen verzenden met behulp van het TCP/IP-model, verdeelt het TCP/IP-model de gegevens in pakketten aan de kant van de afzender en moeten dezelfde pakketten aan de kant van de ontvanger opnieuw worden gecombineerd om dezelfde gegevens te vormen. Dit zorgt ook ervoor dat de nauwkeurigheid van de gegevens behouden blijft. Het TCP/IP-model verdeelt de gegevens in een procedure met vier lagen, waarbij de gegevens eerst in één volgorde naar deze laag gaan en vervolgens weer in omgekeerde volgorde om op dezelfde manier te worden georganiseerd aan de kant van de ontvanger.

<u>Lagen van het TCP/IP-model</u>  
1. Application Layer
2. Transport Layer(TCP/UDP)
3. Network/Internet Layer(IP)
4. Data Link Layer (MAC)
5. Physical Layer

De schematische vergelijking van het TCP/IP- en OSI-model is als volgt:  

![vergelijking TCP/IP](/02_Networking/images/01_osi-stack2-2.png)<br>

<u>Meer informatie over de layers en wat hun functies zijn, lees je [hier](https://www.geeksforgeeks.org/tcp-ip-model/).</u><br><br>

## Key-terms


## Opdracht
### Gebruikte bronnen
- [What is OSI Model? – Layers of OSI Model](https://www.geeksforgeeks.org/open-systems-interconnection-model-osi/)
- [TCP/IP Model](https://www.geeksforgeeks.org/tcp-ip-model/)

### Ervaren problemen


### Resultaat

