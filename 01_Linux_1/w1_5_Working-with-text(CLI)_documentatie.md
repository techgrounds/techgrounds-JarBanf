# Working with text (CLI)


## Key-terms
1. **|** (pipe): kan gebruikt worden om de output van een commando als input te gebruiken van een ander commando.

## Opdracht
### Gebruikte bronnen
1. [echo command in Linux with Examples](https://www.geeksforgeeks.org/echo-command-in-linux-with-examples/)
2. [Grep Command in Linux/Unix with Examples](https://www.javatpoint.com/linux-grep)

### Ervaren problemen
1. Zat vast met het vinden van de commando om een zin uit een tekst bestand te halen die een bepaald woord bevat.
2. Ook was ik in de war omdat je de `grep` commando met én zonder "`|`" kan gebruiken.

### Resultaat
Gebruikte commando's:

`echo "Ik ben in opleiding bij Techgrounds." >> mytextfile.txt`.

`cat mytextfile.txt | grep Techgrounds` óf `grep Techgrounds mytextfile.txt`.

`cat mytextfile.txt | grep Techgrounds > newtextfile.txt` óf `grep Techgrounds mytextfile.txt > newtextfile.txt`.

<img width="" alt="filteren uit tekstbestand met grep-commando" src="https://github.com/techgrounds/techgrounds-JarBanf/blob/main/00_includes/01_Linux/w1_4_files-directories4.png?raw=true">
<br/><br/><br/>
