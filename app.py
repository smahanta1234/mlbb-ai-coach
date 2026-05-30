import streamlit as st

from src.guide_generator import generate_guide
from src.data_loader import heroes_data
from src.ui_analysis import (
    calculate_draft_score,
    get_draft_verdict,
    detect_win_condition
)
from src.hero_cards import build_hero_card
from src.voiceover import generate_voiceover
st.markdown(
    """
    <style>

    /* Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a, #020617);
        color: #e2e8f0;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0b1220;
    }

    /* Title */
    h1 {
        color: #38bdf8;
        font-weight: 800;
    }

    /* Buttons */
    .stButton button {
        background: linear-gradient(90deg, #2563eb, #06b6d4);
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        border: none;
    }

    .stButton button:hover {
        transform: scale(1.02);
    }

    /* Text areas */
    textarea {
        background-color: #0b1220 !important;
        color: #e2e8f0 !important;
    }

    /* Cards */
    .card {
        background-color: #0b1220;
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #1e293b;
        margin-bottom: 1rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)
hero_list = list(heroes_data["heroes"].keys())

st.set_page_config(
    page_title="MLBB AI Coach",
    page_icon="🎮",
    layout="wide"
)

# =========================
# MAIN PAGE
# =========================

st.title("🎮 MLBB AI Coach")

st.markdown("Elite Draft & Gameplay Analysis System")

st.markdown(
    """
    <div class="card">
    <h3>🧠 How to Use MLBB AI Coach</h3>

    <p>
    This tool analyzes your gameplay transcript and generates high-level coaching insights used in competitive MLBB analysis.
    </p>

    <ul>
        <li>📌 Select your hero, lane, and playstyle on the left panel</li>
        <li>📜 Paste or upload your gameplay transcript</li>
        <li>📊 Click <b>Generate Analysis</b> to receive structured coaching</li>
        <li>🎯 Review strengths, weaknesses, macro & micro improvements</li>
    </ul>

    <p>
    <b>Tip:</b> The more detailed your transcript, the more accurate the coaching becomes.
    </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# 3-COLUMN LAYOUT
# =========================

left, center, right = st.columns([1, 2, 2])

# =========================
# LEFT PANEL — SETTINGS
# =========================
with left:
    st.markdown("## ⚙️ Draft Controls")

    hero = st.selectbox("Hero", hero_list)

    lane = st.selectbox(
        "Lane",
        ["Auto Detect", "Jungle", "Gold", "Mid", "EXP", "Roam"]
    )

    selected_playstyle = st.multiselect(
    "Playstyle",
    [
        "Burst",
        "Sustain",
        "Utility",
        "Pickoff",
        "Split Push",
        "Teamfight",
        "Scaling",
        "Aggressive Early",
        "Macro Control",
        "High Mobility",
        "Snowball",
        "Damage",
        "Poke",
        "Regen",
        "Crowd Control",
        "Finisher",
        "Initiator",
        "Guard",
        "Support",
        "Mobility",
        "Chase"
    ]
)

    guide_type = st.selectbox(
        "Guide Type",
        [
            "Beginner Guide",
            "Rank Push Guide",
            "Macro Analysis",
            "Micro Mechanics",
            "Draft Strategy"
        ]
    )

    difficulty = st.select_slider(
        "Difficulty",
        ["Easy", "Intermediate", "Advanced", "Professional"]
    )
    ally_team = st.multiselect(
    "Select Ally Team",
    hero_list,
    max_selections=5,
    key="ally_team"
)

enemy_team = st.multiselect(
    "Select Enemy Team",
    hero_list,
    max_selections=5,
    key="enemy_team"
)
# =========================
# CENTER PANEL — INPUT
# =========================
with center:
    st.markdown("## 📜 Gameplay Transcript")

    uploaded_file = st.file_uploader(
        "Upload Transcript",
        type=["txt", "md"]
    )

    transcript = ""

    if uploaded_file is not None:
        transcript = uploaded_file.read().decode("utf-8")
        st.success("Transcript loaded!")

    transcript = st.text_area(
        "Or paste transcript",
        transcript,
        height=350
    )

# =========================
# RIGHT PANEL — OUTPUT
# =========================
with right:
    st.markdown("## 📊 AI Coach Panel")

    generate = st.button("Generate Analysis")

    if generate:

        if transcript.strip() == "":
            st.warning("Add a transcript first.")

        else:
            with st.spinner("Analyzing MLBB match..."):

                output = generate_guide(
                    transcript=transcript,
                    hero=hero,
                    lane=lane,
                    playstyle=selected_playstyle,
                    guide_type=guide_type,
                    difficulty=difficulty,
                    ally_team=ally_team,
                    enemy_team=enemy_team
                )

            st.success("Analysis Complete")
            # =========================
            # DRAFT ANALYTICS
            # =========================

            draft_score = calculate_draft_score(
                ally_team,
                enemy_team
            )

            draft_verdict = get_draft_verdict(draft_score)

            win_condition = detect_win_condition(selected_playstyle)

            st.markdown(
    f"""
    <div class="card">
        <h3>📊 Draft Strength</h3>
        <h1>{draft_score}/100</h1>
        <p>{draft_verdict}</p>
    </div>
    """,
    unsafe_allow_html=True
)

            st.progress(draft_score / 100)

# =========================
# WIN CONDITION
# =========================

            st.markdown(
    f"""
    <div class="card">
        <h3>🧠 Recommended Win Condition</h3>
        <p>{win_condition}</p>
    </div>
    """,
    unsafe_allow_html=True
)
            # =========================
# HERO CARDS SECTION
# =========================

st.markdown("## 🃏 Ally Team Composition")

if ally_team:
    cols = st.columns(len(ally_team))

    for i, hero_name in enumerate(ally_team):
        with cols[i]:
            st.markdown(build_hero_card(hero_name), unsafe_allow_html=True)

st.markdown("## ⚔️ Enemy Team Composition")

if enemy_team:
    cols = st.columns(len(enemy_team))

    for i, hero_name in enumerate(enemy_team):
        with cols[i]:
            st.markdown(build_hero_card(hero_name), unsafe_allow_html=True)
            # =========================
            # MAIN OUTPUT CARD
            # =========================
            st.markdown(
                f"""
                <div class="card">
                    <h3>🧠 Hero Analysis</h3>
                    <p>{hero} in {lane} lane</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            # =========================
            # OUTPUT CONTENT
            # =========================
            st.markdown("### 📜 Full Coaching Report")
            st.markdown(output)

            # =========================
            # DOWNLOAD SECTION
            # =========================
            st.markdown("---")

            st.download_button(
                "📥 Download Full Report",
                output,
                file_name=f"{hero.lower()}_mlbb_analysis.md",
                mime="text/markdown"
            )
# =========================
# GENERATION
# =========================

st.subheader("📊 Analysis")

if st.button("Generate MLBB Guide"):

    if transcript.strip() == "":
        st.warning("Please paste a gameplay transcript.")

    else:
        with st.spinner("Analyzing gameplay..."):

            output = generate_guide(
                transcript=transcript,
                hero=hero,
                lane=lane,
                playstyle=selected_playstyle,
                guide_type=guide_type,
                difficulty=difficulty,
                ally_team=ally_team,
                enemy_team=enemy_team
            )

        st.success("Guide generated successfully!")

        st.markdown("## 🧠 AI Coaching Dashboard")

        tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Full Report",
        "⚔️ Draft Insights",
        "🧠 Strategy Breakdown",
        "📦 Download"
        ])
        with tab1:
            st.markdown("### Full AI Analysis")

            st.markdown(output)

        with tab2:
            st.markdown("### Draft Intelligence")

            st.info("AI-generated draft analysis breakdown")

            st.markdown("#### Strengths")
            st.success("• Balanced team composition\n• Good scaling potential")

            st.markdown("#### Weaknesses")
            st.error("• Weak early game presence\n• Limited crowd control")

            st.markdown("#### Recommendations")
            st.warning("• Play for mid game objectives\n• Avoid early forced fights")

        with tab3:
            st.markdown("### Strategy Breakdown")

            with st.expander("📈 Macro Strategy"):
                st.write("Focus on rotations, objectives, and map control.")

            with st.expander("⚔️ Micro Mechanics"):
                st.write("Combo execution, timing, and positioning.")

            with st.expander("❌ Common Mistakes"):
                st.write("Overextending, poor vision control, bad engages.")

            with st.expander("📌 Improvement Plan"):
                st.write("Step-by-step ranked improvement roadmap.")

        with tab4:
            st.markdown("### Export Guide")

            st.download_button(
                label="⬇️ Download Full Analysis",
                data=output,
            file_name=f"{hero}_mlbb_coach.md",
            mime="text/markdown"
        )

        st.info("Save this guide for ranked sessions or replay review.")

        safe_hero = hero.lower().replace(" ", "_")
        safe_lane = lane.lower().replace(" ", "_")
        safe_guide = guide_type.lower().replace(" ", "_")
        if st.button("🎙️ Generate Voiceover"):
            audio_path = generate_voiceover(output)
            st.audio(audio_path)
            
        st.download_button(
            label="⬇️ Download Guide",
            data=output,
            file_name=f"{safe_hero}_{safe_lane}_{safe_guide}.md",
            mime="text/markdown"
        )