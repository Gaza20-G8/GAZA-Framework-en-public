"""GAZA Logging Module
File and console logging
"""

import logging
from pathlib import Path
from datetime import datetime
from rich.console import Console

class Logger:
    """GAZA Logger"""
    
    def __init__(self, log_dir: Path):
        self.log_dir = log_dir
        self.log_dir.mkdir(exist_ok=True)
        self.console = Console()
        
        self.logger = logging.getLogger("GAZA")
        self.logger.setLevel(logging.DEBUG)
        
        # Remove existing handlers
        self.logger.handlers.clear()
        
        # File handler
        log_file = self.log_dir / "gaza.log"
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        
    def info(self, message: str):
        """Log info message"""
        self.logger.info(message)
        self.console.print(f"[cyan]ℹ {message}[/cyan]")
        
    def success(self, message: str):
        """Log success message"""
        self.logger.info(message)
        self.console.print(f"[green]✓ {message}[/green]")
        
    def warning(self, message: str):
        """Log warning message"""
        self.logger.warning(message)
        self.console.print(f"[yellow]⚠ {message}[/yellow]")
        
    def error(self, message: str):
        """Log error message"""
        self.logger.error(message)
        self.console.print(f"[red]✗ {message}[/red]")
        
    def debug(self, message: str):
        """Log debug message"""
        self.logger.debug(message)