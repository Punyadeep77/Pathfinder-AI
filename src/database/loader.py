import pandas as pd

from config.logging_config import get_logger
from config.settings import (
    SEED_DIR,
    PROCESSED_DATA_DIR,
)

from src.database.connection import (
    get_connection,
    execute_query,
)

logger = get_logger(__name__)


class DatabaseLoader:
    """
    Loads cleaned datasets into the Pathfinder database.
    """

    def import_roles(self):
        logger.info("Importing career roles into database...")

        df = pd.read_csv(PROCESSED_DATA_DIR / "seed_roles_clean.csv")

        execute_query("DELETE FROM roles")

        conn = get_connection()
        df.to_sql("roles", conn, if_exists="append", index=False)
        conn.close()

        logger.info(f"{len(df)} career roles imported successfully.")

    def import_skill_taxonomy(self):
        logger.info("Importing skill taxonomy into database...")

        df = pd.read_csv(SEED_DIR / "skill_taxonomy.csv")

        execute_query("DELETE FROM skill_taxonomy")

        conn = get_connection()
        df.to_sql("skill_taxonomy", conn, if_exists="append", index=False)
        conn.close()

        logger.info(f"{len(df)} skills imported successfully.")

    def import_all(self):
        logger.info("Starting database import process...")

        self.import_roles()
        self.import_skill_taxonomy()

        logger.info("Database seeded successfully.")


if __name__ == "__main__":
    loader = DatabaseLoader()
    loader.import_all()