import json
import ipaddress

def load_rules(filename="rules.json"):
    with open(filename, "r") as f:
        return json.load(f) # Load rules from a JSON file
    
def match_rule(packet, rule):
    # Check protocol
    if packet['protocol'].upper() != rule['protocol'].upper(): 
        return False

    # Check port
    if packet['port'] != rule['port']: 
        return False
    
    # Check if the IP matches 
    try:
        if "/" in rule['ip']:
            net = ipaddress.ip_network(rule['ip'], strict=False)
            return ipaddress.ip_address(packet['ip']) in net
        else:
            return packet['ip'] == rule['ip']
    except ValueError:
        return False   
    
def check_packet(packet, rules):
    for rule in rules: 
        if match_rule(packet, rule):   
            return rule['action']
    return "DENY"  # Default action if no rules match

if __name__ == "__main__":
    rules = load_rules()
    
    # Example packets to test
    test_packets = [
        {"ip": "192.168.1.10", "port": 80, "protocol": "TCP"},
        {"ip": "110.0.0.5", "port": 22, "protocol": "TCP"},
        {"ip": "8.8.8.8", "port": 53, "protocol": "UDP"},
    ]

    for packet in test_packets:
        decision = check_packet(packet, rules)
        print(f"Packet: {packet} - Action: {decision}")