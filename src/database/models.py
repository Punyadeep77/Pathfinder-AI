from src.database.connection import (fetch_all,fetch_one)

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