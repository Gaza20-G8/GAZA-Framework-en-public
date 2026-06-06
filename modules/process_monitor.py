"""Process Monitor Module
Monitor running processes
"""

from rich.console import Console
from rich.table import Table
import psutil

def show_process_monitor():
    """Display process monitor"""
    console = Console()
    
    table = Table(title="TOP 10 PROCESSES BY MEMORY", style="cyan")
    table.add_column("PID", style="red")
    table.add_column("Name", style="white")
    table.add_column("CPU %", style="yellow")
    table.add_column("Memory MB", style="green")
    
    try:
        processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']),
                          key=lambda p: p.info['memory_info'].rss, reverse=True)[:10]
        
        for proc in processes:
            try:
                table.add_row(
                    str(proc.info['pid']),
                    proc.info['name'][:30],
                    f"{proc.info['cpu_percent']:.1f}",
                    f"{proc.info['memory_info'].rss / (1024**2):.1f}"
                )
            except:
                pass
    except:
        console.print("[red]Error reading processes[/red]")
            
    console.print(table)
    input("\nPress Enter to continue...")