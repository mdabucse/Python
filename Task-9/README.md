#  Plugin Architecture with Dynamic Module Loading

## Overview

This project demonstrates how to build a **plugin-based architecture** in Python where:

- Plugins are discovered dynamically at runtime
- Dependencies between plugins are resolved automatically
- Plugins can be added/removed without modifying the core application

---

## Key Concepts

- **PluginBase** → Defines rules all plugins must follow  
- **Dynamic Loading** → Load plugins using `importlib`  
- **Dependency Resolution** → Ensure correct execution order  
- **Loose Coupling** → Core app doesn’t depend on plugins  

---

## Project Structure
```
Task-9/
│
├── plugin_base.py
├── plugin_loader.py 
├── main.py 
└── plugins/
├── hello_plugin.py
└── rss_plugin.py
```