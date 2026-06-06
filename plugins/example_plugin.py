"""
Example Plugin for GAZA Framework
This is a template for creating new plugins
"""

PLUGIN_NAME = "Example Plugin"
PLUGIN_VERSION = "1.0"
PLUGIN_AUTHOR = "Gaza20-G8"
PLUGIN_DESCRIPTION = "This is an example plugin template for GAZA Framework"

def run():
    """
    Main plugin execution function
    This is called when the plugin is activated
    """
    from rich.console import Console
    from rich.panel import Panel
    
    console = Console()
    
    panel = Panel(
        "[bold red]Example Plugin Running![/bold red]\n\nThis is a template for creating new plugins.\nModify this file to add your own functionality.",
        title="[bold cyan]Example Plugin[/bold cyan]",
        style="magenta"
    )
    console.print(panel)
    
    input("\nPress Enter to continue...")