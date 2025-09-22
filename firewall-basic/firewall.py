import json
import ipaddress
import argparse
import sys
from pathlib import Path

# Utilitzar la ruta absoluta basada en la ubicació del script
SCRIPT_DIR = Path(__file__).parent
RULES_FILE = SCRIPT_DIR / "rules.json"


def load_rules():
    """Carrega les regles des del fitxer JSON"""
    if not RULES_FILE.exists():  
        return []   # return empty list
    try:
        with open(RULES_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error carregant regles: {e}")
        return []


def save_rules(rules):
    """Guarda les regles al fitxer JSON"""
    try:
        with open(RULES_FILE, "w") as f:
            json.dump(rules, f, indent=4)
        print(f"✅ Regles desades a {RULES_FILE}")
    except Exception as e:
        print(f"❌ Error desant regles: {e}")


def match_rule(packet, rule):
    """Comprova si un paquet coincideix amb una regla"""
    # Check protocol
    if packet["protocol"].upper() != rule["protocol"].upper():  
        return False
    # Check port
    if packet["port"] != rule["port"]:
        return False
    # Check IP
    try:
        if "/" in rule["ip"]:
            net = ipaddress.ip_network(rule["ip"], strict=False)
            return ipaddress.ip_address(packet["ip"]) in net
        else:
            return packet["ip"] == rule["ip"]
    except ValueError:
        return False


def check_packet(packet, rules):
    """Comprova un paquet contra totes les regles i retorna l'acció"""
    for rule in rules:
        if match_rule(packet, rule):
            return rule["action"]
    return "ALLOW"  # Default action


def list_rules():
    """Llista totes les regles definides"""
    rules = load_rules()
    if not rules:
        print("❌ No hi ha regles definides.")
        return
    
    print("📋 Regles del firewall:")
    print("-" * 50)
    for idx, rule in enumerate(rules): 
        print(f"[{idx}] {rule['action']} {rule['ip']} Port:{rule['port']} Protocol:{rule['protocol']}")
    print("-" * 50)
    print(f"Total: {len(rules)} regles")


def add_rule(action, ip, port, protocol):
    """Afegeix una nova regla al firewall"""
    try:
        rules = load_rules()
        new_rule = {
            "action": action.upper(),
            "ip": ip,
            "port": int(port),
            "protocol": protocol.upper()
        }
        
        # Validar IP
        try:
            if "/" in ip:
                ipaddress.ip_network(ip, strict=False)
            else:
                ipaddress.ip_address(ip)
        except ValueError:
            print(f"❌ Error: IP '{ip}' no és vàlida")
            return
        
        # Validar port
        if not (0 <= int(port) <= 65535):
            print(f"❌ Error: Port '{port}' no és vàlid (0-65535)")
            return
        
        rules.append(new_rule)
        save_rules(rules)
        print(f"✅ Regla afegida: {new_rule}")
        
    except Exception as e:
        print(f"❌ Error afegint regla: {e}")


def delete_rule(index):
    """Elimina una regla pel seu índex"""
    try:
        rules = load_rules()
        if 0 <= index < len(rules): 
            removed = rules.pop(index)
            save_rules(rules)
            print(f"✅ Regla eliminada: {removed}")
        else:
            print(f"❌ Índex {index} fora de rang. Hi ha {len(rules)} regles (0-{len(rules)-1})")
    except Exception as e:
        print(f"❌ Error eliminant regla: {e}")


def run_test():
    """Executa una prova amb paquets de test"""
    print("🧪 Executant proves del firewall...")
    print("=" * 60)
    
    rules = load_rules()
    test_packets = [
        {"ip": "192.168.1.10", "port": 80, "protocol": "TCP"},
        {"ip": "10.0.0.5", "port": 22, "protocol": "TCP"},
        {"ip": "8.8.8.8", "port": 53, "protocol": "UDP"},
        {"ip": "192.168.1.50", "port": 443, "protocol": "TCP"},
        {"ip": "203.0.113.100", "port": 80, "protocol": "TCP"}
    ]
    
    for pkt in test_packets:
        decision = check_packet(pkt, rules)
        status_icon = "✅" if decision == "ALLOW" else "❌"
        print(f"{status_icon} Paquet {pkt['ip']}:{pkt['port']} ({pkt['protocol']}) → {decision}")
    
    print("=" * 60)
    print(f"Proves completades amb {len(rules)} regles carregades")


def main():
    """Funció principal que gestiona els arguments de la línia de comandos"""
    parser = argparse.ArgumentParser(
        description="🔥 Firewall bàsic amb gestió de regles dinàmiques",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'ús:
  python firewall.py list                              # Llista totes les regles
  python firewall.py add ALLOW 192.168.1.0/24 80 TCP  # Permet HTTP des de la xarxa local
  python firewall.py add DENY 0.0.0.0/0 22 TCP        # Denega SSH des de qualsevol IP
  python firewall.py delete 0                          # Elimina la primera regla
  python firewall.py run                               # Executa proves de test
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

    # Subcomanda list
    subparsers.add_parser("list", help="Llista totes les regles")

    # Subcomanda add
    add_parser = subparsers.add_parser("add", help="Afegeix una nova regla")
    add_parser.add_argument("action", choices=["ALLOW", "DENY"], help="Acció de la regla")
    add_parser.add_argument("ip", help="IP o subxarxa CIDR (ex. 192.168.1.0/24)")
    add_parser.add_argument("port", type=int, help="Port (ex. 80)")
    add_parser.add_argument("protocol", choices=["TCP", "UDP"], help="Protocol")

    # Subcomanda delete
    del_parser = subparsers.add_parser("delete", help="Elimina una regla pel seu índex")
    del_parser.add_argument("index", type=int, help="Índex de la regla (veure amb 'list')")

    # Subcomanda run
    subparsers.add_parser("run", help="Executa la comprovació de paquets de prova")

    args = parser.parse_args()

    # Gestió dels comandos
    if args.command == "list":
        list_rules()
    elif args.command == "add":
        add_rule(args.action, args.ip, args.port, args.protocol)
    elif args.command == "delete":
        delete_rule(args.index)
    elif args.command == "run":
        run_test()
    else:
        # Si no es proporciona cap comando, mostra l'ajuda
        parser.print_help()


if __name__ == "__main__":
    main()