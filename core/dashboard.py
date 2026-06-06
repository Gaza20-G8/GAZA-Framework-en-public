"""GAZA Dashboard Module
System information display
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
from datetime import datetime
import psutil
import platform
import os

class Dashboard:
    """System dashboard"""
    
    def __init__(self, logger, config):
        self.console = Console()
        self.logger = logger
        self.config = config
        
    def show(self):
        """Display dashboard"""
        # Gather system info
        info = self._gather_system_info()
        
        # Create table
        table = Table(title="SYSTEM DASHBOARD", style="red")
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="white")
        
        for key, value in info.items():
            table.add_row(key, str(value))
            
        self.console.print(table)
        self.console.print()
        
    def _gather_system_info(self) -> dict:
        """Gather system information"""
        try:
            cpu_percent = psutil.cpu_percent(interval=0.1)
            memory = psutil.virtual_memory()
            
            return {
                "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "OS": platform.system(),
                "Python": platform.python_version(),
                "User": os.environ.get('USER', os.environ.get('USERNAME', 'N/A')),
                "RAM Usage": f"{memory.percent}%",
                "CPU Usage": f"{cpu_percent}%",
                "Total RAM": f"{memory.total / (1024**3):.2f} GB",
                "Available RAM": f"{memory.available / (1024**3):.2f} GB",
                "Processor": platform.processor(),
                "Hostname": platform.node(),
            }
        except Exception as e:
            self.logger.error(f"Error gathering system info: {str(e)}")
            return {}