from abc import ABC, abstractmethod

class PluginBase(ABC):
    name = "base-plugin"
    version = "0.0.1"
    dependencies = []

    @abstractmethod
    def activate(self, app):
        """Start the plugin"""
        pass

    @abstractmethod
    def deactivate(self, app):
        """Stop the plugin"""
        pass