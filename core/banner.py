"""GAZA Banner Display Module
Cyberpunk themed ASCII art and animations
"""

from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
import pyfiglet
import time

class Banner:
    """GAZA Banner Manager"""
    
    def __init__(self):
        self.console = Console()
        
    def display(self):
        """Display GAZA banner"""
        self.console.clear()
        
        # ASCII Art Logo
        figlet = pyfiglet.Figlet(font='banner', width=200)
        logo = figlet.renderText('GAZA')
        
        # Styled logo
        styled_logo = Text(logo, style="bold red")
        self.console.print(Align.center(styled_logo))
        
        # Signature
        signature = Text("Snapchat: Gaza9.0k", style="bold white on black")
        self.console.print(Align.center(signature))
        
        # Version
        version = Text("Version 9.0", style="dim yellow")
        self.console.print(Align.center(version))
        
        # Separator
        separator = Text("═" * 80, style="red")
        self.console.print(Align.center(separator))
        
        self.console.print()
        time.sleep(1.5)