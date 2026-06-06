"""Metadata Viewer Module
View file metadata
"""

from rich.console import Console
from rich.table import Table
from pathlib import Path
import os
from datetime import datetime

def show_metadata_viewer():
    """Display metadata viewer"""
    console = Console()
    
    path = input("\nEnter file path: ")
    
    try:
        p = Path(path)
        if p.exists():
            stat = p.stat()
            table = Table(title="FILE METADATA", style="magenta")
            table.add_column("Property", style="red")
            table.add_column("Value", style="white")
            
            table.add_row("Filename", p.name)
            table.add_row("Size (bytes)", str(stat.st_size))
            table.add_row("Created", datetime.fromtimestamp(stat.st_ctime).strftime("%Y-%m-%d %H:%M:%S"))
            table.add_row("Modified", datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"))
            table.add_row("Accessed", datetime.fromtimestamp(stat.st_atime).strftime("%Y-%m-%d %H:%M:%S"))
            table.add_row("Permissions", oct(stat.st_mode)[-3:])
            
            console.print(table)
        else:
            console.print("[red]File not found[/red]")
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        
    input("\nPress Enter to continue...")