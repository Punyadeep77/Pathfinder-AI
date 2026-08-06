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

from config.constants import (
    SEED_ROLES_FILE,
    PROCESSED_ROLES_FILE,
)

from scripts.generate_seed_dataset import create_seed_roles
from scripts.generate_skill_taxonomy import create_skill_taxonomy

from src.utils.etl_pipeline import ETLPipeline
from src.database.schema import create_database
from src.database.loader import import_all


def print_header():
    print("=" * 60)
    print("PATHFINDER AI - DATA PIPELINE")
    print("=" * 60)


def print_success():
    print("\n" + "=" * 60)
    print("PATHFINDER DATA PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)


def print_failure(error):
    print("\n" + "=" * 60)
    print("PATHFINDER DATA PIPELINE FAILED")
    print("=" * 60)
    print(f"Error: {error}")


def generate_seed_data():
    print("\n[1/5] Generating Seed Roles...")
    create_seed_roles()

    print("\n[2/5] Generating Skill Taxonomy...")
    create_skill_taxonomy()


def run_etl():
    print("\n[3/5] Running ETL Pipeline...")

    pipeline = ETLPipeline(
        input_file=SEED_ROLES_FILE,
        output_file=PROCESSED_ROLES_FILE,
    )

    pipeline.run()


def initialize_database():
    print("\n[4/5] Creating Database...")
    create_database()

    print("\n[5/5] Importing Processed Dataset...")
    import_all()


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