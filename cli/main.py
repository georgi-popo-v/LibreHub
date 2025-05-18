# librehub/cli/main.py

import time
from core.peer_discovery import register_instance, start_discovery

def main():
    print("=== LibreHub v0.1 ===")
    z1 = register_instance(port=8000)
    z2, listener = start_discovery()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[🛑] Изход от LibreHub...")
        z1.close()
        z2.close()

if __name__ == "__main__":
    main()

