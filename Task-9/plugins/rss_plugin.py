from plugin_base import PluginBase

class RSSPlugin(PluginBase):
    name = "rss-feed"
    dependencies = ["hello-plugin"]

    def activate(self, app):
        print("RSS Plugin Activated")

    def deactivate(self, app):
        print("RSS Plugin Deactivated")