import re
import xml.etree.ElementTree as ET
from datetime import datetime

# Load the Nmap output file
def parse_nmap_output(file_path):
    with open(file_path, 'r') as file:
        nmap_output = file.read()

    hosts_data = []
    current_host = None

    for line in nmap_output.splitlines():
        # Detect a new host section
        if line.startswith("Nmap scan report for"):
            if current_host:
                hosts_data.append(current_host)  # Save the previous host
            current_host = {"ip": re.search(r'\((.*?)\)', line).group(1), "ports": []}

        # Capture MAC Address
        elif "MAC Address" in line and current_host:
            mac_match = re.search(r"MAC Address: ([\w:]+)", line)
            if mac_match:
                current_host["mac"] = mac_match.group(1)

        # Capture open ports
        elif re.match(r"\d+/tcp\s+open\s+\S+", line) and current_host:
            port_match = re.match(r"(\d+)/tcp\s+open\s+(\S+)", line)
            if port_match:
                current_host["ports"].append({"port": port_match.group(1), "service": port_match.group(2)})

    # Add the last host if present
    if current_host:
        hosts_data.append(current_host)

    return hosts_data

def create_nmap_xml(hosts_data, output_file_path):
    # Create the XML structure
    nmap_run = ET.Element("nmaprun", scanner="nmap", args="Generated from nmap text output",
                          start=str(int(datetime.now().timestamp())),
                          startstr=datetime.now().strftime("%c"),
                          version="7.94", xmloutputversion="1.04")

    for host in hosts_data:
        host_element = ET.SubElement(nmap_run, "host")
        ET.SubElement(host_element, "address", addr=host["ip"], addrtype="ipv4")
        if "mac" in host:
            ET.SubElement(host_element, "address", addr=host["mac"], addrtype="mac")
        ports_element = ET.SubElement(host_element, "ports")
        for port in host["ports"]:
            port_element = ET.SubElement(ports_element, "port", protocol="tcp", portid=port["port"])
            state_element = ET.SubElement(port_element, "state", state="open")
            service_element = ET.SubElement(port_element, "service", name=port["service"])

    # Save the XML to a file
    tree = ET.ElementTree(nmap_run)
    tree.write(output_file_path, encoding="utf-8", xml_declaration=True)

# File paths
input_file_path = "/path/to/your/nmap_results.txt"  # Replace with the path to your Nmap text file
output_file_path = "/path/to/output/nmap_results_converted.xml"  # Replace with your desired output path

# Convert Nmap text output to XML
hosts_data = parse_nmap_output(input_file_path)
create_nmap_xml(hosts_data, output_file_path)

print(f"Nmap XML output saved to {output_file_path}")
