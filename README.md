<p align="center">
  <img src="https://sdmntprsouthcentralus.oaiusercontent.com/files/00000000-49a4-61f7-960f-3ac1d41333dc/raw?se=2025-04-15T05%3A14%3A56Z&sp=r&sv=2024-08-04&sr=b&scid=547445bc-cb12-5925-8e4d-f45e059bd07c&skoid=dfdaf859-26f6-4fed-affc-1befb5ac1ac2&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-14T20%3A17%3A42Z&ske=2025-04-15T20%3A17%3A42Z&sks=b&skv=2024-08-04&sig=Tla4hRUdPjalPPV9AkwaX63liMcKlCwEY2UT8K%2BFktI%3D" alt="Logo de Priorix" width="150"/>
</p>

<div align="center">
  <h1>🧠 Priorix</h1>
  <h3>Administrador de Tareas Modular en Python</h3>

  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg?style=flat&logo=python" />
  <img src="https://img.shields.io/badge/Estado-Activo-success?style=flat" />
  <img src="https://img.shields.io/badge/Hecho%20con%20💻-por%20[TuNombre]-purple?style=flat" />
</div>

---

**Priorix** es una aplicación de consola escrita en Python para gestionar tareas de forma simple pero estructurada. Utiliza módulos separados para facilitar la edición, creación y visualización de tareas, con almacenamiento local en JSON.

---

## 📂 Estructura del proyecto

```bash
priorix/
├── arranque.py           # Main launcher
├── core/                 # Core functionality
│   ├── init.py
│   ├── tareas.py         # Task management
│   ├── storage.py        # JSON persistence
│   └── interfaz.py       # User interface
├── data/                 # Task storage
│   └── tareas.json
└── README.md
```

---

## 🚀 Funcionalidades

- 📌 **Crear tareas** con nombre, descripción y fecha
- ✏️ **Editar tareas existentes**
- 📋 **Visualizar tareas** en formato claro y estético
- 💾 **Persistencia en JSON**
- 🧱 **Arquitectura modular** (cada acción en su archivo)

---

## ▶️ Cómo usar Priorix

1. Clona este repositorio:

```bash
git clone https://github.com/TuUsuario/priorix.git
cd priorix
```

2. Ejecuta el arranque:

```bash
python arranque.py
```

> Para salir del programa, utiliza la opción `Salir` que aparece en el menú o cierra la terminal.

---

## 📸 Vista previa

> Así se ve Priorix en acción:

![Demo de consola]()

---

## 🔧 Requisitos

- Python 3.7 o superior

---

## 🛠 Contribuir

¿Te gustaría aportar? Haz un fork, crea una nueva rama y envía tu pull request.  
¡Toda ayuda es bienvenida!

---

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT. 