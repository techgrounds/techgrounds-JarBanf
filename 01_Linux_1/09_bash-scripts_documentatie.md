# Bash Scripts
[Geef een korte beschrijving van het onderwerp]

## Key-terms
1. **PATH variable**: is een omgevingsvariabele die een geordende lijst met paden bevat waarnaar Linux zal zoeken naar uitvoerbare bestanden bij het uitvoeren van een opdracht. Het gebruik van deze paden betekent dat we geen absoluut pad hoeven op te geven bij het uitvoeren van een opdracht.<br> 
Als we bijvoorbeeld Hallo, wereld! in Bash willen printen kan het commando `echo` worden gebruikt in plaats van `/bin/echo`, zolang /bin zich in PATH bevindt.
2. **HTTPd**: Hypertext Transfer Protocol daemon. Het is een softwareprogramma dat gewoonlijk als proces op de achtergrond draait en de rol speelt van een server in een client-servermodel met behulp van de HTTP- en/of HTTPS-netwerkprotocol(len).

## Opdracht
### Gebruikte bronnen
1. [httpd](https://en.wikipedia.org/wiki/Httpd)
2. [Adding a Path to the Linux PATH Variable](https://www.baeldung.com/linux/path-variable)
3. [How to Write a Bash Script: A Simple Bash Scripting Tutorial](https://www.datacamp.com/tutorial/how-to-write-bash-script-tutorial)
4. [How To Install the Apache Web Server on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04)

### Ervaren problemen
1. Hoe voeg ik een nieuwe directory aan de PATH variable?
2. Hoe schrijf ik een script?
3. Welke script heb ik nodig om een lijn van tekst toe te voegen aan een bestand wanneer de script wordt ge-execute?
4. Wat zijn de commando's om de httpd package te installeren, activeren, enable-en en de status van op te vragen?

### Resultaat
1. Met de export commando kan ik een nieuwe directory toevoegen in de PATH variable. Met deze commando voeg ik **tijdelijk** een nieuwe directory toe. Zodra ik een nieuwe shell open, ben ik deze toevoeging kwijt.<br> 
`export PATH=$PATH:/home/jared_/scripts`

2. In de scripts directory heb ik een `addline.sh` bestand gemaakt. Hierin staat een commando dat een lijn toevoegd in `addline.txt`.<br> 
`echo "Wanneer addline.sh word ge-execute, wordt dit lijn aangemaakt in dit bestand" >> addline.txt`

3.  Bij het executen van `addline.sh` wordt een lijn toegevoegd in addline.txt.

4. In de script directory heb ik een `setuphttpd.sh` bestand gemaakt. Hierin heb ik de commando's gezet die nodig zijn om Apache web server te installeren, activeren, enable-en en de status ervan uit te printen in de terminal.<br> 
`sudo apt install -y apache2` -> installeert, activeert en enabled de Apache web server. De `-y` zorgt ervoor dat er autmatisch "yes" wordt beantwoord op de vragen.<br> 
`sudo systemctl status apache2` -> geeft de status van Apache web server aan in de terminal.

5. 