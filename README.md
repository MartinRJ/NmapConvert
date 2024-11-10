# NmapConvert
Convert Nmap Output

Converts nmap default scan output into XML for importing into Metasploit's database.

Import the result in Metasploit with: db_import /tmp/nmap_results_converted.xml

Example Nmap input:

-----

nmap --scanflags SYN -D 192.168.217.5,192.168.218.23,ME -p- 192.168.216.0/21 --exclude 192.168.220.12,192.168.221.11,192.168.216.1 | tee stealthscan.txt  

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-09 03:23 UTC  
Nmap scan report for ip-192-168-217-1.local (192.168.217.1)  
Host is up (0.00077s latency).  
All 65535 scanned ports on ip-192-168-217-1.local (192.168.217.1) are in ignored states.  
Not shown: 65535 filtered tcp ports (no-response)  
MAC Address: 02:1C:2E:4B:AA:4F (Unknown)  

Nmap scan report for ip-192-168-217-6.local (192.168.217.6)  
Host is up (0.0029s latency).  
Not shown: 65534 filtered tcp ports (no-response)  
PORT    STATE SERVICE  
636/tcp open  ldapssl  
MAC Address: 02:10:29:B9:01:4D (Unknown)  

Nmap scan report for ip-192-168-217-8.local (192.168.217.8)  
Host is up (0.0015s latency).  
Not shown: 65534 filtered tcp ports (no-response)  
PORT     STATE SERVICE  
5671/tcp open  amqps  
MAC Address: 02:3A:B3:52:14:DF (Unknown)  

Nmap scan report for ip-192-168-217-13.local (192.168.217.13)  
Host is up (0.0024s latency).  
Not shown: 65533 filtered tcp ports (no-response)  
PORT    STATE SERVICE  
80/tcp  open  http  
443/tcp open  https  
MAC Address: 02:48:32:9B:31:13 (Unknown)  

Nmap scan report for ip-192-168-217-100.local (192.168.217.100)  
Host is up (0.0026s latency).  
Not shown: 65531 filtered tcp ports (no-response)  
PORT     STATE SERVICE  
80/tcp   open  http  
443/tcp  open  https  
1433/tcp open  ms-sql-s  
3389/tcp open  ms-wbt-server  
MAC Address: 02:12:AD:3B:22:43 (Unknown)  

Nmap scan report for ip-192-168-218-41.local (192.168.218.41)  
Host is up (0.0042s latency).  
Not shown: 65533 filtered tcp ports (no-response)  
PORT    STATE SERVICE  
80/tcp  open  http  
443/tcp open  https  

Nmap scan report for ip-192-168-219-252.local (192.168.219.252)  
Host is up (0.0032s latency).  
Not shown: 65534 filtered tcp ports (no-response)  
PORT    STATE SERVICE  
443/tcp open  https  

Nmap scan report for ip-192-168-217-9.local (192.168.217.9)  
Host is up (0.0015s latency).  
Not shown: 65534 filtered tcp ports (no-response)  
PORT     STATE SERVICE  
5671/tcp open  amqps  
MAC Address: 02:2A:FB:52:28:43 (Unknown)  

Nmap done: 2045 IP addresses (100 hosts up) scanned in 9019.95 seconds
