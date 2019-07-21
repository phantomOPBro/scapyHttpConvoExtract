from scapy.all import *
data = "attack.pcap"
power = rdpcap(data)

os.system("tshark -r attack.pcap -Y http -w attack.pcap")
httpSessions = power.sessions()

for session in httpSessions:
    for packet in httpSessions[session]:
        try:
            if packet[TCP].dport == 80 or packet[TCP].sport == 80:
                print packet[TCP].payload
        except:
            pass
