"""SSL Information Module
SSL certificate information
"""

from rich.console import Console
from rich.table import Table

def show_ssl_info():
    """Display SSL information"""
    console = Console()
    
    table = Table(title="SSL INFORMATION", style="yellow")
    table.add_column("Property", style="red")
    table.add_column("Value", style="white")
    
    # Placeholder for SSL info
    table.add_row("Feature", "SSL certificate validation")
    table.add_row("Status", "[green]Available[/green]")
    
    console.print(table)
    input("\nPress Enter to continue...")