from pathlib import Path
import sys

# Add the root directory to Python path
root_dir = str(Path(__file__).parent.parent)
if root_dir not in sys.path:
    sys.path.append(root_dir)

from webui import create_ui
from src.utils.default_config_settings import default_config

# Get default configuration
config = default_config()

# Create the Gradio interface
demo = create_ui(config)

# For Vercel serverless deployment
app = demo.app