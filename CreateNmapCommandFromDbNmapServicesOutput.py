#Script to create nmap command from Metasploit's db_nmap "services -o filename.txt" output

import csv

# Path to CSV file
input_file = "open_ports.txt"

# Listes for hosts and ports
hosts = set()
ports = set()

# Read CSV-file
with open(input_file, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["state"].strip().lower() == "open":  # Only consider open ports.
            hosts.add(row["host"].strip())
            ports.add(row["port"].strip())

# Kombinierte Strings für Hosts und Ports
host_list = " ".join(hosts)  # Separate hosts by space
port_list = ",".join(sorted(ports))  # Sort ports and separate them by comma

# Generate db_nmap-command
db_nmap_command = f"db_nmap -sV -p{port_list} {host_list}"
print("Generated db_nmap command:")
print(db_nmap_command)
