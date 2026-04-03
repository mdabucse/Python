import os
import importlib
from plugin_base import PluginBase

PLUGIN_FOLDER = "plugins"


def load_plugins():
    plugins = []

    for filename in os.listdir(PLUGIN_FOLDER):
        if filename.endswith(".py") and not filename.startswith("_"):

            module_name = filename[:-3]
            module_path = f"{PLUGIN_FOLDER}.{module_name}"

            module = importlib.import_module(module_path)

            for attr in dir(module):
                obj = getattr(module, attr)

                if isinstance(obj, type) and issubclass(obj, PluginBase) and obj != PluginBase:
                    plugins.append(obj())

    return plugins


def resolve_dependencies(plugins):
    plugin_map = {plugin.name: plugin for plugin in plugins}
    visited = set()
    visiting = set()
    stack = []

    def visit(plugin):
        if plugin.name in visiting:
            raise Exception(f"Circular dependency: {plugin.name}")

        if plugin.name not in visited:
            visiting.add(plugin.name)

            for dep in plugin.dependencies:
                if dep not in plugin_map:
                    raise Exception(f"Missing dependency: {dep}")
                visit(plugin_map[dep])

            visiting.remove(plugin.name)
            visited.add(plugin.name)
            stack.append(plugin)

    for plugin in plugins:
        visit(plugin)

    return stack