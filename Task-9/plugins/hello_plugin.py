from plugin_base import PluginBase

class HelloPlugin(PluginBase):
    name = "hello-plugin"

    def activate(self, app):
        print("Hello Plugin Activated")

    def deactivate(self, app):
        print("Hello Plugin Deactivated")