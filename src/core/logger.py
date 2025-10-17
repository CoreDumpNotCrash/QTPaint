"""logger.py is for customized logs and errors"""

from core import config

def log(msg: str):
    if not config.DEBUG_MODE:
        return
    
    print(f"\033[32m[LOG]\033[0m {msg}")