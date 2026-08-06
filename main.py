from src.engines.identity.identity_engine import IdentityEngine
from src.services.recommendation_service import RecommendationService


def main():

    profile = {
        "name": "Punyadeep",
        "education": "B.Tech",
        "branch": "Data Science",
        "current_year": "3rd Year",
        "cgpa": 8.0,
        "experience_years": 0,
        "timeline_months": 8,
        "learning_hours_week": 20,

        "skills": {
            "Python": "Intermediate",
            "SQL": "Intermediate",
            "Pandas": "Intermediate",
            "Excel": "Advanced",
            "Power BI": "Beginner"
        },

        "positive_preferences": [
            "Hybrid"
        ],

        "negative_preferences": [
            "Night Shift"
        ],

        "career_interests": [
            "Data Science",
            "Artificial Intelligence"
        ]
    }

    identity_engine = IdentityEngine()
    user = identity_engine.build_identity(profile)

    recommendation_service = RecommendationService()

    recommendations = recommendation_service.recommend(user)

    print("\n========== TOP CAREER RECOMMENDATIONS ==========\n")

    for index, verdict in enumerate(recommendations[:5], start=1):

        print(f"{index}. {verdict.role_name}")
        print(f"Verdict : {verdict.verdict}")
        print(f"Skill Match : {verdict.skill_match}%")
        print(f"Final Score : {verdict.final_score}")
        print(f"Average Salary : {verdict.average_salary_lpa} LPA")

        if verdict.missing_skills:
            print("Missing Skills :", ", ".join(verdict.missing_skills))

        print("Strengths :")
        for item in verdict.strengths:
            print("  •", item)

        print("Risks :")
        if verdict.risks:
            for item in verdict.risks:
                print("  •", item)
        else:
            print("  None")

        print("-" * 60)


if __name__ == "__main__":
    main()