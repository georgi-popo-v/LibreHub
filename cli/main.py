# librehub/cli/main.py

import subprocess
import sys
import time
import socket
from core.peer_discovery import register_instance, start_discovery
from core.peer_connect import peer_connect
from core.qr_utils import generate_qr

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        print("Грешка при инсталиране на зависимости!")

def connect_by_input():
    addr = input("Въведи IP:PORT или сканирай QR: ").strip()
    try:
        ip, port = addr.split(":")
        peer_connect(ip, int(port))
    except Exception:
        print("[⚠️] Невалиден формат. Използвай IP:PORT (пример: 192.168.1.50:8000)")

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Връзка към някакъв адрес, не е нужно да е наличен
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def main():
    print("=== LibreHub v0.1 ===")
    z1 = register_instance(port=8000)
    z2, listener = start_discovery()

    ip = get_local_ip()
    peer_info = f"{ip}:8000"
    print(f"[📡] Сподели това с другите инстанции: {peer_info}")
    generate_qr(peer_info)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[🛑] Изход от LibreHub...")
        z1.close()
        z2.close()

if __name__ == "__main__":
    install_requirements()
    mode = input("Избери режим (s=стартирай, c=свържи се): ").strip()
    if mode == "s":
        main()
    elif mode == "c":
        connect_by_input()

