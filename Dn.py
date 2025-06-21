inmutable_system_tcp_udp_dns.py

Sistema Inmutable de Conexión TCP/UDP/DNS - Protección IA

import socket import json import time import hashlib import logging

logging.basicConfig(level=logging.INFO)

Configuraciones

DNS_SERVERS = ["8.8.8.8", "1.1.1.1"] TCP_TARGET = ("example.com", 80) UDP_TARGET = ("8.8.8.8", 53)

def hash_integridad(data): return hashlib.sha256(data.encode()).hexdigest()

def dns_check(): try: socket.gethostbyname("google.com") logging.info("DNS OK") except: logging.warning("Fallo DNS")

def tcp_check(): try: with socket.create_connection(TCP_TARGET, timeout=5): logging.info("TCP OK") except: logging.warning("Fallo TCP")

def udp_check(): try: sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) sock.sendto(b"\x00", UDP_TARGET) logging.info("UDP Enviado") sock.close() except: logging.warning("Fallo UDP")

def loop_eterno(): while True: dns_check() tcp_check() udp_check() payload = json.dumps({ "timestamp": time.time(), "status": "ok", "integridad": hash_integridad("FernandoIA") }) logging.info("Payload: %s", payload) time.sleep(10)

if name == "main": loop_eterno()

