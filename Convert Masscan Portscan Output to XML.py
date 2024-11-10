import re
import xml.etree.ElementTree as ET
from datetime import datetime

def parse_masscan_output(file_path):
    """
    Parse the Masscan output file.
    """
    with open(file_path, 'r') as file:
        masscan_output = file.read()

    hosts_data = {}
    for line in masscan_output.splitlines():
        match = re.match(r"Discovered open port (\d+)/tcp on ([\d.]+)", line)
        if match:
            port = match.group(1)
            ip = match.group(2)
            if ip not in hosts_data:
                hosts_data[ip] = []
            hosts_data[ip].append(port)

    return [{"ip": ip, "ports": ports} for ip, ports in hosts_data.items()]

def create_masscan_xml(hosts_data, output_file_path):
    """
    Create an XML structure from the parsed Masscan data.
    """
    nmap_run = ET.Element("nmaprun", scanner="masscan", args="Converted from Masscan output",
                          start=str(int(datetime.now().timestamp())),
                          startstr=datetime.now().strftime("%c"),
                          version="1.3", xmloutputversion="1.04")

    for host in hosts_data:
        host_element = ET.SubElement(nmap_run, "host")
        ET.SubElement(host_element, "address", addr=host["ip"], addrtype="ipv4")
        ports_element = ET.SubElement(host_element, "ports")
        for port in host["ports"]:
            port_element = ET.SubElement(ports_element, "port", protocol="tcp", portid=port)
            state_element = ET.SubElement(port_element, "state", state="open")
            # Adding a generic service name since Masscan doesn't provide it
            service_element = ET.SubElement(port_element, "service", name="unknown")

    # Save the XML to a file
    tree = ET.ElementTree(nmap_run)
    tree.write(output_file_path, encoding="utf-8", xml_declaration=True)

# File paths
input_file_path = "/path/to/your/masscan_results.txt"  # Replace with your Masscan output file
output_file_path = "/path/to/output/masscan_results_converted.xml"  # Replace with your desired output path

# Convert Masscan text output to XML
hosts_data = parse_masscan_output(input_file_path)
create_masscan_xml(hosts_data, output_file_path)

print(f"Masscan XML output saved to {output_file_path}")
