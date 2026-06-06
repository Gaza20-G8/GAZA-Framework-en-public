"""GAZA Plugin Loader Module
Dynamic plugin loading system
"""

import importlib.util
from pathlib import Path
from typing import List, Dict, Any

class PluginLoader:
    """Plugin loader manager"""
    
    def __init__(self, plugins_dir: Path):
        self.plugins_dir = plugins_dir
        self.plugins = {}
        
    def load_plugins(self) -> Dict[str, Any]:
        """Load all plugins from directory"""
        if not self.plugins_dir.exists():
            return {}
            
        for plugin_file in self.plugins_dir.glob("*.py"):
            if plugin_file.name.startswith("_"):
                continue
                
            try:
                spec = importlib.util.spec_from_file_location(
                    plugin_file.stem,
                    plugin_file
                )
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                if hasattr(module, 'PLUGIN_NAME'):
                    self.plugins[module.PLUGIN_NAME] = {
                        'module': module,
                        'name': getattr(module, 'PLUGIN_NAME', 'Unknown'),
                        'version': getattr(module, 'PLUGIN_VERSION', '1.0'),
                        'author': getattr(module, 'PLUGIN_AUTHOR', 'Unknown'),
                        'description': getattr(module, 'PLUGIN_DESCRIPTION', 'No description'),
                    }
            except Exception as e:
                print(f"Error loading plugin {plugin_file.name}: {str(e)}")
                
        return self.plugins
        
    def list_plugins(self) -> List[Dict]:
        """List all loaded plugins"""
        return list(self.plugins.values())