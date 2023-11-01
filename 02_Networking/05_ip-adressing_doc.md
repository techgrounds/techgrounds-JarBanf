# IP Adressing
**IP address**:  
The internet needs a way to differentiate between different computers, routers, and websites. An IP (Internet Protocol) address is a unique address that identifies a device on the internet or a local network.

**Two versions of IP addresses**  
- IPv4
- IPv6

<ins>IPv4</ins>  
IPv4 is actually the first version of IP to be used. It uses a 32-bit address that consist of a string of numbers separated by periods. This 32-bit address space provides almost 4.3 billion unique addresses, though some IP blocks are reserved for special uses.  
IPv4 addresses are expressed as a set of four numbers. Each number in the set can range from 0 to 255. So, the full IPv4 addressing range goes from 0.0.0.0 to 255.255.255.255.  
For example: 192.168.10.150

<ins>IPv6</ins>  
The IPv6 is a newer version of IP that uses a 128-bit address format that consist of a string of both numbers and letters seperated by periods. IPv6 supports 1,028 times more IP addresses than IPv4.  
IPv6 addresses are expresses as a set of 8 hexadecimal values. Each hexadecimal value in the set can range from 0000 to FFFF. So the full IPv6 adressing range goes from 0000.0000.0000.0000.0000.0000.0000.0000 to FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF.  
For example: 3002:0bd6:0000:0000:0000:ee00:0033:6778

**Types of IP addresses**
- Private IP addresses
- Public IP addresses

<ins>Private IP addresses</ins>  
Every device that connects to your internet network has a private IP address. Your router needs a way to identify these devices separately, and many items need a way to recognize each other. Therefore, your router generates private IP addresses that are unique identifiers for each device that differentiate them on the network.

<ins>Public IP addresses</ins>  
A public IP address is the primary address associated with your whole network. your public IP address is provided to your router by your ISP. Typically, ISPs have a large pool of IP addresses that they distribute to their customers. Your public IP address is the address that all the devices outside your internet network will use to recognize your network.

**Public IP addresses come in two forms**
- Dynamic
- Static

<ins>Dynamic IP addresses</ins>  
Dynamic IP addresses change automatically and regularly. ISPs buy a large pool of IP addresses and assign them automatically to their customers. Periodically, they re-assign them and put the older IP addresses back into the pool to be used for other customers. The rationale for this approach is to generate cost savings for the ISP. There are security benefits, too, because a changing IP address makes it harder for criminals to hack into your network interface.

<ins>Static IP addresses</ins>  
In contrast to dynamic IP addresses, static addresses remain consistent. Once the network assigns an IP address, it remains the same. Most individuals and businesses do not need a static IP address, but for businesses that plan to host their own server, it is crucial to have one. This is because a static IP address ensures that websites and email addresses tied to it will have a consistent IP address. Vital if you want other devices to be able to find them consistently on the web.

**NAT**  
NAT stands for network address translation. The idea of NAT is to allow multiple devices to access the Internet through a single public address. To achieve this, the translation of a private IP address to a public IP address is required. NAT is a process in which one or more local IP address is translated into one or more Global IP address and vice versa in order to provide Internet access to the local hosts. Also, it does the translation of port numbers. It masks the port number of the host with another port number, in the packet that will be routed to the destination. It then makes the corresponding entries of IP address and port number in the NAT table. NAT generally operates on a router or firewall. 

## Key-terms


## Opdracht
### Gebruikte bronnen
- [What is an IP Address – Definition and Explanation](https://www.kaspersky.com/resource-center/definitions/what-is-an-ip-address)
- [IPv4 vs IPv6: What’s The Difference Between the Two Protocols?](https://kinsta.com/blog/ipv4-vs-ipv6/)
- [Network Address Translation (NAT)](https://www.geeksforgeeks.org/network-address-translation-nat/)


### Ervaren problemen
Geen

### Resultaat
1. **Ontdek wat je publieke IP adres is van je laptop en mobiel op wifi. Zijn de adressen hetzelfde of niet? Leg uit waarom.**  
De publieke IP adres van mijn laptop en mobiele telefoon zijn hetzelfde. Mijn laptop en mobiele zijn verbonden met de router via een privé/lokaal netwerk. De router op zijn beurt zet ons privé IP adressen om in één publieke IP adres. Dit adres wordt bepaald en aan ons gegeven door ons ISP.

2. **Ontdek wat je privé IP adres is van je laptop en mobiel op wifi. Zijn de adressen hetzelfde of niet? Leg uit waarom.**  
De privé IP adres van mijn laptop en mobiele telefoon zijn verschillend. Deze apparaten zijn onderdeel van mijn privé netwerk. Elke apparaat heeft een unieke IP adres zodat ze binnen deze privé netwerk elkaar kunnen identificeren en met elkaar communiceren.

3. **Verander het privé IP adres van je mobiel naar dat van je laptop. Wat gebeurt er dan?**  
Mijn verbinding verbreekt.

4. **Probeer het privé IP adres van je mobiel te veranderen naar een adres buiten je netwerk. Wat gebeurt er dan?**  
Mijn verbinding verbreekt.