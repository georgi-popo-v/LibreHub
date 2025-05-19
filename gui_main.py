import socket
import tkinter as tk
from tkinter import messagebox
from core.peer_discovery import register_instance, start_discovery

def find_free_port(start=8000, end=9000):
    for port in range(start, end):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
    raise RuntimeError("No free ports available.")

def start_instance():
    try:
        port = find_free_port()
        register_instance(port=port)
        start_discovery()
        messagebox.showinfo("LibreHub", f"LibreHub стартира на порт {port}")
    except Exception as e:
        messagebox.showerror("Грешка", str(e))

def main():
    root = tk.Tk()
    root.title("LibreHub")
    root.geometry("300x180")
    root.resizable(False, False)

    label = tk.Label(root, text="LibreHub v0.1", font=("Helvetica", 16))
    label.pack(pady=20)

    btn_start = tk.Button(root, text="Стартирай", width=20, command=start_instance)
    btn_start.pack(pady=10)

    btn_exit = tk.Button(root, text="Изход", width=20, command=root.quit)
    btn_exit.pack()

    root.mainloop()

if __name__ == "__main__":
    main()

