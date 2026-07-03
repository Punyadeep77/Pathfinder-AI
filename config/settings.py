from pathlib import Path

# Root directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
DATABASE_DIR = DATA_DIR / "database"
SEED_DIR = DATA_DIR / "seed"

# Database
DATABASE_NAME = "pathfinder.db"
DATABASE_PATH = DATABASE_DIR / DATABASE_NAME