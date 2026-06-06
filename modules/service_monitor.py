"""Service Monitor Module
Monitor system services
"""

from rich.console import Console
from rich.table import Table

def show_service_monitor():
    """Display service monitor"""
    console = Console()
    
    table = Table(title="SERVICE MONITOR", style="magenta")
    table.add_column("Service", style="red")
    table.add_column("Status", style="white")
    
    # Placeholder for service monitoring
    table.add_row("SSH", "[green]Running[/green]")
    table.add_row("HTTP", "[green]Running[/green]")
    table.add_row("Database", "[yellow]Idle[/yellow]")
    
    console.print(table)
    input("\nPress Enter to continue...")