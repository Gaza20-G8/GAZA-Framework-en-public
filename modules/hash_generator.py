"""Hash Generator Module
Generate file hashes
"""

from rich.console import Console
from rich.table import Table
import hashlib

def show_hash_generator():
    """Display hash generator"""
    console = Console()
    
    path = input("\nEnter file path: ")
    
    try:
        with open(path, 'rb') as f:
            file_data = f.read()
            
            md5_hash = hashlib.md5(file_data).hexdigest()
            sha1_hash = hashlib.sha1(file_data).hexdigest()
            sha256_hash = hashlib.sha256(file_data).hexdigest()
            
            table = Table(title="FILE HASHES", style="cyan")
            table.add_column("Algorithm", style="red")
            table.add_column("Hash", style="white")
            
            table.add_row("MD5", md5_hash)
            table.add_row("SHA1", sha1_hash)
            table.add_row("SHA256", sha256_hash)
            
            console.print(table)
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        
    input("\nPress Enter to continue...")