import streamlit as st

from src.context.context_engine import ContextEngine
from src.services.discussion_service import EvidenceDiscussionService
from src.services.recommendation_service import RecommendationService


st.set_page_config(page_title="Pathfinder AI", page_icon="🧭", layout="wide")


def reset_analysis():
    for key in ("context", "recommendations", "source_text"):
        st.session_state.pop(key, None)


def show_verdict(verdict):
    st.subheader(verdict.role_name)
    st.caption(f"{verdict.verdict} · score {verdict.final_score}/100")
    metrics = st.columns(4)
    metrics[0].metric("Skill match", f"{verdict.skill_match}%")
    metrics[1].metric("Interest alignment", f"{verdict.career_interest_match}%")
    metrics[2].metric("Timeline match", f"{verdict.timeline_match_score}%")
    metrics[3].metric("Market demand", f"{verdict.market_demand_score}/100")

    evidence, risks = st.columns(2)
    with evidence:
        st.markdown("**Evidence**")
        for reason in verdict.reasons:
            st.write(f"• {reason}")
        if verdict.missing_skills:
            st.write("**Missing skills:** " + ", ".join(verdict.missing_skills))
        st.write(f"**Average salary:** {verdict.average_salary_lpa} LPA")
    with risks:
        st.markdown("**Reality check**")
        items = verdict.risks + verdict.limitations
        if items:
            for item in items:
                st.write(f"• {item}")
        else:
            st.write("No major risks identified from available evidence.")


st.title("🧭 Pathfinder AI")
st.caption("Evidence-driven career decision intelligence")

with st.sidebar:
    st.header("Your situation")
    if st.button("Start a new analysis", use_container_width=True):
        reset_analysis()
        st.rerun()

if "context" not in st.session_state:
    situation = st.text_area(
        "Describe your situation naturally",
        placeholder=(
            "Example: I am a 3rd-year BTech student with intermediate Python, SQL "
            "and Pandas. I want to become a data analyst in 8 months, can study 20 "
            "hours a week, and do not want heavy networking."
        ),
        height=180,
    )
    if st.button("Understand my situation", type="primary"):
        if not situation.strip():
            st.error("Please describe your situation before continuing.")
        else:
            st.session_state.source_text = situation
            st.session_state.context = ContextEngine().understand(situation)
            st.rerun()

if "context" in st.session_state and "recommendations" not in st.session_state:
    engine = ContextEngine()
    context = st.session_state.context
    st.info(f"Detected user type: {context.user_type.replace('_', ' ')}")
    offer_lpa = context.extracted_information.get("existing_offer_lpa")
    if offer_lpa is not None:
        label = context.extracted_information.get("existing_offer_label")
        st.caption(f"Current offer recorded: {label} — ₹{offer_lpa:.2f} LPA")
    if context.has_missing_constraints():
        constraint = context.missing_required_constraints[0]
        answer = st.text_input(engine.get_clarification(context), key=f"answer_{constraint}")
        if st.button("Continue", type="primary"):
            if not answer.strip():
                st.error("Please provide an answer to continue.")
            else:
                st.session_state.context = engine.resolve_missing_constraints(context, {constraint: answer})
                st.rerun()
    else:
        try:
            user = engine.build_identity(context)
            st.session_state.recommendations = RecommendationService().recommend(user)
            st.rerun()
        except Exception as error:
            st.error(f"Pathfinder could not analyze this profile: {error}")

if "recommendations" in st.session_state:
    service = RecommendationService()
    offer_lpa = st.session_state.context.extracted_information.get("existing_offer_lpa")
    if offer_lpa is not None:
        label = st.session_state.context.extracted_information.get("existing_offer_label")
        st.info(f"Current offer benchmark: {label} — ₹{offer_lpa:.2f} LPA")
    primary, exploration = service.split_primary_and_exploration(st.session_state.recommendations)
    primary_tab, explore_tab, discussion_tab = st.tabs(
        ["Primary recommendations", "Explore more options", "Evidence discussion"]
    )
    with primary_tab:
        st.write("These roles are supported by Pathfinder's decision system.")
        if not primary:
            st.warning("No role is currently recommended without important trade-offs.")
        for verdict in primary[:5]:
            with st.container(border=True):
                show_verdict(verdict)
    with explore_tab:
        st.write("These are additional options, not primary recommendations.")
        for verdict in exploration:
            with st.expander(f"{verdict.role_name} — {verdict.verdict}"):
                show_verdict(verdict)
    with discussion_tab:
        candidates = primary or st.session_state.recommendations
        selected_name = st.selectbox("Discuss a role", [item.role_name for item in candidates])
        selected = next(item for item in candidates if item.role_name == selected_name)
        question = st.text_input(
            "Ask about its evidence",
            placeholder="Why is this recommended? What skills are missing? What are the risks?",
        )
        if question:
            st.write(EvidenceDiscussionService().answer(question, selected))
        st.caption("This local-first discussion uses verified Pathfinder evidence and cannot override a verdict.")
