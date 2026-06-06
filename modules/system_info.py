"""System Information Module
Display system details
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import platform
import os
import socket

def show_system_info():
    """Display system information"""
    console = Console()
    
    info_data = {
        "Hostname": socket.gethostname(),
        "OS": platform.system(),
        "OS Version": platform.release(),
        "Architecture": platform.architecture()[0],
        "Python Version": platform.python_version(),
        "Processor": platform.processor(),
        "Machine": platform.machine(),
        "User": os.environ.get('USER', os.environ.get('USERNAME', 'Unknown')),
    }
    
    table = Table(title="SYSTEM INFORMATION", style="cyan")
    table.add_column("Property", style="red")
    table.add_column("Value", style="white")
    
    for key, value in info_data.items():
        table.add_row(key, str(value))
        
    console.print(table)
    input("\nPress Enter to continue...")