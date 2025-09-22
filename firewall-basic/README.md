🔥 Firewall Bàsic en Python (CLI Dinàmica)
Un simulador de firewall escrit en Python per aprendre com funcionen els cortafocs de xarxa: filtra tràfic (simulat) segons IP, port i protocol.
⚠️ Projecte educatiu
No canvia les regles del teu sistema ni bloqueja tràfic real.
Serveix exclusivament per aprendre conceptes de xarxes i seguretat.
🧠 1. Teoria bàsica
Un firewall és una barrera de seguretat que:
Supervisa el tràfic de xarxa entrant i sortint.
Aplica regles per permetre o denegar connexions.
Protegeix els sistemes d’accessos no autoritzats.
Conceptes clau
IP: identificador únic d’un dispositiu en una xarxa.
Port: punt lògic de comunicació (p. ex. 80 = HTTP).
Protocol: manera com viatja la informació (TCP, UDP…).
Regles de filtratge: condicions per acceptar (ALLOW) o bloquejar (DENY) paquets.
Aquest projecte se centra en la capa de xarxa (IP/ports/protocols) per simplicitat.
🗂️ 2. Estructura del projecte
firewall-basic/
├── firewall.py       # Codi principal del firewall
├── rules.json        # Regles de filtratge
├── test_packets.json # Paquets de prova (opcional)
└── README.md         # Aquest document
