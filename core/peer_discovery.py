from zeroconf import Zeroconf, ServiceInfo, ServiceBrowser
import socket

SERVICE_TYPE = "_librehub._tcp.local."

class PeerListener:
    def __init__(self):
        self.peers = []
        
    def remove_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info:
            ip = socket.inet_ntoa(info_addresses[0])
            print(f"[✅] Открит LibreHub: {name} ({ip}:{info.port})")
            self.peers.append((name, ip, info.port))

    def add_service(self, zeroconf, type, name):
        if name.startswith(f"{socket.gethostname()}._librehub._tcp.local."):
            return  
        info = zeroconf.get_service_info(type, name)
        if info:
            ip = socket.inet_ntoa(info.addresses[0])
            print(f"[✅] Открит LibreHub: {name} ({ip}:{info.port})")
            self.peers.append((name, ip, info.port))

    def update_service(self, zeroconf, type, name):
        pass

def start_discovery():
    zeroconf = Zeroconf()
    listener = PeerListener()
    browser = ServiceBrowser(zeroconf, SERVICE_TYPE, listener)
    print("[🔍] Стартирано търсене за други инстанции в мрежата...")
    return zeroconf, listener

def register_instance(port=8000):
    ip = socket.gethostbyname(socket.gethostname())
    desc = {'version': '0.1'}
    info = ServiceInfo(
            SERVICE_TYPE,
            f"{socket.gethostname()}._librehub._tcp.local.",
            addresses=[socket.inet_aton(ip)],
            port=port,
            properties=desc,
            server=f"{socket.gethostname()}.local."
    )
        
    zeroconf = Zeroconf()
    zeroconf.register_service(info)
    print(f"[🌐] LibreHub стартиран на {ip}:{port}")
    return zeroconf


