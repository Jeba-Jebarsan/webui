import argparse
from webui import create_ui
from src.utils.default_config_settings import default_config

def main():
    parser = argparse.ArgumentParser(description="Custom Browser Agent UI")
    parser.add_argument("--port", type=int, default=7788)
    parser.add_argument("--host", type=str, default="127.0.0.1")
    args = parser.parse_args()
    
    # Get default configuration
    config = default_config()
    
    # Create and launch UI
    demo = create_ui(config)
    demo.launch(
        server_name=args.host,
        server_port=args.port,
        show_api=False
    )

if __name__ == "__main__":
    main()