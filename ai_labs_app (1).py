import streamlit as st
import time
import json
import random

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Labs — L&D Division",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── GLOBAL CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ── Design tokens ──────────────────────────────────────────────────────── */
:root {
    --c-primary:    #0F3D61;   /* deep corporate navy — primary brand */
    --c-primary-2:  #15517F;   /* lighter navy for gradients/hover */
    --c-accent:     #C5821A;   /* single muted amber accent */
    --c-success:    #1E8449;   /* status only */
    --c-error:      #B03A2E;   /* status only */
    --c-ink:        #1B2430;   /* body text */
    --c-muted:      #6B7785;   /* secondary text */
    --c-line:       #E3E7EC;   /* borders */
    --c-surface:    #FFFFFF;
    --c-bg:         #F4F6F9;
    --radius:       10px;
    --shadow-sm:    0 1px 2px rgba(15,61,97,0.06);
    --shadow-md:    0 4px 14px rgba(15,61,97,0.08);
    --sp-1: 4px; --sp-2: 8px; --sp-3: 12px; --sp-4: 16px; --sp-5: 24px; --sp-6: 32px;
}

html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: var(--c-ink); }
.main { background: var(--c-bg); }

/* ── Typographic scale ──────────────────────────────────────────────────── */
h2 { font-size: 24px !important; font-weight: 800 !important; color: var(--c-primary) !important;
     letter-spacing: -0.3px; margin-bottom: var(--sp-1) !important; }
h3 { font-size: 16px !important; font-weight: 700 !important; color: var(--c-primary) !important; }
h4 { font-size: 14px !important; font-weight: 600 !important; }

/* ── Sidebar ───────────────────────────────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, var(--c-primary) 0%, #0B2C46 100%) !important;
    border-right: 1px solid rgba(255,255,255,0.06);
}
section[data-testid="stSidebar"] * { color: #FFFFFF !important; }
section[data-testid="stSidebar"] .block-container { padding-top: 28px; }

.sb-brand-title { font-size: 16px; font-weight: 800; letter-spacing: 0.2px; margin-bottom: 2px; }
.sb-brand-sub   { font-size: 12px; color: #A9C2D9 !important; font-weight: 500; }
.sb-brand-org   { font-size: 11px; color: #6F93B3 !important; margin-top: 1px; }

section[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.12) !important; margin: 18px 0 !important; }

section[data-testid="stSidebar"] .stRadio label {
    color: #B8CCDF !important; font-size: 13.5px !important; font-weight: 500 !important;
    padding: 2px 0;
}
section[data-testid="stSidebar"] .stRadio div[data-checked="true"] label {
    color: #FFFFFF !important; font-weight: 700 !important;
}

.sb-progress-label { font-size: 11px; font-weight: 700; letter-spacing: 0.6px; text-transform: uppercase;
    color: #7FA3C2 !important; margin-bottom: 6px; }
.sb-lab-status { font-size: 12.5px !important; color: #C9DAE8 !important; padding: 3px 0; }
.sb-lab-status.done { color: #FFFFFF !important; font-weight: 600; }

.sb-footer { font-size: 10.5px !important; color: #5F84A4 !important; line-height: 1.6; }

/* ── Cards ─────────────────────────────────────────────────────────────── */
.lab-card {
    background: var(--c-surface);
    border-radius: var(--radius);
    padding: var(--sp-4) var(--sp-5);
    margin: var(--sp-3) 0;
    border-left: 4px solid var(--c-primary);
    box-shadow: var(--shadow-sm);
    height: 100%;
}
.lab-card-orange { border-left-color: var(--c-accent); }
.lab-card-green  { border-left-color: var(--c-success); }
.lab-card-red    { border-left-color: var(--c-error); }
.lab-card-purple { border-left-color: var(--c-primary-2); }

/* ── Badges ────────────────────────────────────────────────────────────── */
.badge {
    display: inline-block;
    padding: 3px 11px;
    border-radius: 999px;
    font-size: 11.5px;
    font-weight: 600;
    margin: 2px 4px 2px 0;
    letter-spacing: 0.1px;
}
.badge-blue   { background: #EAF1F7; color: var(--c-primary); }
.badge-orange { background: #FBF1E2; color: #8A5A12; }
.badge-green  { background: #E7F3EC; color: var(--c-success); }
.badge-red    { background: #F8E9E7; color: var(--c-error); }

/* ── Prompt box ──────────────────────────────────────────────────────────── */
.prompt-box {
    background: var(--c-primary);
    color: #BFD9EC;
    border-radius: var(--radius);
    padding: var(--sp-3) var(--sp-4);
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 12.5px;
    line-height: 1.7;
    margin: var(--sp-2) 0;
    border-left: 3px solid var(--c-accent);
}
.prompt-weak {
    background: #34201D;
    border-left-color: var(--c-error);
    color: #E8B4AD;
}

/* ── Step box ────────────────────────────────────────────────────────────── */
.step-box {
    background: var(--c-surface);
    border-radius: var(--radius);
    padding: var(--sp-3) var(--sp-4);
    margin: var(--sp-2) 0;
    border: 1px solid var(--c-line);
    display: flex;
    gap: var(--sp-3);
    align-items: flex-start;
}
.step-num {
    background: var(--c-primary);
    color: white;
    width: 28px; height: 28px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; font-weight: 700;
    flex-shrink: 0;
}

/* ── Data card ───────────────────────────────────────────────────────────── */
.data-card {
    border-radius: var(--radius);
    padding: var(--sp-4) var(--sp-5);
    margin: var(--sp-2) 0;
    border: 1px solid;
    background: var(--c-surface);
}
.data-card-blue   { border-color: var(--c-line); border-left: 3px solid var(--c-primary); }
.data-card-green  { border-color: var(--c-line); border-left: 3px solid var(--c-success); }
.data-card-orange { border-color: var(--c-line); border-left: 3px solid var(--c-accent); }

/* ── Score ───────────────────────────────────────────────────────────────── */
.score-big {
    font-size: 44px;
    font-weight: 800;
    text-align: center;
    line-height: 1;
    color: var(--c-primary);
}

/* ── Section banner ──────────────────────────────────────────────────────── */
.section-banner {
    background: var(--c-primary);
    color: white;
    padding: 10px 18px;
    border-radius: var(--radius);
    font-size: 14.5px;
    font-weight: 700;
    letter-spacing: 0.1px;
    margin: var(--sp-5) 0 var(--sp-3) 0;
}

.metric-row {
    display: flex; gap: var(--sp-3); flex-wrap: wrap; margin: var(--sp-3) 0;
}
.metric-box {
    background: var(--c-surface);
    border-radius: var(--radius);
    padding: var(--sp-3) var(--sp-5);
    text-align: center;
    border: 1px solid var(--c-line);
    box-shadow: var(--shadow-sm);
    flex: 1; min-width: 120px;
}
.metric-val { font-size: 26px; font-weight: 800; color: var(--c-primary); }
.metric-lbl { font-size: 10.5px; color: var(--c-muted); margin-top: 3px; text-transform: uppercase; letter-spacing: 0.4px; font-weight: 600; }

/* ── Misc polish ─────────────────────────────────────────────────────────── */
hr { margin: var(--sp-4) 0 !important; border-color: var(--c-line) !important; }
.stButton > button[kind="primary"] {
    background: var(--c-primary) !important; border: none !important;
    border-radius: var(--radius) !important; font-weight: 700 !important;
}
div[data-testid="stExpander"] { border-radius: var(--radius) !important; border: 1px solid var(--c-line) !important; }
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE INITIALIZATION ─────────────────────────────────────────────
def init_state():
    defaults = {
        "l1_ex1_before": "", "l1_ex1_after": "", "l1_ex1_done": False,
        "l1_ex2_prompt": "", "l1_ex2_output": "", "l1_ex2_changes": "",
        "l1_ex2_scenario": "A",
        "l1_chain_notes": ["", "", "", ""],
        "l1_score": 0,
        "l2_step": 0,
        "l2_notes": {"sensors": "", "maintenance": "", "inventory": ""},
        "l2_decision": "",
        "l2_vulnerability": "",
        "l2_recommendation_shown": False,
        "l3_obs": {c: {"pred": "", "conf": "", "correct": ""} for c in [
            "Helmet on, facing forward",
            "Helmet on, sideways",
            "No helmet, forward",
            "No helmet, dim lighting",
            "Helmet tilted / partial",
            "Different person with helmet"
        ]},
        "l3_accuracy_note": "",
        "l3_improvement": "",
        "l3_score": 0,
        "completed_labs": set(),
        "total_score": 0,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ── SIDEBAR NAVIGATION ───────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sb-brand-title">AI LABS</div>
    <div class="sb-brand-sub">Session Journey of AI</div>
    <div class="sb-brand-org">L&amp;D Division · Training Programme 2025–26</div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    lab = st.radio(
        "Navigate",
        ["🏠 Home", "🛠️ Lab 1 — Prompt Lab", "🤖 Lab 2 — Agentic Lab", "📊 Lab 3 — ML Lab"],
        key="nav"
    )
    st.markdown("---")
    done = len(st.session_state.completed_labs)
    st.markdown(f'<div class="sb-progress-label">Progress · {done}/3 Labs</div>', unsafe_allow_html=True)
    st.progress(done / 3)
    for lab_name, lab_label in [("Lab 1", "Prompt Lab"), ("Lab 2", "Agentic Lab"), ("Lab 3", "ML Lab")]:
        is_done = lab_name in str(st.session_state.completed_labs)
        icon = "✓" if is_done else "○"
        cls = "done" if is_done else ""
        st.markdown(f'<div class="sb-lab-status {cls}">{icon} &nbsp;{lab_name} — {lab_label}</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(
        '<div class="sb-footer">Prepared by Keshar Mishra<br>IT Department Intern<br>Learning &amp; Development Division</div>',
        unsafe_allow_html=True
    )

# ── HUB OVERVIEW / HOME MODULE ───────────────────────────────────────────────
if lab == "🏠 Home":
    st.markdown("## Session Journey of AI")
    st.markdown(
        '<p style="font-size:14px;color:var(--c-muted);margin-top:-4px;max-width:680px">'
        "Welcome, Trainee. This platform gives you three interactive labs that let you "
        "experience AI from the inside — no coding, no installation, just your browser.</p>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="lab-card">
        <h3>Lab 1 · Prompt Lab</h3>
        <p style="font-size:13px;color:var(--c-muted);margin:8px 0;min-height:54px">See how prompt wording changes AI output quality for plant operations tasks.</p>
        <span class="badge badge-blue">45 min</span>
        <span class="badge badge-orange">Groups of 3–4</span>
        <span class="badge badge-green">ChatGPT / Claude</span>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="lab-card lab-card-orange">
        <h3>Lab 2 · Agentic Solution Lab</h3>
        <p style="font-size:13px;color:var(--c-muted);margin:8px 0;min-height:54px">Simulate how an agentic AI platform plans, queries data, and gives recommendations autonomously.</p>
        <span class="badge badge-blue">45 min</span>
        <span class="badge badge-orange">Groups of 4–5</span>
        <span class="badge badge-green">No device needed</span>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="lab-card lab-card-green">
        <h3>Lab 3 · ML Lab</h3>
        <p style="font-size:13px;color:var(--c-muted);margin:8px 0;min-height:54px">Train a real neural network in your browser. PPE detection — just like an industrial computer-vision safety system.</p>
        <span class="badge badge-blue">45 min</span>
        <span class="badge badge-orange">Groups of 2–3</span>
        <span class="badge badge-green">Teachable Machine</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Why These Labs Matter")
    m1, m2, m3, m4, m5 = st.columns(5)
    metrics = [("3","Hands-On Labs"),("45 min","Per Lab"),("0","Lines of Code"),
               ("100%","Browser-Based"),("Real","AI Models Used")]
    for col, (val, lbl) in zip([m1,m2,m3,m4,m5], metrics):
        with col:
            st.markdown(f"""
            <div class="metric-box">
            <div class="metric-val">{val}</div>
            <div class="metric-lbl">{lbl}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.info("👈 Use the sidebar to navigate to any lab. Start with Lab 1.")

# ── LAB 1 MODULE (PROMPT ENGINEERING) ────────────────────────────────────────
elif lab == "🛠️ Lab 1 — Prompt Lab":
    st.markdown("## Lab 1 — Prompt Engineering Lab")
    st.markdown(
        '<span class="badge badge-blue">45 min</span> '
        '<span class="badge badge-orange">Groups of 3–4</span> '
        '<span class="badge badge-green">ChatGPT or Claude</span>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="lab-card">
    <b>Learning Objective:</b> Experience firsthand how the structure and specificity of a prompt
    directly changes the quality of AI output — transitioning prompt entry from casual typing
    into a reliable engineering skill for the shop floor.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-banner">📐 The R-T-C-F-C Framework</div>', unsafe_allow_html=True)
    st.markdown("Every strong industrial prompt has 5 elements:")

    fw_data = {
        "Role": ("Who is the AI?", "\"You are a safety officer at a steel plant.\"", "#0F3D61"),
        "Task": ("What exactly do you want?", "\"Write a 7-point blast furnace checklist.\"", "#15517F"),
        "Context": ("Plant conditions, data, history", "\"Temp hit 85°C in Hot Strip Mill 2.\"", "#C5821A"),
        "Format": ("How should output look?", "\"Numbered list with checkboxes.\"", "#1E8449"),
        "Constraint": ("Rules and limits", "\"Only include steps from IS 3901 standard.\"", "#B03A2E"),
    }
    cols = st.columns(5)
    for col, (elem, (purpose, example, color)) in zip(cols, fw_data.items()):
        with col:
            st.markdown(f"""
            <div style="background:white;border-radius:8px;padding:12px;border-top:4px solid {color};
            box-shadow:0 2px 6px rgba(0,0,0,0.07);height:160px;">
            <div style="font-size:15px;font-weight:700;color:{color}">{elem}</div>
            <div style="font-size:12px;color:#444;margin:6px 0">{purpose}</div>
            <div style="font-size:11px;color:#777;font-style:italic">{example}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="section-banner">Exercise 1 — Weak vs Strong Prompt (15 min)</div>', unsafe_allow_html=True)
    st.markdown("Copy each prompt into ChatGPT or Claude. Paste the AI's response in the boxes below.")

    tab_a, tab_b = st.tabs(["Pair A: Safety Checklist", "Pair B: Maintenance Report"])

    with tab_a:
        col_weak, col_strong = st.columns(2)
        with col_weak:
            st.markdown("**❌ WEAK Prompt**")
            st.markdown('<div class="prompt-box prompt-weak">Give me a safety checklist.</div>', unsafe_allow_html=True)
            st.markdown('<span class="badge badge-red">Vague — no plant, no role, no format</span>', unsafe_allow_html=True)
        with col_strong:
            st.markdown("**✅ STRONG Prompt**")
            st.markdown("""
            <div class="prompt-box">
            You are a safety officer at a steel plant's blast furnace unit [Role].
            Create a 7-point pre-shift safety checklist for furnace operators [Task].
            This is for a 6-hour shift on Hot Strip Mill 2 [Context].
            Format as a numbered list with a ☐ checkbox before each item [Format].
            Keep language simple — operators are not engineers [Constraint].
            </div>
            """, unsafe_allow_html=True)

        st.markdown("**📝 Paste the AI's output for each and compare:**")
        c1, c2 = st.columns(2)
        with c1:
            before = st.text_area("Weak prompt output (paste here)", key="l1_a_weak", height=180,
                                   placeholder="Paste what ChatGPT/Claude said for the weak prompt...")
        with c2:
            after = st.text_area("Strong prompt output (paste here)", key="l1_a_strong", height=180,
                                  placeholder="Paste what ChatGPT/Claude said for the strong prompt...")
        if before and after:
            st.success("✅ Great! Notice the difference? The strong prompt gives you a usable, plant-specific result.")

    with tab_b:
        col_weak2, col_strong2 = st.columns(2)
        with col_weak2:
            st.markdown("**❌ WEAK Prompt**")
            st.markdown('<div class="prompt-box prompt-weak">Write a maintenance report.</div>', unsafe_allow_html=True)
        with col_strong2:
            st.markdown("**✅ STRONG Prompt**")
            st.markdown("""
            <div class="prompt-box">
            Write a maintenance incident report [Task].
            Situation: A main bearing in Hot Strip Mill showed abnormal vibration
            (sensor reading: 8.2 mm/s, threshold: 4.5 mm/s) for 3 consecutive days [Context].
            Maintenance team replaced bearing on 28 May 2025. Downtime: 4 hours [Context].
            Format: Date / Equipment / Observation / Action Taken / Downtime / Next Inspection Date [Format].
            </div>
            """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.text_area("Weak output", key="l1_b_weak", height=180,
                         placeholder="Paste weak prompt output here...")
        with c2:
            st.text_area("Strong output", key="l1_b_strong", height=180,
                          placeholder="Paste strong prompt output here...")

    st.markdown("---")
    st.markdown('<div class="section-banner">Exercise 2 — Write Your Own Prompt (15 min)</div>', unsafe_allow_html=True)
    st.markdown("Your group picks one scenario and writes a prompt using all 5 R-T-C-F-C elements.")

    scenario_options = {
        "A": "Explain why predictive maintenance is better than reactive maintenance — for a furnace operator who has never heard of AI.",
        "B": "Write a short SOP for safe PPE usage in the casting section.",
        "C": "Summarise a conveyor belt motor trip at 2 AM (2 hours downtime) into 3 bullet points for a plant manager.",
        "D": "Create 5 quiz questions about blast furnace hazards for a trainee exam.",
    }
    scenario = st.selectbox("Pick your scenario:", [f"Scenario {k}: {v}" for k, v in scenario_options.items()])

    st.markdown("**Now build your prompt using the 5 elements:**")
    cols = st.columns(5)
    labels = ["Role", "Task", "Context", "Format", "Constraint"]
    placeholders = [
        "You are a...",
        "Write / Create / Explain...",
        "Plant conditions, data...",
        "Bullet list / table / 3 sentences...",
        "Only use... / Keep under... / Must include...",
    ]
    prompt_parts = {}
    for col, label, ph in zip(cols, labels, placeholders):
        with col:
            prompt_parts[label] = st.text_input(label, placeholder=ph, key=f"l1_part_{label}")

    if any(prompt_parts.values()):
        combined = " ".join([f"[{k}: {v}]" for k, v in prompt_parts.items() if v])
        st.markdown("**Your assembled prompt:**")
        st.markdown(f'<div class="prompt-box">{combined}</div>', unsafe_allow_html=True)
        if st.button("📋 Copy to clipboard reminder"):
            st.info("Copy the prompt above and paste it into ChatGPT or Claude, then paste the output below.")

    st.text_area("Paste AI output here", key="l1_ex2_output", height=150,
                 placeholder="Paste what the AI gave you...")
    st.text_area("What would you change to improve it?", key="l1_ex2_changes", height=80,
                 placeholder="e.g. Add more context about temperature thresholds...")

    st.markdown("---")
    st.markdown('<div class="section-banner">Exercise 3 — Chain Prompting (15 min)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="lab-card">
    Chain prompting = building on previous AI responses. Real industrial tasks need conversations,
    not single questions. Run these <b>in order in the same chat window</b>.
    </div>
    """, unsafe_allow_html=True)

    chain_prompts = [
        ("Starter — Diagnose", 'You are a maintenance engineer at a steel plant. I have a blast furnace bearing showing 75% failure probability within 5 days. List 3 possible causes and what data I should check for each.'),
        ("Step 2 — Action Plan", 'Now assume the first cause is correct. Write a step-by-step action plan for the shift engineer to follow in the next 48 hours.'),
        ("Step 3 — Write Email", 'Convert that action plan into a formal email I can send to my plant manager.'),
        ("Step 4 — Shorten", 'Now make the email shorter — maximum 5 sentences. Subject line included.'),
    ]

    for i, (title, prompt_text) in enumerate(chain_prompts):
        with st.expander(f"{'▶' if i==0 else '  '} Prompt {i+1}: {title}"):
            st.markdown(f'<div class="prompt-box">{prompt_text}</div>', unsafe_allow_html=True)
            st.text_area(f"Paste AI output for Step {i+1}", key=f"l1_chain_{i}", height=120,
                        placeholder=f"Paste ChatGPT/Claude response for Step {i+1} here...")

    st.markdown("---")
    st.markdown('<div class="section-banner">💬 Debrief Questions</div>', unsafe_allow_html=True)
    debriefs = [
        "What's the plant risk if an operator gives vague context during a safety-critical task?",
        "How is writing a structured prompt similar to writing a good job card or work order?",
        "In chain prompting, what happened to the email between Step 3 and Step 4?",
        "Which of the 5 R-T-C-F-C elements had the biggest impact on output quality?",
    ]
    for q in debriefs:
        st.text_area(q, key=f"l1_debrief_{q[:20]}", height=70, placeholder="Type your answer...")

    if st.button("✅ Mark Lab 1 as Complete", type="primary"):
        st.session_state.completed_labs.add("Lab 1")
        st.balloons()
        st.success("🎉 Lab 1 complete! Navigate to Lab 2 from the sidebar.")

# ── LAB 2 MODULE (AGENTIC SOLUTIONS) ─────────────────────────────────────────
elif lab == "🤖 Lab 2 — Agentic Lab":
    st.markdown("## Lab 2 — Agentic Solution Lab")
    st.markdown(
        '<span class="badge badge-blue">45 min</span> '
        '<span class="badge badge-orange">Groups of 4–5</span> '
        '<span class="badge badge-green">Role-play simulation</span>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="lab-card lab-card-orange">
    <b>Learning Objective:</b> Simulate how an agentic AI platform receives a goal,
    plans steps, queries databases, and generates a recommendation autonomously using the
    <b>ReAct (Reasoning + Acting)</b> loop.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-banner">👥 Assign Roles (one per group member)</div>', unsafe_allow_html=True)
    roles = [
        ("USER", "Plant Shift Manager", "Read the scenario aloud. You trigger the agent.", "#0F3D61"),
        ("AGENT BRAIN", "Core AI Orchestrator", "Follow the 7-step script. Speak each step aloud.", "#15517F"),
        ("DATA CALLER 1", "Sensor Database", "Read your sensor card ONLY when Agent Brain calls you.", "#C5821A"),
        ("DATA CALLER 2", "Maintenance Log", "Read your maintenance card ONLY when called.", "#1E8449"),
        ("DATA CALLER 3", "Spare Parts Inventory", "Read your inventory card ONLY when called.", "#B03A2E"),
        ("HUMAN APPROVER", "Plant Manager", "Receive the recommendation. Approve or override.", "#3A4A5A"),
    ]
    cols = st.columns(3)
    for i, (role, persona, duty, color) in enumerate(roles):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="background:white;border-radius:8px;padding:12px 14px;margin:6px 0;
            border-left:4px solid {color};box-shadow:0 2px 6px rgba(0,0,0,0.07);">
            <div style="font-size:13px;font-weight:700;color:{color}">{role}</div>
            <div style="font-size:12px;font-weight:600;color:#0F3D61">{persona}</div>
            <div style="font-size:12px;color:#666;margin-top:4px">{duty}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="section-banner">🚨 The Scenario (USER reads this aloud)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="data-card data-card-blue">
    <b style="font-size:15px;color:#0F3D61"> Blast Furnace 02</b><br><br>
    <span style="font-size:14px;line-height:1.8">
    The Predictive Maintenance dashboard registers a <b>YELLOW ALERT</b> on Blast Furnace-02.<br>
    Main Bearing <b>MB-7</b> shows a <b>75% probability of failure within 5 days</b>.<br>
    I need the AI agent to investigate all available data and give me an optimal recommendation.
    </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="section-banner">🃏 Data Cards (Data Callers — read ONLY when called)</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.expander("📡 DATA CARD 1 — Sensor Database"):
            st.markdown("""
            <div class="data-card data-card-blue">
            <b>MB-7 Vibration:</b> 8.6 mm/s <span style="color:red">(Threshold: 4.5 mm/s ⚠️)</span><br>
            <b>MB-7 Temperature:</b> 94°C <span style="color:red">(Normal: &lt;75°C ⚠️)</span><br>
            <b>Trend:</b> Rising for 6 consecutive days<br>
            <b>Last normal reading:</b> 5 days ago
            </div>
            """, unsafe_allow_html=True)
    with c2:
        with st.expander("🔧 DATA CARD 2 — Maintenance Log"):
            st.markdown("""
            <div class="data-card data-card-green">
            <b>Last replaced:</b> 14 months ago <span style="color:red">(Cycle: 12 months ⚠️)</span><br>
            <b>Last lubrication:</b> 3 weeks ago <span style="color:red">(Due: every 2 weeks ⚠️)</span><br>
            <b>Previous failure:</b> March 2023 → 18 hrs downtime<br>
            <b>Emergency repair cost:</b> ₹8.4 lakh
            </div>
            """, unsafe_allow_html=True)
    with c3:
        with st.expander("📦 DATA CARD 3 — Spare Parts Inventory"):
            st.markdown("""
            <div class="data-card data-card-orange">
            <b>SKF-22230 bearings in stock:</b> 2 units ✅<br>
            <b>Replacement time:</b> 6 hours<br>
            <b>Next planned shutdown:</b> 8 days <span style="color:red">(Too late ⚠️)</span><br>
            <b>Active order at risk:</b> ₹4.2 crore (due in 3 days)
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="section-banner">🧠 Agent Brain — 7-Step ReAct Script (speak each step aloud)</div>', unsafe_allow_html=True)

    agent_steps = [
        ("1", "Acknowledge Goal",     "Goal received. MB-7 bearing has a failure alert. I will investigate and provide an optimised recommendation.", "#0F3D61"),
        ("2", "State Plan",           "I need: (a) current sensor readings, (b) maintenance history, (c) spare parts availability. Then I will calculate risk.", "#15517F"),
        ("3", "Call Sensor DB",       "DATA CALLER 1 — give me MB-7 current readings and trend.", "#C5821A"),
        ("4", "Call Maintenance Log", "DATA CALLER 2 — give me MB-7 replacement and lubrication history.", "#1E8449"),
        ("5", "Call Inventory",       "DATA CALLER 3 — do we have the compatible bearing in stock? How long to replace?", "#B03A2E"),
        ("6", "Synthesise",           "Bearing is overdue for replacement. Running at 94°C and 8.6 mm/s. Both readings rising. Stock available. Emergency failure cost last time: ₹8.4 lakh. Active order: ₹4.2 crore.", "#C5821A"),
        ("7", "Recommendation →",     "RECOMMENDATION TO HUMAN APPROVER: Replace MB-7 within 24 hours after the current order completes in 72 hours. Increase lubrication monitoring every 12 hours as interim. Estimated savings vs emergency failure: ₹6+ lakh.", "#1E8449"),
    ]

    for num, title, script, color in agent_steps:
        st.markdown(f"""
        <div style="display:flex;gap:12px;align-items:flex-start;margin:8px 0;
        background:white;border-radius:8px;padding:12px 14px;border:1px solid #E2E8F0;">
        <div style="background:{color};color:white;width:32px;height:32px;border-radius:50%;
        display:flex;align-items:center;justify-content:center;font-weight:700;
        font-size:14px;flex-shrink:0;">{num}</div>
        <div>
        <div style="font-weight:600;font-size:13px;color:#0F3D61">{title}</div>
        <div style="font-style:italic;font-size:13px;color:#444;margin-top:3px">"{script}"</div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="section-banner">📝 Agent Brain — Record Your Data Findings</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.session_state.l2_notes["sensors"] = st.text_area(
            "From DATA CARD 1 (Sensors)", height=100,
            value=st.session_state.l2_notes["sensors"],
            placeholder="Note the key sensor readings...")
    with c2:
        st.session_state.l2_notes["maintenance"] = st.text_area(
            "From DATA CARD 2 (Maintenance)", height=100,
            value=st.session_state.l2_notes["maintenance"],
            placeholder="Note the maintenance history...")
    with c3:
        st.session_state.l2_notes["inventory"] = st.text_area(
            "From DATA CARD 3 (Inventory)", height=100,
            value=st.session_state.l2_notes["inventory"],
            placeholder="Note parts availability...")

    st.markdown("---")
    st.markdown('<div class="section-banner">👔 Human Approver — Make Your Decision</div>', unsafe_allow_html=True)
    decision = st.radio(
        "Do you approve the Agent Brain's recommendation?",
        ["✅ Approve — Replace after 72 hours + increase lubrication monitoring",
         "🔄 Modify — Stop furnace immediately, don't risk the active order",
         "❌ Override — Continue operations, re-evaluate in 2 days"],
        key="l2_decision_radio"
    )
    st.text_area("Justify your decision:", key="l2_justification", height=80,
                 placeholder="Why did you approve / modify / override?")

    st.markdown("---")
    st.markdown('<div class="section-banner">🔍 System Vulnerability Analysis</div>', unsafe_allow_html=True)
    st.text_area(
        "What breaks in the Agent Brain's reasoning if DATA CARD 3 said: '0 units in stock'?",
        key="l2_vuln", height=80,
        placeholder="How would the recommendation change? What would the agent do next?")
    st.text_area(
        "An agentic AI platform completes this entire 7-step sequence across live enterprise systems in under 30 seconds. How does that speed change daily plant operations?",
        key="l2_speed", height=80,
        placeholder="Think about night shifts, weekends, emergency situations...")

    st.markdown("---")
    st.markdown('<div class="section-banner">💬 Debrief Questions</div>', unsafe_allow_html=True)
    for q in [
        "What data point had the biggest influence on the Agent Brain's recommendation?",
        "Can the Agent Brain ever be wrong? What is the human's role?",
        "Name one real-world AI agent (from the session) that follows this exact same loop.",
    ]:
        st.text_area(q, key=f"l2_deb_{q[:15]}", height=70, placeholder="Your answer...")

    if st.button("✅ Mark Lab 2 as Complete", type="primary"):
        st.session_state.completed_labs.add("Lab 2")
        st.balloons()
        st.success("🎉 Lab 2 complete! Navigate to Lab 3 from the sidebar.")

# ── LAB 3 MODULE (MACHINE LEARNING VISION) ───────────────────────────────────
elif lab == "📊 Lab 3 — ML Lab":
    st.markdown("## Lab 3 — ML Lab: Train a Real AI Model")
    st.markdown(
        '<span class="badge badge-blue">45 min</span> '
        '<span class="badge badge-orange">Groups of 2–3 per device</span> '
        '<span class="badge badge-green">teachablemachine.withgoogle.com</span>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="lab-card lab-card-green">
    <b>Learning Objective:</b> Train a real neural network image classifier in your browser.
    Experience what 'training data', 'model accuracy', 'confidence scores', and 'inference'
    actually mean — the same mechanics behind industrial computer-vision safety systems.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-banner">🚀 Step 1 — Open Teachable Machine</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background:white;border-radius:8px;padding:16px 20px;border:1px solid #E2E8F0;margin:8px 0;">
    <ol style="font-size:14px;line-height:2.2;color:#1A1A2E;">
    <li>Go to <a href="https://teachablemachine.withgoogle.com" target="_blank"><b>teachablemachine.withgoogle.com</b></a></li>
    <li>Click <b>Get Started</b></li>
    <li>Click <b>Image Project</b></li>
    <li>Select <b>Standard Image Model</b></li>
    <li>Rename <b>Class 1</b> → <code>PPE ON</code></li>
    <li>Rename <b>Class 2</b> → <code>PPE OFF</code></li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

    confirm_open = st.checkbox("✅ I have opened Teachable Machine and set up my two classes")

    if confirm_open:
        st.markdown('<div class="section-banner">📸 Step 2 — Collect Training Images</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            <div class="data-card data-card-green">
            <b style="color:#1E8449">CLASS 1 — PPE ON</b><br><br>
            • Put on a safety helmet (or any hat / headgear)<br>
            • Click <b>Webcam</b> → <b>Hold to Record</b><br>
            • Vary head position slightly while recording<br>
            • Target: <b>60–80 frames</b><br><br>
            <span style="font-size:12px;color:#666">Tip: Move left, right, tilt slightly. Variety = accuracy.</span>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class="data-card data-card-blue">
            <b style="color:#0F3D61">CLASS 2 — PPE OFF</b><br><br>
            • Remove the helmet completely<br>
            • Same background and lighting as Class 1<br>
            • Click <b>Webcam</b> → <b>Hold to Record</b><br>
            • Target: <b>60–80 frames</b><br><br>
            <span style="font-size:12px;color:#666">Important: Same number of images as Class 1.</span>
            </div>
            """, unsafe_allow_html=True)

        images_done = st.checkbox("✅ I have collected 60–80 images for BOTH classes")

        if images_done:
            st.markdown('<div class="section-banner">⚙️ Step 3 — Train the Model</div>', unsafe_allow_html=True)
            st.markdown("""
            <div style="background:#0F3D61;color:white;border-radius:8px;padding:14px 18px;margin:8px 0;">
            Click the blue <b>Train Model</b> button in Teachable Machine.<br>
            Wait 30–60 seconds. <b>Do NOT switch browser tabs during training.</b><br>
            <span style="color:#A8D4F5;font-size:13px;">What's happening: A real gradient descent algorithm is adjusting neural network weights based on your pixel data.</span>
            </div>
            """, unsafe_allow_html=True)

            training_done = st.checkbox("✅ Model training is complete — preview window is active")

            if training_done:
                st.markdown('<div class="section-banner">🧪 Step 4 — Test & Record Results</div>', unsafe_allow_html=True)
                st.markdown("Test each condition and record what the model predicts. Be honest — include failures!")

                test_conditions = [
                    "Helmet on, facing forward",
                    "Helmet on, sideways",
                    "No helmet, forward",
                    "No helmet, dim lighting",
                    "Helmet tilted / partial",
                    "Different person with helmet",
                ]

                header_cols = st.columns([3, 2, 2, 2])
                header_cols[0].markdown("**Test Condition**")
                header_cols[1].markdown("**Predicted Class**")
                header_cols[2].markdown("**Confidence %**")
                header_cols[3].markdown("**Correct? (Y/N)**")
                st.markdown("<hr style='margin:4px 0'>", unsafe_allow_html=True)

                for condition in test_conditions:
                    cols = st.columns([3, 2, 2, 2])
                    with cols[0]:
                        st.markdown(f"<div style='padding:6px 0;font-size:13px'>{condition}</div>", unsafe_allow_html=True)
                    with cols[1]:
                        pred = st.selectbox("", ["", "PPE ON", "PPE OFF"], key=f"pred_{condition}", label_visibility="collapsed")
                    with cols[2]:
                        conf = st.number_input("", min_value=0, max_value=100, key=f"conf_{condition}", label_visibility="collapsed")
                    with cols[3]:
                        correct = st.selectbox("", ["", "Y", "N"], key=f"correct_{condition}", label_visibility="collapsed")
                    st.session_state.l3_obs[condition] = {"pred": pred, "conf": conf, "correct": correct}

                filled = [v for v in st.session_state.l3_obs.values() if v["correct"] in ["Y", "N"]]
                if filled:
                    correct_count = sum(1 for v in filled if v["correct"] == "Y")
                    accuracy = round(correct_count / len(filled) * 100)
                    conf_avg = sum(v["conf"] for v in filled if v["conf"]) / max(len(filled), 1)
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        color = "#1E8449" if accuracy >= 80 else "#C5821A" if accuracy >= 60 else "#B03A2E"
                        st.markdown(f"""
                        <div class="metric-box">
                        <div class="metric-val" style="color:{color}">{accuracy}%</div>
                        <div class="metric-lbl">Your model accuracy</div>
                        </div>""", unsafe_allow_html=True)
                    with c2:
                        st.markdown(f"""
                        <div class="metric-box">
                        <div class="metric-val" style="color:#0F3D61">{correct_count}/{len(filled)}</div>
                        <div class="metric-lbl">Correct predictions</div>
                        </div>""", unsafe_allow_html=True)
                    with c3:
                        st.markdown(f"""
                        <div class="metric-box">
                        <div class="metric-val" style="color:#15517F">{round(conf_avg)}%</div>
                        <div class="metric-lbl">Avg confidence</div>
                        </div>""", unsafe_allow_html=True)

                    if accuracy < 70:
                        st.warning("⚠️ Accuracy below 70%. Try: more training images, better lighting consistency, or more varied angles.")
                    elif accuracy < 90:
                        st.info("👍 Good result. To reach industrial deployment level (>97%), you'd need millions of diverse frames.")
                    else:
                        st.success("🎉 Excellent accuracy for a lab model!")

                st.markdown("---")
                st.text_area("What did you notice about accuracy when lighting or angle changed?",
                             key="l3_accuracy_note", height=80, placeholder="Write your observation...")
                st.text_area("What would you do to improve this model?",
                             key="l3_improvement", height=80,
                             placeholder="e.g. More images, add 'partial PPE' class, vary backgrounds...")

                st.markdown("---")
                st.markdown('<div class="section-banner">🏆 Challenge Extensions (if time allows)</div>', unsafe_allow_html=True)
                challenges = [
                    ("3-Class Test", "Add a 3rd class: PARTIAL PPE (helmet on, no vest). Retrain. Does accuracy drop?", "#15517F"),
                    ("Spoofing Attack", "Hold a phone showing a photo of a helmet. Does the model get fooled?", "#B03A2E"),
                    ("Data Quantity Test", "Retrain with only 20 images. Compare accuracy vs 80 images.", "#C5821A"),
                    ("Lighting Test", "Train in bright light, test in dim light. Record the confidence score drop.", "#0F3D61"),
                ]
                cols = st.columns(2)
                for i, (title, desc, color) in enumerate(challenges):
                    with cols[i % 2]:
                        done_ch = st.checkbox(f"✅ {title}", key=f"l3_ch_{i}")
                        st.markdown(f"""
                        <div style="background:white;border-radius:8px;padding:10px 14px;
                        border-left:3px solid {color};margin-bottom:8px;font-size:12px;color:#444">
                        {desc}
                        </div>""", unsafe_allow_html=True)

                st.markdown("---")
                st.markdown('<div class="section-banner">🔗 Connecting Your Lab to Industrial Scale</div>', unsafe_allow_html=True)
                scale_data = [
                    ("You captured 80 webcam images", "Industrial plants stream millions of CCTV frames daily"),
                    ("You manually labelled 2 classes", "Uses annotation pipelines + semi-supervised labelling"),
                    ("Model trained in 60 seconds", "Runs on hundreds of Google Cloud TPUs"),
                    ("Tested in one room, one light setting", "Operates across furnaces, dust, glare, heat"),
                    ("Your accuracy: ~85%", "Industrial deployment targets >97% before go-live"),
                ]
                for lab_side, scale_side in scale_data:
                    c1, c2 = st.columns(2)
                    with c1:
                        st.markdown(f'<div style="background:#EBF4FB;border-radius:6px;padding:8px 12px;font-size:12px;margin:3px 0">🧑‍💻 {lab_side}</div>', unsafe_allow_html=True)
                    with c2:
                        st.markdown(f'<div style="background:#E9F7EF;border-radius:6px;padding:8px 12px;font-size:12px;margin:3px 0">🏭 {scale_side}</div>', unsafe_allow_html=True)

                st.markdown("---")
                st.markdown('<div class="section-banner">💬 Debrief Questions</div>', unsafe_allow_html=True)
                for q in [
                    "Why did confidence drop when lighting changed? What does this mean for blast furnace deployment?",
                    "If this model had 15% error at a real factory gate, what are the safety consequences?",
                    "What is the human's role after a model is deployed?",
                ]:
                    st.text_area(q, key=f"l2_deb_{q[:15]}", height=70, placeholder="Your answer...")

    if st.button("✅ Mark Lab 3 as Complete", type="primary"):
        st.session_state.completed_labs.add("Lab 3")
        st.balloons()
        st.success("🎉 Lab 3 complete! All three labs done.")

    if len(st.session_state.completed_labs) == 3:
        st.markdown("---")
        st.markdown("""
        <div style="background:#0F3D61;color:white;border-radius:12px;padding:24px;text-align:center;">
        <div style="font-size:32px">🏆</div>
        <div style="font-size:22px;font-weight:700;margin:8px 0">All 3 Labs Complete!</div>
        <div style="color:#A8D4F5;font-size:14px">
        You have experienced Prompt Engineering, Agentic AI simulation, and real ML model training.<br>
        These are the same technologies powering modern industrial AI agent platforms today.
        </div>
        </div>
        """, unsafe_allow_html=True)
