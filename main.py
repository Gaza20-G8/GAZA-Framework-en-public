#!/usr/bin/env python3
"""GAZA Framework v9.0
Modern Cyberpunk Terminal Interface
Author: Gaza20-G8
"""

import sys
import os
import json
from pathlib import Path
from core.banner import Banner
from core.menu import MenuManager
from core.logger import Logger
from core.config import ConfigManager
from core.dashboard import Dashboard
from core.animations import LoadingAnimation

class GAZAFramework:
    """Main GAZA Framework Controller"""
    
    def __init__(self):
        self.version = "9.0"
        self.author = "Gaza20-G8"
        self.base_path = Path(__file__).parent
        
        # Initialize core components
        self.logger = Logger(self.base_path / "logs")
        self.config = ConfigManager(self.base_path / "config.json")
        self.banner = Banner()
        self.menu = MenuManager(self.logger, self.config)
        self.dashboard = Dashboard(self.logger, self.config)
        
    def initialize(self):
        """Initialize GAZA Framework"""
        self.logger.info("Initializing GAZA Framework v9.0")
        
        # Create necessary directories
        self._create_directories()
        
        # Show loading animation
        loading = LoadingAnimation()
        loading.show()
        
        self.logger.success("Framework initialized successfully")
        
    def _create_directories(self):
        """Create required directories"""
        dirs = ["logs", "exports", "plugins", "assets"]
        for directory in dirs:
            path = self.base_path / directory
            path.mkdir(exist_ok=True)
            
    def run(self):
        """Run GAZA Framework"""
        try:
            self.initialize()
            self.banner.display()
            self.dashboard.show()
            self.menu.run()
        except KeyboardInterrupt:
            self.logger.warning("Framework terminated by user")
            sys.exit(0)
        except Exception as e:
            self.logger.error(f"Critical error: {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    framework = GAZAFramework()
    framework.run()