"""GAZA Loading Animation Module
Spinners and progress animations
"""

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.spinner import Spinner
from rich.live import Live
import time

class LoadingAnimation:
    """Loading animation manager"""
    
    def __init__(self):
        self.console = Console()
        
    def show(self):
        """Show loading animation"""
        self.console.clear()
        
        steps = [
            "Initializing...",
            "Loading modules...",
            "Loading configuration...",
            "Loading plugins...",
            "Loading dashboard...",
            "Finalizing...",
        ]
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=self.console,
        ) as progress:
            task = progress.add_task("[red]GAZA Framework Loading", total=len(steps))
            
            for step in steps:
                progress.update(task, description=f"[red]{step}")
                time.sleep(0.3)
                progress.advance(task)
                
        self.console.print("[green]✓ Loading complete![/green]")
        time.sleep(1)