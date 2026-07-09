import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATABASE_PATH = BASE_DIR / "data" / "database" / "pathfinder.db"

def create_database():
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            education TEXT,
            branch TEXT,
            current_year TEXT,
            cgpa REAL,
            experience_years REAL,
            timeline_months INTEGER,
            learning_hours_week INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_skills (
            skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            skill_name TEXT,
            proficiency TEXT,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_preferences (
            preference_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            preference_type TEXT,
            preference_value TEXT,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS roles (
            role_id INTEGER PRIMARY KEY,
            role_name TEXT,
            industry TEXT,
            domain TEXT,
            role_description TEXT,
            entry_level TEXT,
            minimum_experience_years REAL,
            average_salary_lpa REAL,
            market_demand_score INTEGER,
            competition_score INTEGER,
            growth_score INTEGER,
            automation_risk_score INTEGER,
            preparation_months INTEGER,
            coding_intensity INTEGER,
            mathematics_intensity INTEGER,
            communication_intensity INTEGER,
            work_life_balance INTEGER,
            work_mode TEXT,
            travel_required TEXT,
            client_interaction TEXT,
            leadership_required TEXT,
            networking_required TEXT,
            shift_type TEXT,
            remote_opportunity TEXT,
            required_skills TEXT,
            preferred_skills TEXT,
            recommended_certifications TEXT,
            portfolio_required TEXT,
            future_growth_roles TEXT,
            role_characteristics TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS skill_taxonomy (
            skill_id INTEGER PRIMARY KEY,
            skill_name TEXT,
            category TEXT,
            subcategory TEXT,
            description TEXT,
            importance_level TEXT,
            is_active TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS career_verdicts (
            verdict_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            role_id INTEGER,
            skill_match INTEGER,
            timeline_match INTEGER,
            final_score INTEGER,
            verdict TEXT,
            reasons TEXT,
            risks TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            FOREIGN KEY(role_id) REFERENCES roles(role_id)
        )
        """)

        conn.commit()
        conn.close()
        print("Database Created Successfully")

if __name__ == "__main__":
    create_database()