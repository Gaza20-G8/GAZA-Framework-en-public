"""Log Analyzer Module
Analyze log files
"""

from rich.console import Console
from rich.table import Table
from pathlib import Path

def show_log_analyzer():
    """Display log analyzer"""
    console = Console()
    
    path = input("\nEnter log file path: ")
    
    try:
        p = Path(path)
        if p.exists():
            with open(p, 'r') as f:
                lines = f.readlines()
                
            table = Table(title="LOG ANALYSIS", style="yellow")
            table.add_column("Metric", style="red")
            table.add_column("Value", style="white")
            
            table.add_row("Total Lines", str(len(lines)))
            table.add_row("File Size", f"{p.stat().st_size} bytes")
            
            console.print(table)
            
            # Show last 10 lines
            console.print("\n[cyan]Last 10 lines:[/cyan]")
            for line in lines[-10:]:
                console.print(line.rstrip())
        else:
            console.print("[red]File not found[/red]")
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        
    input("\nPress Enter to continue...")