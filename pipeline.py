"""
Pathfinder AI
Master Pipeline

Flow
-----
Generate Seed Roles
        ↓
Generate Skill Taxonomy
        ↓
Run ETL Pipeline
        ↓
Create Database
        ↓
Import Clean Data into SQLite
"""

from config.settings import (
    SEED_ROLES_FILE,
    PROCESSED_ROLES_FILE,
)
from scripts.generate_seed_dataset import create_seed_roles
from scripts.generate_skill_taxonomy import create_skill_taxonomy

from src.utils.etl_pipeline import ETLPipeline
from src.database.schema import create_database
from src.database.loader import DatabaseLoader

from config.logging_config import get_logger
logger = get_logger(__name__)

def print_header():
   logger.info("=" * 60)
   logger.info("PATHFINDER AI - DATA PIPELINE")
   logger.info("=" * 60)


def print_success():
    logger.info("\n" + "=" * 60)
    logger.info("PATHFINDER DATA PIPELINE COMPLETED SUCCESSFULLY")
    logger.info("=" * 60)


def print_failure(error):
    logger.error("\n" + "=" * 60)
    logger.error("PATHFINDER DATA PIPELINE FAILED")
    logger.error("=" * 60)
    logger.exception(f"Error: {error}")


def generate_seed_data():
    logger.info("\n[1/5] Generating Seed Roles...")
    create_seed_roles()

    logger.info("\n[2/5] Generating Skill Taxonomy...")
    create_skill_taxonomy()


def run_etl():
    logger.info("\n[3/5] Running ETL Pipeline...")

    pipeline = ETLPipeline(
        input_file=SEED_ROLES_FILE,
        output_file=PROCESSED_ROLES_FILE,
    )

    pipeline.run()


def initialize_database():
    logger.info("\n[4/5] Creating Database...")
    create_database()

    logger.info("[5/5] Importing Processed Dataset...")

    loader = DatabaseLoader()
    loader.import_all()


def main():
    try:
        print_header()

        generate_seed_data()

        run_etl()

        initialize_database()

        print_success()

    except Exception as error:
        print_failure(error)


if __name__ == "__main__":
    main()