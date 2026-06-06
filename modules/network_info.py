"""Network Information Module
Display network configuration
"""

from rich.console import Console
from rich.table import Table
import socket

def show_network_info():
    """Display network information"""
    console = Console()
    
    table = Table(title="NETWORK INFORMATION", style="blue")
    table.add_column("Property", style="red")
    table.add_column("Value", style="white")
    
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        
        table.add_row("Hostname", hostname)
        table.add_row("IP Address", ip_address)
        table.add_row("FQDN", socket.getfqdn())
    except:
        table.add_row("Error", "Could not retrieve network info")
        
    console.print(table)
    input("\nPress Enter to continue...")