from src.engines.identity.identity_engine import IdentityEngine

def test_identity_engine():

    profile = {
        "name": "Punyadeep",
        "education": "B.Tech",
        "branch": "Data Science",
        "current_year": "3rd Year",
        "cgpa": 7.92,
        "experience_years": 0,
        "timeline_months": 8,
        "learning_hours_week": 20,
        "skills": {
            "Python": "Intermediate",
            "SQL": "Beginner",
            "Pandas": "Intermediate"
        },
        "positive_preferences": [
            "Analytics",
            "AI"
        ],
        "negative_preferences": [
            "DevOps",
            "Networking"
        ],
        "career_interests": [
            "Data Science",
            "Machine Learning"
        ]
    }

    engine = IdentityEngine()
    user = engine.build_identity(profile)
    print(user)

if __name__ == "__main__":
    test_identity_engine()