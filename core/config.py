"""GAZA Configuration Manager Module
JSON configuration handling
"""

import json
from pathlib import Path
from typing import Any, Dict

class ConfigManager:
    """Configuration manager"""
    
    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.config = self._load_config()
        
    def _load_config(self) -> Dict:
        """Load configuration from JSON"""
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r') as f:
                    return json.load(f)
            except:
                return self._default_config()
        return self._default_config()
        
    def _default_config(self) -> Dict:
        """Return default configuration"""
        return {
            "app": {
                "name": "GAZA Framework",
                "version": "9.0",
                "author": "Gaza20-G8",
            },
            "theme": {
                "primary_color": "red",
                "secondary_color": "white",
            },
            "logging": {
                "enabled": True,
                "level": "INFO",
            }
        }
        
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        return value if value is not None else default
        
    def set(self, key: str, value: Any):
        """Set configuration value"""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value
        self.save()
        
    def save(self):
        """Save configuration to JSON"""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")