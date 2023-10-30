# Processes
In Linux wordt een proces gestart telkens wanneer een toepassing wordt gestart, een programma wordt uitgevoerd of een opdracht wordt uitgevoerd. Elk programma of commando in Linux creëert slechts één proces, maar een applicatie kan daarentegen meerdere processen initiëren om verschillende taken te vervullen.

## Key-terms
1. **Telnet**: Telnet is een oud netwerkprotocol dat wordt gebruikt om verbinding te maken met externe systemen via een TCP/IP -netwerk. Telnet is geen veilig protocol en wordt daarom NIET AANBEVOLEN!. Dit komt omdat gegevens die via het protocol worden verzonden, niet-versleuteld zijn en door hackers kunnen worden onderschept. In plaats van telnet te gebruiken, is SSH een protocol dat meer de voorkeur verdient, dat gecodeerd en veiliger is.
2. **PID**: de process ID is een unieke identificatie die aan elk actief proces wordt toegewezen.

## Opdracht
### Gebruikte bronnen
1. [Telnet Command Usage in Linux/Unix](https://www.digitalocean.com/community/tutorials/telnet-command-linux-unix)
2. [What is a Process in Linux/Unix?](https://www.scaler.com/topics/linux-process/)
3. [Using Telnet in Linux](https://www.baeldung.com/linux/telnet)
4. [Ps Command in Linux (List Processes)](https://linuxize.com/post/ps-command-in-linux/#)

### Ervaren problemen
1. Is telnet uberhaupt geinstalleerd op de linux machine?
2. Hoe start ik telnet?
3. Hoe check ik de status/info van telnet?
4. Hoe stop ik telnet?
5. Hoe check ik of telnet inderdaad gestopt is?


### Resultaat
1. Installeer telnet.<br> 
`sudo apt-get install telnetd`

<img width="" alt="install telnet" src="https://github.com/techgrounds/techgrounds-JarBanf/blob/main/00_includes/01_Linux/w1_8_processes1.png?raw=true">
<br/><br/>


2. Check of telnet al aan staat.<br> 
`systemctl status inetd`.<br> 
Na het installeren staat telnet al active.<br> 
Ik zie gelijk ook de PID van telnet, 7266.<br> 
En hoeveel memory het gebruikt, 1004.0K.

<img width="" alt="check status telnet" src="https://github.com/techgrounds/techgrounds-JarBanf/blob/main/00_includes/01_Linux/w1_8_processes2.png?raw=true">
<br/><br/>

3. Stop telnet.<br> 
`sudo systemctl stop inetd` of `sudo kill 7266`<br> 
En check of telnet inderdaad gestopt is.<br> 
`systemctl status inetd`<br> 
`ps auxf`

<img width="" alt="check status telnet" src="https://github.com/techgrounds/techgrounds-JarBanf/blob/main/00_includes/01_Linux/w1_8_processes3.png?raw=true">
<br/><br/>