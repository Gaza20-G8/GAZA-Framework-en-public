"""File Analyzer Module
Analyze files and directories
"""

from rich.console import Console
from rich.table import Table
from pathlib import Path
import os

def show_file_analyzer():
    """Display file analyzer"""
    console = Console()
    
    path = input("\nEnter file/directory path: ")
    
    try:
        p = Path(path)
        if p.is_file():
            size = os.path.getsize(p)
            table = Table(title="FILE INFORMATION", style="green")
            table.add_column("Property", style="red")
            table.add_column("Value", style="white")
            
            table.add_row("Filename", p.name)
            table.add_row("Size", f"{size} bytes")
            table.add_row("Type", p.suffix)
            table.add_row("Path", str(p.absolute()))
            
            console.print(table)
        else:
            console.print("[red]File not found[/red]")
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        
    input("\nPress Enter to continue...")