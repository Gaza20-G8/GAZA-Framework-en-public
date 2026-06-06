"""DNS Lookup Module
DNS resolution tools
"""

from rich.console import Console
from rich.table import Table
import socket

def show_dns_lookup():
    """Display DNS lookup tool"""
    console = Console()
    
    domain = input("\nEnter domain to lookup: ")
    
    try:
        ip = socket.gethostbyname(domain)
        table = Table(title="DNS LOOKUP RESULTS", style="cyan")
        table.add_column("Property", style="red")
        table.add_column("Value", style="white")
        
        table.add_row("Domain", domain)
        table.add_row("IP Address", ip)
        
        console.print(table)
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        
    input("\nPress Enter to continue...")