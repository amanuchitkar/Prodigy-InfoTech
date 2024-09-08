from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw, get_if_list

def packet_callback(packet):
    """
    Callback function to process and display packet information.
    
    :param packet: The captured network packet
    """
    print("\n[Packet Captured]")
    if IP in packet:
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
    if packet.haslayer(TCP):
        print(f"Protocol: TCP")
    elif packet.haslayer(UDP):
        print(f"Protocol: UDP")
    elif packet.haslayer(ICMP):
        print(f"Protocol: ICMP")
    if packet.haslayer(Raw):
        payload = packet[Raw].load
        print(f"Payload: {payload}")

def main():
    """
    Main function to start the packet sniffer.
    """
    print("Starting packet sniffer...")
    
    # List available interfaces to find the correct one
    interfaces = get_if_list()
    print("Available interfaces:", interfaces)
    
    # Choose the correct interface from the list
    iface = '\\Device\\NPF_Loopback'  # Example from available interfaces; try this or others listed
    if iface not in interfaces:
        print(f"Interface {iface} not found.")
        return
    
    # Start sniffing packets
    sniff(iface=iface, prn=packet_callback, store=0, count=10)

if __name__ == "__main__":
    main()
