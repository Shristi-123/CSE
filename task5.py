from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto

        
        protocol = {6: "TCP", 17: "UDP"}.get(proto, str(proto))

        print(f"\n[ {datetime.now().strftime('%H:%M:%S')} ] {protocol} Packet")
        print(f"From: {src_ip} --> To: {dst_ip}")

        if Raw in packet:
            data = packet[Raw].load
            print(f"Payload: {data[:50]!r}")  

def main():
    print("Starting packet sniffer (Press Ctrl+C to stop)...")
    sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    main()
