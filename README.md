# GAZA Framework v9.0

## 🔴 Cyberpunk Terminal Interface

A professional, modern terminal framework for system administration and analysis with a cyberpunk aesthetic.

```
    ██████╗  █████╗ ███████╗ █████╗ 
   ██╔════╝ ██╔══██╗██╔════╝██╔══██╗
   ██║  ███╗███████║███████╗███████║
   ██║   ██║██╔══██║╚════██║██╔══██║
   ╚██████╔╝██║  ██║███████║██║  ██║
    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

   Snapchat: Gaza9.0k
   Version 9.0
```

## 📋 Features

- **System Monitoring**: Real-time CPU, RAM, and process monitoring
- **Network Tools**: DNS lookup, network information, connectivity tests
- **File Analysis**: File hashing, metadata viewing, directory statistics
- **Plugin System**: Dynamic plugin loading and management
- **Logging**: Comprehensive activity logging
- **Modern UI**: Rich tables, panels, and animations
- **Cyberpunk Theme**: Red and black terminal interface

## 🔧 Requirements

- Python 3.12+
- Linux/macOS (Termux compatible)

## 📦 Installation

### Linux/macOS

```bash
git clone https://github.com/Gaza20-G8/GAZA-Framework-en-public.git
cd GAZA-Framework-en-public
pip install -r requirements.txt
chmod +x main.py
python main.py
```

### Termux (Android)

```bash
pkg install git python
git clone https://github.com/Gaza20-G8/GAZA-Framework-en-public.git
cd GAZA-Framework-en-public
pip install -r requirements.txt
python main.py
```

## 🚀 Usage

```bash
python main.py
```

## 📁 Project Structure

```
GAZA-Framework-en-public/
├── main.py
├── requirements.txt
├── config.json
├── README.md
├── .gitignore
├── core/
│   ├── __init__.py
│   ├── banner.py
│   ├── menu.py
│   ├── animations.py
│   ├── config.py
│   ├── logger.py
│   ├── plugin_loader.py
│   ├── theme.py
│   └── dashboard.py
├── modules/
│   ├── __init__.py
│   ├── system_info.py
│   ├── hardware_info.py
│   ├── process_monitor.py
│   ├── service_monitor.py
│   ├── network_info.py
│   ├── dns_lookup.py
│   ├── ssl_info.py
│   ├── file_analyzer.py
│   ├── metadata_viewer.py
│   ├── hash_generator.py
│   └── log_analyzer.py
├── plugins/
│   └── example_plugin.py
├── assets/
├── logs/
└── exports/
```

## 🎮 Menu Navigation

```
H - Help                      V - Version                   S - Settings                  Q - Quit

SYSTEM:
01 - System Information       02 - Hardware Inventory       03 - User Inventory           04 - Process Monitor
05 - Service Monitor          06 - Event Logs

NETWORK:
07 - Network Information      08 - DNS Lookup               09 - SSL Information          10 - Connectivity Tests
11 - Interface Statistics

FILES:
12 - File Analyzer            13 - Metadata Viewer          14 - Directory Statistics     15 - Hash Generator

UTILITIES:
16 - JSON Viewer              17 - Log Analyzer             18 - Password Generator

PLUGINS:
19 - Plugin Manager
```

## 🔌 Creating Plugins

Create a new file in the `plugins/` directory:

```python
# plugins/my_plugin.py

PLUGIN_NAME = "My Plugin"
PLUGIN_VERSION = "1.0"
PLUGIN_AUTHOR = "Your Name"
PLUGIN_DESCRIPTION = "Description of what my plugin does"

def run():
    """Plugin main execution function"""
    from rich.console import Console
    console = Console()
    console.print("[bold red]My Plugin is running![/bold red]")
```

## 📝 Logging

All activities are logged to `logs/gaza.log` with timestamps and severity levels:
- INFO
- WARNING
- ERROR
- SUCCESS

## ⚙️ Configuration

Edit `config.json` to customize:
- Theme colors (primary, secondary, background)
- Logging level and file location
- Plugin directory
- Dashboard refresh rate

## 🛡️ Error Handling

The framework includes comprehensive error handling that:
- Logs all errors to file
- Displays errors in red panels
- Never crashes the application
- Allows recovery and continuation

## 🎨 Cyberpunk Theme

- **Primary Color**: Bold Red
- **Secondary Color**: White
- **Background**: Black
- **Style**: Terminal Hacker / SOC Dashboard

## 📊 Dashboard Features

Real-time display of:
- Current time and date
- Operating system info
- Python version
- Current user
- RAM usage and availability
- CPU usage percentage
- Total processor information
- System uptime

## 🔐 Security Features

- File hashing (MD5, SHA1, SHA256)
- SSL information display
- Network security tools
- Comprehensive logging for audit trails

## 📄 License

Public Domain - Use freely

## 👤 Author

**Gaza20-G8**
- Snapchat: Gaza9.0k
- GitHub: @Gaza20-G8

## 💬 Support

For issues and questions:
1. Check the logs in `logs/gaza.log`
2. Review the README documentation
3. Create a plugin to extend functionality

---

**GAZA Framework v9.0** - Professional Terminal Interface for Linux/Termux/macOS

Made with ❤️ in cyberpunk red