#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http
import zlib


def sniffer(interface):
    scapy.sniff(iface=interface, store=False, prn=proc_sniffed_pack)

def proc_sniffed_pack(pack):
    if pack.haslayer(http.HTTPRequest):
        if pack.haslayer(scapy.IP):
            src_ip = pack[scapy.IP].src
            dst_ip = pack[scapy.IP].dst
            src_port = pack[scapy.TCP].sport
            dst_port = pack[scapy.TCP].dport
            print(f"IP: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")


        method = pack[http.HTTPRequest].Method.decode()
        url = (pack[http.HTTPRequest].Host + pack[http.HTTPRequest].Path).decode()
        print(f"[{method}] {url}")


        fields = pack[http.HTTPRequest].fields
        print("HTTP Fields: ", fields)


        if pack.haslayer(scapy.Raw):
            raw_data = pack[scapy.Raw].load
            print("Raw Data: (hex)", raw_data.hex())
            try:
                print("Raw data (text): ", raw_data.decode("utf-8"))
            except UnicodeDecodeError:
                print("Ras-w data is not text (possibly binary or encrypted)")
                if "Content-Encoding" in fields:
                    print("Data is compressed (e.g., gzip)")
                    try:
                        decompressed = zlib.decompress(raw_data)
                        print("Decompressed data (text): ", decompressed.decode("utf-8"))
                    except zlib.error:
                        print("Failed to decompress (not gzip or corrupted)")
                elif dst_port == 443:
                    print("Likely HTTPS traffic (encrypted)")
                else:
                    print("Possibly binary data or misidentified packet")


sniffer('Wi-Fi')
