import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
web_dir = os.path.join(BASE_DIR, "web")
if web_dir not in sys.path:
    sys.path.insert(0, web_dir)

from server import app
