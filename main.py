from src.context.context_engine import ContextEngine
from src.services.recommendation_service import RecommendationService


def main():

    print("\n========== PATHFINDER AI ==========\n")

    user_input = input(
        "Tell me about yourself, your situation, "
        "career goal, skills, and constraints:\n\n> "
    )

    context_engine = ContextEngine()

    context = context_engine.understand(user_input)

    # Ask only for missing required information.
    while context.has_missing_constraints():

        question = context_engine.get_clarification(context)

        print(f"\nPathfinder: {question}")

        answer = input("> ")

        constraint = context.missing_required_constraints[0]

        context = context_engine.resolve_missing_constraints(
            context,
            {
                constraint: answer
            }
        )

    user = context_engine.build_identity(context)

    print(
        "\nPathfinder: I have enough information. "
        "Analyzing your profile...\n"
    )

    recommendation_service = RecommendationService()

    recommendations = recommendation_service.recommend(user)

    print(
        "\n========== TOP CAREER RECOMMENDATIONS ==========\n"
    )

    for index, verdict in enumerate(
        recommendations[:5],
        start=1
    ):

        print(f"{index}. {verdict.role_name}")
        print(f"Verdict : {verdict.verdict}")

        print(
            f"Skill Match : "
            f"{verdict.skill_match}%"
        )

        print(
            f"Career Interest Match : "
            f"{verdict.career_interest_match}%"
        )

        print(
            f"Timeline Match : "
            f"{verdict.timeline_match_score}%"
        )

        print(
            f"Timeline Gap : "
            f"{verdict.timeline_gap_months} month(s)"
        )

        print(
            f"Final Score : "
            f"{verdict.final_score}"
        )

        print(
            f"Average Salary : "
            f"{verdict.average_salary_lpa} LPA"
        )

        if verdict.missing_skills:
            print(
                "Missing Skills :",
                ", ".join(verdict.missing_skills)
            )

        if verdict.portfolio_required == "Yes":
            print(
                "Portfolio Required : Yes"
            )

        print("Strengths :")

        if verdict.strengths:
            for item in verdict.strengths:
                print("  •", item)
        else:
            print("  None")

        print("Limitations :")

        if verdict.limitations:
            for item in verdict.limitations:
                print("  •", item)
        else:
            print("  None")

        print("Risks :")

        if verdict.risks:
            for item in verdict.risks:
                print("  •", item)
        else:
            print("  None")

        print("-" * 60)


if __name__ == "__main__":
    main()