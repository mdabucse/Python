import os
import importlib
from plugin_base import PluginBase
from plugin_loader import load_plugins, resolve_dependencies
PLUGIN_FOLDER = "plugins"

def load_plugins():
    plugins = []

    for filename in os.listdir(PLUGIN_FOLDER):
        if filename.endswith(".py") and not filename.startswith("_"):

            module_name = filename[:-3]  # remove .py
            module_path = f"{PLUGIN_FOLDER}.{module_name}"

            module = importlib.import_module(module_path)

            # Find classes inside module
            for attr in dir(module):
                obj = getattr(module, attr)

                if isinstance(obj, type) and issubclass(obj, PluginBase) and obj != PluginBase:
                    plugins.append(obj())

    return plugins

if __name__ == "__main__":
    print("[CORE] Loading plugins...")
    plugins = load_plugins()

    print("[CORE] Resolving dependencies...")
    plugins = resolve_dependencies(plugins)

    print("[CORE] Activating plugins...")
    for plugin in plugins:
        print(f"-> {plugin.name}")
        plugin.activate(app=None)