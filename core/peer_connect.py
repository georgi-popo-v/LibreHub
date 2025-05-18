# core/peer_connect.py

import socket

def peer_connect(ip: str, port: int = 8000):
    try:
        print(f"[🔗] Опит за свързване с {ip}:{port}...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((ip, port))
        print(f"[✅] Успешно свързване с {ip}:{port}")
        s.close()
    except Exception as e:
        print(f"[❌] Неуспешно свързване: {e}")

