from pathlib import Path
import pandas as pd

from src.database.connection import (
    get_connection,
    execute_query,
    fetch_all,
    fetch_one
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SEED_FOLDER = BASE_DIR / "data" / "seed"

def import_roles():
    df = pd.read_csv(
        SEED_FOLDER / "seed_roles.csv"
    )

    execute_query(
        "DELETE FROM roles"
    )

    conn = get_connection()

    df.to_sql(
        "roles",
        conn,
        if_exists="append",
        index=False
    )

    conn.close()
    print(f"{len(df)} Roles Imported")

def import_skill_taxonomy():
    df = pd.read_csv(
        SEED_FOLDER / "skill_taxonomy.csv"
    )

    execute_query(
        "DELETE FROM skill_taxonomy"
    )

    conn = get_connection()

    df.to_sql(
        "skill_taxonomy",
        conn,
        if_exists="append",
        index=False
    )

    conn.close()
    print(f"{len(df)} Skills Imported")

def get_all_roles():
    return fetch_all("""
        SELECT *
        FROM roles
        ORDER BY role_name
    """)

def get_role(role_id):
    return fetch_one("""
        SELECT *
        FROM roles
        WHERE role_id = ?
    """, (role_id,))

def get_all_skills():
    return fetch_all("""
        SELECT *
        FROM skill_taxonomy
        ORDER BY category, skill_name
    """)

def get_skill(skill_name):
    return fetch_one("""
        SELECT *
        FROM skill_taxonomy
        WHERE skill_name = ?
    """, (skill_name,))

if __name__ == "__main__":
    import_roles()
    import_skill_taxonomy()
    print("\nDatabase Seeded Successfully")

