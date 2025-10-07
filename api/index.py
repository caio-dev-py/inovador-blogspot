import sys
import os

# Ajusta o sys.path para encontrar o src/app
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app', 'src', 'app'))

from src.app import create_app

app = create_app()