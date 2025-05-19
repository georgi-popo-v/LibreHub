import socket
import tkinter as tk
from tkinter import messagebox
from core.peer_discovery import register_instance, start_discovery
from core.peer_connect import peer_connect
import threading


def find_free_port(start=8000, end=9000):
    for port in range(start, end):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
    raise RuntimeError("Няма свободни портове.")


def start_discovery_process(status_label):
    status_label.config(text="🔍 Търси устройства...")

    port = find_free_port()
    register_instance(port=port)
    zeroconf, listener = start_discovery()

    while True:
        services = listener.get_service_info()
        if services:
            for service in services:
                ip, discovered_port = service.parsed_addresses()[0], service.port
                peer_connect(ip, discovered_port)
                status_label.config(text=f"✅ Свързан към {ip}:{discovered_port}. Режим споделяне")
                return


def start_instance(status_label):
    threading.Thread(target=start_discovery_process, args=(status_label,), daemon=True).start()


def main():
    root = tk.Tk()
    root.title("LibreHub")
    root.geometry("350x200")
    root.resizable(False, False)

    label = tk.Label(root, text="LibreHub v0.1", font=("Helvetica", 16))
    label.pack(pady=20)

    status_label = tk.Label(root, text="", font=("Helvetica", 12))
    status_label.pack(pady=10)

    btn_start = tk.Button(root, text="Стартирай", width=20,
                          command=lambda: start_instance(status_label))
    btn_start.pack(pady=10)

    btn_exit = tk.Button(root, text="Изход", width=20, command=root.quit)
    btn_exit.pack()

    root.mainloop()


if __name__ == "__main__":
    main()