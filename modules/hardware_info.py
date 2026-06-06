"""Hardware Information Module
CPU, Memory, Disk information
"""

from rich.console import Console
from rich.table import Table
import psutil

def show_hardware_info():
    """Display hardware information"""
    console = Console()
    
    # CPU Info
    cpu_table = Table(title="CPU INFORMATION", style="yellow")
    cpu_table.add_column("Property", style="red")
    cpu_table.add_column("Value", style="white")
    
    cpu_table.add_row("Physical Cores", str(psutil.cpu_count(logical=False)))
    cpu_table.add_row("Total Cores", str(psutil.cpu_count(logical=True)))
    cpu_table.add_row("CPU Usage", f"{psutil.cpu_percent()}%")
    
    console.print(cpu_table)
    
    # Memory Info
    memory = psutil.virtual_memory()
    mem_table = Table(title="MEMORY INFORMATION", style="green")
    mem_table.add_column("Property", style="red")
    mem_table.add_column("Value", style="white")
    
    mem_table.add_row("Total", f"{memory.total / (1024**3):.2f} GB")
    mem_table.add_row("Available", f"{memory.available / (1024**3):.2f} GB")
    mem_table.add_row("Used", f"{memory.used / (1024**3):.2f} GB")
    mem_table.add_row("Percentage", f"{memory.percent}%")
    
    console.print(mem_table)
    input("\nPress Enter to continue...")