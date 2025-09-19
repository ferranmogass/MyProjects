# 🔥 Firewall Básico en Python

Este proyecto implementa **un simulador de firewall** escrito en Python.  
Su objetivo es **ilustrar el funcionamiento teórico de un cortafuegos**:  
filtrar tráfico (simulado) en función de la **dirección IP**, el **puerto** y el **protocolo**.

> ⚠️ **Aviso**: Este proyecto es educativo.  
> No modifica reglas del sistema operativo ni bloquea tráfico real.  
> Sirve para aprender conceptos de redes y seguridad.

---

## 🧠 1. Teoría

Un **firewall** (o cortafuegos) es una barrera de seguridad que:
- Supervisa el tráfico de red entrante y saliente.
- Aplica un conjunto de **reglas** para permitir o denegar conexiones.
- Protege sistemas frente a accesos no autorizados.

### Conceptos básicos

- **IP (Internet Protocol)**: Identificador único de cada dispositivo en una red.
- **Puerto**: Punto lógico donde se comunican las aplicaciones (p. ej. 80 = HTTP).
- **Protocolo**: Define cómo viaja la información (TCP, UDP, etc.).
- **Reglas de filtrado**: Conjunto de condiciones que determinan si un paquete se acepta (`ALLOW`) o se bloquea (`DENY`).

Un firewall real puede operar en:
- **Capa de red** (IP, puertos, protocolos)
- **Capa de aplicación** (HTTP, DNS, etc.)

Este proyecto se centra en **capa de red** para simplificar.

---

## 🗂️ 2. Estructura del proyecto

firewall-basic/
├── firewall.py
├── rules.json
└── README.md

### 2.1 `firewall.py`
- **Carga las reglas** desde `rules.json`.
- **Recibe paquetes de prueba** (diccionarios en Python)
- Comprueba cada paquete:
  - Dirección IP (acepta direcciones individuales o subredes en formato CIDR).
  - Puerto (número entero).
  - Protocolo (TCP o UDP).
- Devuelve `ALLOW` o `DENY` según la primera regla que coincida.
- Si no coincide ninguna, **NO permite el tráfico por defecto**.

### 2.2 `rules.json`
Archivo en formato JSON que define las reglas del firewall.  
Ejemplo incluido:
```json
[
    { "action": "ALLOW", "ip": "192.168.1.10", "port": 80,  "protocol": "TCP" },
    { "action": "DENY",  "ip": "10.0.0.0/24",  "port": 22,  "protocol": "TCP" },
    { "action": "ALLOW", "ip": "0.0.0.0/0",    "port": 53,  "protocol": "UDP" }
]
