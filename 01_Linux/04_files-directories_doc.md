# Files & Directories
Linux gebruikt files en folder zoals wij gewend zijn met andere OS. Folders wordt in Linux directories genoemd. Wanneer ik een terminal opent, zal ik in de home-directory werken. Vanuit hier kan ik navigeren door het hele systeem met behulp van commando's.

## Key-terms
1. **OS**: Operating System, besturingssysteem in het Nederlands. Een besturingssysteem is een programma dat na het opstarten van een computer in het geheugen geladen wordt en de hardware aanstuurt. Het fungeert als een medium tussen de hardware en de computergebruiker.
2. **Nano**: Nano is een veelgebruikte tekstverwerker in Linux.

## Opdracht
### Gebruikte bronnen
1. [Besturingssysteem](https://nl.wikipedia.org/wiki/Besturingssysteem)
2. [How To Create A File In Linux: Touch, Cat, Echo, Printf Command](https://unstop.com/blog/how-to-create-a-file-in-linux)
3. [Linuxables: Introduction to the Nano Text Editor](https://www.linux.com/training-tutorials/linuxables-introduction-nano-text-editor/)
4. [Absolute vs Relative Path in Linux: What's the Difference?](https://linuxhandbook.com/absolute-vs-relative-path/)
5. [How to Get the Full Path of a File in Linux](https://www.geeksforgeeks.org/how-to-get-the-full-path-of-a-file-in-linux/)

### Ervaren problemen
1. Ik wist niet wat de commando was om een tekst bestand te creëren in linux.
2. En ook niet hoe tekst toe te voegen in een tekst bestand.
3. Wat is absolute path en wat is relative path?
4. Hoe vind ik de absolute path van een bestand of directory?

### Resultaat
Het is mij gelukt om met `mk dir` command een nieuw directory te maken. Met `touch` command een nieuwe lege tekst-bestand. En de `Nano` text editor te openen. Zie hieronder.

<img width="" alt="directory en text bestand creëren" src="https://github.com/techgrounds/techgrounds-JarBanf/blob/main/00_includes/01_Linux/w1_4_files-directories1.png?raw=true">
<br/><br/><br/>

In de Nano text editor wat tekst ingevuld en met `CTRL-x` het bestand op te slaan en uit de editor te gaan terug naar de terminal. Zie hieronder.

<img width="" alt="tekst toevoegen in bestand met nano text editor" src="https://github.com/techgrounds/techgrounds-JarBanf/blob/main/00_includes/01_Linux/w1_4_files-directories2.png?raw=true">
<br/><br/><br/>

Met de `cat` command kan ik de inhoud van de tekst-bestand tonen in de terminal.

<img width="" alt="met cat commando inhoud tonen" src="https://github.com/techgrounds/techgrounds-JarBanf/blob/main/00_includes/01_Linux/w1_4_files-directories3.png?raw=true">
<br/><br/><br/>

Vanuit de `techgrounds`-directory kan ik door middel van relative path met de `cd ..` commando naar de parent-directory gaan. En ook door middel van absolute path met de `/home/jared_` commando naar de parent-directory gaan.

<img width="" alt="relative path en absolute path" src="https://github.com/techgrounds/techgrounds-JarBanf/blob/main/00_includes/01_Linux/w1_4_files-directories4.png?raw=true">
<br/><br/><br/>