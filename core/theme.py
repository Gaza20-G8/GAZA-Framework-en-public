"""GAZA Theme Manager Module
Color and style management
"""

from rich.style import Style
from rich.theme import Theme

class ThemeManager:
    """Theme manager"""
    
    CYBERPUNK_THEME = Theme({
        "primary": "bold red",
        "secondary": "bold white",
        "accent": "yellow",
        "success": "bold green",
        "error": "bold red",
        "warning": "bold yellow",
        "info": "bold cyan",
    })
    
    @classmethod
    def get_cyberpunk_theme(cls) -> Theme:
        """Get cyberpunk theme"""
        return cls.CYBERPUNK_THEME