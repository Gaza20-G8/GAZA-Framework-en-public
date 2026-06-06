"""GAZA Menu Manager Module
Main navigation and command routing
"""

from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.table import Table
import sys

class MenuManager:
    """Main Menu Controller"""
    
    def __init__(self, logger, config):
        self.console = Console()
        self.logger = logger
        self.config = config
        self.running = True
        
    def display_main_menu(self):
        """Display main menu"""
        self.console.clear()
        
        # Top menu
        top_menu = Text("[H] Help    [V] Version    [S] Settings    [Q] Quit", style="bold red")
        self.console.print(Align.center(top_menu))
        self.console.print(Align.center(Text("═" * 80, style="red")))
        self.console.print()
        
        self._display_system_menu()
        self._display_network_menu()
        self._display_files_menu()
        self._display_utilities_menu()
        
    def _display_system_menu(self):
        """Display system menu section"""
        self.console.print(Text("[SYSTEM]", style="bold red"))
        menu_items = [
            "[01] System Information",
            "[02] Hardware Inventory",
            "[03] User Inventory",
            "[04] Process Monitor",
            "[05] Service Monitor",
            "[06] Event Logs",
        ]
        for item in menu_items:
            self.console.print(Text(item, style="yellow"))
        self.console.print(Text("═" * 80, style="red"))
        self.console.print()
        
    def _display_network_menu(self):
        """Display network menu section"""
        self.console.print(Text("[NETWORK]", style="bold red"))
        menu_items = [
            "[07] Network Information",
            "[08] DNS Information",
            "[09] SSL Information",
            "[10] Connectivity Tests",
            "[11] Interface Statistics",
        ]
        for item in menu_items:
            self.console.print(Text(item, style="cyan"))
        self.console.print(Text("═" * 80, style="red"))
        self.console.print()
        
    def _display_files_menu(self):
        """Display files menu section"""
        self.console.print(Text("[FILES]", style="bold red"))
        menu_items = [
            "[12] File Analyzer",
            "[13] Metadata Viewer",
            "[14] Directory Statistics",
            "[15] Hash Generator",
        ]
        for item in menu_items:
            self.console.print(Text(item, style="green"))
        self.console.print(Text("═" * 80, style="red"))
        self.console.print()
        
    def _display_utilities_menu(self):
        """Display utilities menu section"""
        self.console.print(Text("[UTILITIES]", style="bold red"))
        menu_items = [
            "[16] JSON Viewer",
            "[17] Log Analyzer",
            "[18] Password Generator",
        ]
        for item in menu_items:
            self.console.print(Text(item, style="magenta"))
        self.console.print(Text("═" * 80, style="red"))
        self.console.print()
        
        self.console.print(Text("[PLUGINS]", style="bold red"))
        self.console.print(Text("[19] Plugin Manager", style="blue"))
        self.console.print(Text("═" * 80, style="red"))
        self.console.print()
        
    def run(self):
        """Run menu loop"""
        while self.running:
            try:
                self.display_main_menu()
                choice = input(Text("Select > ", style="bold red").plain).strip().upper()
                self._handle_choice(choice)
            except KeyboardInterrupt:
                self.running = False
                self.console.print(Text("\n[red]Framework terminated[/red]"))
                sys.exit(0)
                
    def _handle_choice(self, choice):
        """Handle menu choice"""
        if choice == 'H':
            self._show_help()
        elif choice == 'V':
            self._show_version()
        elif choice == 'S':
            self._show_settings()
        elif choice == 'Q':
            self.running = False
            self.console.print(Text("[green]Goodbye![/green]"))
            sys.exit(0)
        elif choice == '01':
            self._show_system_info()
        elif choice == '02':
            self._show_hardware_info()
        elif choice == '04':
            self._show_process_monitor()
        elif choice == '07':
            self._show_network_info()
        elif choice == '12':
            self._show_file_analyzer()
        elif choice == '15':
            self._show_hash_generator()
        elif choice == '17':
            self._show_log_analyzer()
        else:
            self.console.print(Text("[red]✗ Invalid choice[/red]"))
            input("Press Enter to continue...")
            
    def _show_help(self):
        """Show help information"""
        help_panel = Panel(
            """GAZA Framework v9.0 - Help
            
System Commands:
[yellow]•[/yellow] Use numbers to access modules
[yellow]•[/yellow] Type [bold]H[/bold] for Help
[yellow]•[/yellow] Type [bold]V[/bold] for Version
[yellow]•[/yellow] Type [bold]S[/bold] for Settings  
[yellow]•[/yellow] Type [bold]Q[/bold] to Quit

Modules:
[cyan]01-06:[/cyan] System information and monitoring
[cyan]07-11:[/cyan] Network analysis tools
[cyan]12-15:[/cyan] File system utilities
[cyan]16-18:[/cyan] General utilities
[cyan]19:[/cyan] Plugin management""",
            title="[bold red]HELP[/bold red]",
            style="cyan"
        )
        self.console.print(help_panel)
        input("Press Enter to continue...")
        
    def _show_version(self):
        """Show version information"""
        version_panel = Panel(
            """[bold red]GAZA Framework v9.0[/bold red]

Snapchat: Gaza9.0k
Author: Gaza20-G8

Cyberpunk Terminal Interface
Modern System Administration Tool""",
            title="[bold red]VERSION[/bold red]",
            style="yellow"
        )
        self.console.print(version_panel)
        input("Press Enter to continue...")
        
    def _show_settings(self):
        """Show settings menu"""
        self.console.clear()
        self.console.print(Panel("[bold red]SETTINGS[/bold red]", style="red"))
        self.console.print(Text("[1] Change Theme", style="cyan"))
        self.console.print(Text("[2] Enable Logging", style="cyan"))
        self.console.print(Text("[3] Disable Logging", style="cyan"))
        self.console.print(Text("[4] Export Settings", style="cyan"))
        self.console.print(Text("[5] Reset Configuration", style="cyan"))
        self.console.print(Text("[6] Back to Menu", style="cyan"))
        input("Press Enter to continue...")
        
    def _show_system_info(self):
        """Show system info"""
        from modules import system_info
        system_info.show_system_info()
        
    def _show_hardware_info(self):
        """Show hardware info"""
        from modules import hardware_info
        hardware_info.show_hardware_info()
        
    def _show_process_monitor(self):
        """Show process monitor"""
        from modules import process_monitor
        process_monitor.show_process_monitor()
        
    def _show_network_info(self):
        """Show network info"""
        from modules import network_info
        network_info.show_network_info()
        
    def _show_file_analyzer(self):
        """Show file analyzer"""
        from modules import file_analyzer
        file_analyzer.show_file_analyzer()
        
    def _show_hash_generator(self):
        """Show hash generator"""
        from modules import hash_generator
        hash_generator.show_hash_generator()
        
    def _show_log_analyzer(self):
        """Show log analyzer"""
        from modules import log_analyzer
        log_analyzer.show_log_analyzer()