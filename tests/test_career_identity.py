from src.models.career_identity import CareerIdentity

def test_career_identity():
    user = CareerIdentity(
        name="Punyadeep",
        education="B.Tech",
        branch="Data Science",
        current_year="3rd Year",
        cgpa=7.92,
        experience_years=0,
        
        skills={
            "Python":"Intermediate",
            "SQL":"Beginner",
            "Pandas":"Intermediate"
        },
        
        timeline_months=8,
        learning_hours_week=20,
        positive_preferences=[
            "Analytics",
            "AI"
        ],
        
        negative_preferences=[
            "DevOps",
            "Networking"
        ],
        
        career_interests=[
            "Data Science",
            "Machine Learning"
        ]
    )
    
    print(user)
    print()
    print(user.total_skills())
    print(user.has_skill("Python"))
    print(user.get_skill_level("Python"))

if __name__ == "__main__":
    test_career_identity()