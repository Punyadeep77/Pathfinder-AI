from pathlib import Path
import pandas as pd

from src.database.connection import (get_connection,execute_query)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SEED_FOLDER = BASE_DIR / "data" / "seed"
PROCESSED_FOLDER = BASE_DIR / "data" / "processed"

class DatabaseLoader:
    """
    Loads cleaned datasets into the Pathfinder database.
    """
    def import_roles(self):
        df = pd.read_csv(PROCESSED_FOLDER / "seed_roles_clean.csv")
        
        execute_query("DELETE FROM roles")
        
        conn = get_connection()
        df.to_sql("roles",conn,if_exists="append",index=False)

        conn.close()
        print(f"{len(df)} Roles Imported")

    def import_skill_taxonomy(self):
        df = pd.read_csv(SEED_FOLDER / "skill_taxonomy.csv")

        execute_query("DELETE FROM skill_taxonomy")
        conn = get_connection()

        df.to_sql("skill_taxonomy",conn,if_exists="append",index=False)

        conn.close()
        print(f"{len(df)} Skills Imported")

    def import_all(self):
        self.import_roles()
        self.import_skill_taxonomy()
        print("\nDatabase Seeded Successfully")

if __name__ == "__main__":
    loader = DatabaseLoader()
    loader.import_all()