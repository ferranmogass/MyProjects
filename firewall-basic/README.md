# 🔥 Firewall Básico en Python (con CLI Dinámica)

Este proyecto implementa un **simulador de firewall** escrito en Python.  
Su objetivo es ilustrar el funcionamiento teórico de un cortafuegos:  
filtrar tráfico (simulado) en función de la **dirección IP**, el **puerto** y el **protocolo**.

---

## 🧠 1. Teoría 

Un **firewall** (cortafuegos) es una barrera de seguridad que:
- Supervisa el tráfico de red entrante y saliente.
- Aplica un conjunto de **reglas** para permitir o denegar conexiones.
- Protege a los sistemas frente a accesos no autorizados.

### Conceptos básicos

- **IP (Internet Protocol)**: Identificador único de cada dispositivo en una red.
- **Puerto**: Punto lógico donde se comunican las aplicaciones (p. ej. 80 = HTTP).
- **Protocolo**: Define cómo viaja la información (TCP, UDP, etc...).
- **Reglas de filtrado**: Conjunto de condiciones que determinan si un paquete se acepta (`ALLOW`) o se bloquea (`DENY`).

En un entorno real, un firewall puede operar en:
- **Capa de red** (IP, puertos, protocolos).
- **Capa de aplicación** (HTTP, DNS, etc.).

Este proyecto se centra en la **capa de red** para simplificar.

---

## 🗂️ 2. Estructura del proyecto

```
firewall-basic/
├── firewall.py       # Código principal del firewall
├── rules.json        # Reglas de filtrado
└── README.md         # Este documento
```

### Archivos principales

- **`firewall.py`**  
  Código principal:
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
  ```

---

## ⚙️ 3. Requisitos de instalación

- **Python 3.8+**
- Librerías estándar (`json`, `ipaddress`, `argparse`) - ya incluidas en Python.

**Clonar este repositorio:**
```bash
git clone https://github.com/ferranmogass/MyProjects.git
cd MyProjects/firewall-basic
```

---

## ▶️ 4. Ejecución del programa

### 4.1 Ejecución básica

Ejecuta el firewall con los paquetes de prueba internos:
```bash
python firewall.py run
```

**Salida esperada:**
```
🧪 Executant proves del firewall...
============================================================
✅ Paquet 192.168.1.10:80 (TCP) → ALLOW
❌ Paquet 10.0.0.5:22 (TCP) → DENY
✅ Paquet 8.8.8.8:53 (UDP) → ALLOW
✅ Paquet 192.168.1.50:443 (TCP) → ALLOW
✅ Paquet 203.0.113.100:80 (TCP) → ALLOW
============================================================
Proves completades amb 6 regles carregades
```

---

## 🖥️ 5. Gestión de reglas desde CLI

La principal mejora de esta versión es la **gestión dinámica de reglas** sin editar manualmente `rules.json`.

### 📋 Listar reglas

```bash
python firewall.py list
```

**Muestra todas las reglas con su índice:**
```
📋 Regles del firewall:
--------------------------------------------------
[0] ALLOW 192.168.1.10 Port:80 Protocol:TCP
[1] DENY 10.0.0.0/24 Port:22 Protocol:TCP
[2] ALLOW 0.0.0.0/0 Port:53 Protocol:UDP
--------------------------------------------------
Total: 3 regles
```

### ➕ Añadir una regla

```bash
python firewall.py add ALLOW 192.168.1.50 443 TCP
```

**Ejemplos de reglas útiles:**
```bash
# Permitir HTTP desde la red local
python firewall.py add ALLOW 192.168.1.0/24 80 TCP

# Denegar SSH desde cualquier IP
python firewall.py add DENY 0.0.0.0/0 22 TCP

# Permitir DNS desde cualquier lugar
python firewall.py add ALLOW 0.0.0.0/0 53 UDP

# Permitir HTTPS desde una IP específica
python firewall.py add ALLOW 203.0.113.15 443 TCP
```

### 🗑️ Eliminar una regla

```bash
python firewall.py delete 0
```
> Elimina la regla con índice 0. Usa `list` para ver los índices.

### 🧪 Ejecutar comprobación de paquetes

```bash
python firewall.py run
```

### 📖 Ver ayuda

```bash
python firewall.py --help
```

---

## 📝 6. Ejemplos de uso completos

### Escenario 1: Configuración de servidor web.
```bash
# 1. Ver reglas actuales
python firewall.py list

# 2. Permitir HTTP y HTTPS desde la red local
python firewall.py add ALLOW 192.168.1.0/24 80 TCP
python firewall.py add ALLOW 192.168.1.0/24 443 TCP

# 3. Denegar SSH desde el exterior
python firewall.py add DENY 0.0.0.0/0 22 TCP

# 4. Probar la configuración
python firewall.py run
```

### Escenario 2: Limpieza de reglas
```bash
# 1. Ver todas las reglas
python firewall.py list

# 2. Eliminar reglas innecesarias (empezar por los índices más altos)
python firewall.py delete 2
python firewall.py delete 1
python firewall.py delete 0

# 3. Verificar que están eliminadas
python firewall.py list
```

---

## 🔧 7. Características técnicas

### Validaciones implementadas
- **IPs válidas**: Acepta IPs individuales (`192.168.1.10`) y rangos CIDR (`192.168.1.0/24`).
- **Puertos válidos**: Rango 0-65535.
- **Protocolos soportados**: TCP, UDP.
- **Acciones disponibles**: ALLOW, DENY.

### Gestión de archivos
- **Rutas absolutas**: El script funciona desde cualquier directorio.
- **Formato JSON**: Datos estructurados y legibles.

### Manejo de errores
- Validación de argumentos de entrada.
- Gestión de archivos corruptos o inexistentes.
- Mensajes de error descriptivos.

---

## 🎯 8. Objetivos de aprendizaje

Al completar este proyecto, he aprendido:

1. **Conceptos de redes**: IPs, puertos, protocolos, subredes CIDR.
2. **Seguridad básica**: Funcionamiento de un firewall, reglas de filtrado.
3. **Python**: Manejo de JSON, validación de datos, CLI con `argparse`.
4. **Debugging**: Manejo de errores y validaciones.

---

## 🚀 9. Posibles mejoras

- [ ] Soporte para rangos de puertos (`80-8080`).
- [ ] Reglas por fecha/hora.
- [ ] Logging de eventos.
- [ ] Importar/exportar reglas en otros formatos.
- [ ] Estadísticas de tráfico bloqueado/permitido.

---

## 📄 10. Licencia

Este proyecto es de código abierto y con fines educativos.  
Siéntete libre de modificarlo y mejorarlo.

---
