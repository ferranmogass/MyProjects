# 🔥 Firewall Básico en Python (con CLI Dinámica)

Este proyecto implementa un **simulador de firewall** escrito en Python.  
Su objetivo es ilustrar el funcionamiento teórico de un cortafuegos:  
filtrar tráfico (simulado) en función de la **dirección IP**, el **puerto** y el **protocolo**.

> ⚠️ **Aviso importante**: Este proyecto es puramente educativo.  
> No modifica las reglas de tu sistema operativo ni bloquea tráfico real.  
> Su finalidad es **aprender** conceptos de redes y seguridad.

---

## 🧠 1. Teoría previa

Un **firewall** (cortafuegos) es una barrera de seguridad que:
- Supervisa el tráfico de red entrante y saliente.
- Aplica un conjunto de **reglas** para permitir o denegar conexiones.
- Protege a los sistemas frente a accesos no autorizados.

### Conceptos básicos

- **IP (Internet Protocol)**: Identificador único de cada dispositivo en una red.
- **Puerto**: Punto lógico donde se comunican las aplicaciones (p. ej. 80 = HTTP).
- **Protocolo**: Define cómo viaja la información (TCP, UDP, etc.).
- **Reglas de filtrado**: Conjunto de condiciones que determinan si un paquete se acepta (`ALLOW`) o se bloquea (`DENY`).

En un entorno real, un firewall puede operar en:
- **Capa de red** (IP, puertos, protocolos)
- **Capa de aplicación** (HTTP, DNS, etc.)

Este proyecto se centra en la **capa de red** para simplificar.

---

## 🗂️ 2. Estructura del proyecto
firewall-basic/
├── firewall.py # Código principal del firewall
├── rules.json # Reglas de filtrado
├── test_packets.json # Paquetes de prueba (opcional)
└── README.md # Este documento


### Archivos principales

- **`firewall.py`**  
  Código principal que:
  - Carga y guarda las reglas desde `rules.json`.
  - Comprueba paquetes de prueba contra las reglas.
  - Ofrece una **interfaz de línea de comandos (CLI)** para añadir, eliminar y listar reglas.
  
- **`rules.json`**  
  Archivo JSON con las reglas de filtrado.  
  Ejemplo:
  ```json
  [
      { "action": "ALLOW", "ip": "192.168.1.10", "port": 80,  "protocol": "TCP" },
      { "action": "DENY",  "ip": "10.0.0.0/24",  "port": 22,  "protocol": "TCP" },
      { "action": "ALLOW", "ip": "0.0.0.0/0",    "port": 53,  "protocol": "UDP" }
  ]

## ⚙️ 3. Requisitios de instalación
- Python 3.8+
- Librerías estándar (json, ipaddress) - ya incluidas en Python.

Clonar este repositorio:
git clone https://github.com/<TU_USUARIO>/firewall-basic.git
cd firewall-basic

## ▶️ 4. Ejecucción del programa 
### 4.1 Ejecución básica 
Ejecuta el firewall con los paquetes de prueba internos:
python firewall.py run
Salida esperada: 
Paquete {'ip': '192.168.1.10', 'port': 80, 'protocol': 'TCP'} -> ALLOW
Paquete {'ip': '10.0.0.5', 'port': 22, 'protocol': 'TCP'} -> DENY
Paquete {'ip': '8.8.8.8', 'port': 53, 'protocol': 'UDP'} -> ALLOW

## 🖥️ 5. Gestión de reglas desde CLI
La principal mejora de esta versión es la **gestión dinámica de reglas** sin editar manualmente rules.json
### Listar reglas:
python firewall.py list

Muestra todas las reglas con su índice: 
[0] ALLOW 192.168.1.10 Port:80 Protocol:TCP
[1] DENY  10.0.0.0/24   Port:22 Protocol:TCP
### Añadir una regla
python firewall.py add ALLOW 192.168.1.50 443 TCP
### Eliminar una regla
python firewall.py delete 0
### Ejectuar comprobación de paquetes
python firewall.py run
