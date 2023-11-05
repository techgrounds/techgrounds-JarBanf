# Network detection
Nmap is short for Network Mapper. It is an open-source Linux command-line tool that is used to scan IP addresses and ports in a network and to detect installed applications.

## Key-terms

## Opdracht
1. Scan the network of your Linux machine using nmap. What do you find?
2. Open Wireshark in Windows/MacOS Machine. Analyse what happens when you open an internet browser.

### Gebruikte bronnen
- [Nmap Command in Linux with Examples](https://www.geeksforgeeks.org/nmap-command-in-linux-with-examples/)
- [What is Nmap and How to Use it – A Tutorial for the Greatest Scanning Tool of All Time](https://www.freecodecamp.org/news/what-is-nmap-and-how-to-use-it-a-tutorial-for-the-greatest-scanning-tool-of-all-time/)
- [How to check your network connections on Linux](https://www.networkworld.com/article/3262045/checking-your-network-connections-on-linux.html)

### Ervaren problemen
Geen

### Resultaat
1. **Scan the network of your Linux machine using nmap. What do you find?**  
- nmap installeren.
```
sudo apt-get install nmap
```
- Met de commando `ip a` vind ik mijn private IP adres. En dat is `10.82.162.177/24`.

![ip a](/02_Networking/images/08_network-detection1-1.png)<br><br> 

- Met een basic scan van mijn private IP adres zie ik het volgende.
```
nmap 10.82.162.177
```
![nmap](/02_Networking/images/08_network-detection1-2.png)<br><br>

- Met een agresieve scan van mijn private IP adres zie ik het volgende.
```
nmap -A 10.82.162.177
```
![nmap -A](/02_Networking/images/08_network-detection1-3.png)<br><br>

- Met een basic scan van het hele 10.82.162.177 /24 subnet krijg informatie te zien van alle hosts binnen deze subnet. 
```
nmap 10.82.162.177/24
```
![nmap hele subnet](/02_Networking/images/08_network-detection1-4-1.png)
![nmap hele subnet](/02_Networking/images/08_network-detection1-4-2.png)<br><br>

- Nu dat ik kan zien welke hosts er allemaal actief zijn binnen de hele subnet kan ik kiezen om meer informatie te vinden van een bepaalde host. In dit geval een agresieve scan van `10.82.162.34`.
```
sudo nmap -A 10.82.162.34
```
![nmap hele subnet](/02_Networking/images/08_network-detection1-5.png)<br><br>

2. **Open Wireshark in Windows/MacOS Machine. Analyse what happens when you open an internet browser.**
- Ik heb eerst een 10 seconde capture gedaan van mijn WiFi interface zonder een browser open. Er is geen http protocol actief.

![capture zonder browser](/02_Networking/images/08_network-detection2-1.png)<br><br>

- Daarna een 10 seconde capture van mijn WiFi interface terwijl ik mijn browser opende en naar 2 verschillende website ging.  
Er is veel activiteit met tcp en http op port 80.

![capture met browser](/02_Networking/images/08_network-detection2-2.png)<br><br>