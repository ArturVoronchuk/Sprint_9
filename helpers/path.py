from pathlib import Path

APP_DIR = Path(__file__).parent.parent
ASSETS_DIR = APP_DIR / "assets"

def get_asset_path(filename: str) -> str:
    return str(ASSETS_DIR / filename)