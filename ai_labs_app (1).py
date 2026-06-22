import streamlit as st
import time
import json
import random

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Labs — L&D Division",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="collapsed" # Automatically collapses the sidebar to keep focus on the single page UI
)

# ── GLOBAL CSS DESIGN SYSTEM (MATURE ENTERPRISE STYLING) ─────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght=400;500;600;700;800&display=swap');

/* Design Tokens */
:root {
    --c-primary:    #0F3D61;   /* deep corporate navy — primary brand */
    --c-primary-2:  #15517F;   /* lighter navy for gradients/hover */
    --c-accent:     #C5821A;   /* single muted amber accent (status-neutral emphasis) */
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

html, body, [class*="css"] { 
    font-family: 'Inter', sans-serif; 
    color: var(--c-ink); 
}
.main { background: var(--c-bg); }

/* Master Header Title Banner */
.master-header {
    background: linear-gradient(135deg, var(--c-primary) 0%, var(--c-primary-2) 100%);
    padding: 24px 32px;
    border-radius: var(--radius);
    color: #FFFFFF !important;
    margin-bottom: 24px;
    box-shadow: var(--shadow-md);
}
.master-header h1 { color: #FFFFFF !important; font-size: 26px; font-weight: 700; margin: 0; letter-spacing: -0.02em; }
.master-header p { color: #D4E6F1 !important; font-size: 13px; margin: 6px 0 0 0; opacity: 0.85; }

/* Typographic Scale Styles */
h2 { font-size: 24px !important; font-weight: 800 !important; color: var(--c-primary) !important; letter-spacing: -0.3px; margin-bottom: var(--sp-1) !important; }
h3 { font-size: 16px !important; font-weight: 700 !important; color: var(--c-primary) !important; }
h4 { font-size: 14px !important; font-weight: 600 !important; }

/* Section Typographic Line Dividers */
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

/* Layout Content Cards */
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

/* Badges Tokens */
.badge { display: inline-block; padding: 3px 11px; border-radius: 999px; font-size: 11.5px; font-weight: 600; margin: 2px 4px 2px 0; letter-spacing: 0.1px; }
.badge-blue   { background: #EAF1F7; color: var(--c-primary); }
.badge-orange { background: #FBF1E2; color: #8A5A12; }
.badge-green  { background: #E7F3EC; color: var(--c-success); }
.badge-red    { background: #F8E9E7; color: var(--c-error); }

/* Code & Output Terminals */
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
.prompt-weak { background: #34201D; border-left-color: var(--c-error); color: #E8B4AD; }

.data-card { border-radius: var(--radius); padding: var(--sp-4) var(--sp-5); margin: var(--sp-2) 0; border: 1px solid; background: var(--c-surface); }
.data-card-blue   { border-color: var(--c-line); border-left: 3px solid var(--c-primary); }
.data-card-green  { border-color: var(--c-line); border-left: 3px solid var(--c-success); }
.data-card-orange { border-color: var(--c-line); border-left: 3px solid var(--c-accent); }

.metric-row { display: flex; gap: var(--sp-3); flex-wrap: wrap; margin: var(--sp-3) 0; }
.metric-box { background: var(--c-surface); border-radius: var(--radius); padding: var(--sp-3) var(--sp-5); text-align: center; border: 1px solid var(--c-line); box-shadow: var(--shadow-sm); flex: 1; min-width: 120px; }
.metric-val { font-size: 26px; font-weight: 800; color: var(--c-primary); }
.metric-lbl { font-size: 10.5px; color: var(--c-muted); margin-top: 3px; text-transform: uppercase; letter-spacing: 0.4px; font-weight: 600; }

hr { margin: var(--sp-4) 0 !important; border-color: var(--c-line) !important; }
.stButton > button[kind="primary"] { background: var(--c-primary) !important; border: none !important; border-radius: var(--radius) !important; font-weight: 700 !important; }
div[data-testid="stExpander"] { border-radius: var(--radius) !important; border: 1px solid var(--c-line) !important; }

/* Premium Tab Styling Overrides */
.stTabs [data-baseweb="tab-list"] { gap: 8px; background-color: transparent; }
.stTabs [data-baseweb="tab"] { background-color: #EAECEE; border-radius: 6px 6px 0 0; padding: 10px 24px; font-weight: 600; font-size: 13.5px; color: var(--c-muted); border: none !important; }
.stTabs [aria-selected="true"] { background-color: var(--c-primary) !important; color: white !important; }
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
        "l3_obs": {c: {"pred": "", "conf": 0, "correct": ""} for c in [
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
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ── TOP ANCHORED APP BANNER ──────────────────────────────────────────────────
st.markdown("""
<div class="master-header">
    <h1>Session Journey of AI — Enterprise Portal</h1>
    <p>Learning &amp; Development Division Training Hub · Interactive Unified Single-Page Workflow Layout</p>
</div>
""", unsafe_allow_html=True)

# ── CENTRAL UNIFIED TAB LAYOUT SYSTEM ────────────────────────────────────────
tab_home, tab_lab1, tab_lab2, tab_lab3 = st.tabs([
    "🏠 Hub Overview Matrix", 
    "🛠️ Lab 1: Prompt Lab", 
    "🤖 Lab 2: Agentic Lab", 
    "📊 Lab 3: CV Model Lab"
])

# ── VIEWPORT 1: HUB OVERVIEW MATRIX ──────────────────────────────────────────
with tab_home:
    st.markdown("## Session Journey of AI")
    st.markdown(
        '<p style="font-size:14px;color:var(--c-muted);margin-top:-4px;max-width:680px">'
        "Welcome, Trainee. This continuous platform gives you three interactive labs that let you "
        "experience AI from the inside — no coding or local environment steps required.</p>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        l1_done = "Lab 1" in st.session_state.completed_labs
        st.markdown(f"""
        <div class="lab-card {'lab-card-green' if l1_done else ''}">
        <h3>Lab 1 · Prompt Lab</h3>
        <p style="font-size:13px;color:var(--c-muted);margin:8px 0;min-height:54px">See how prompt wording changes AI output quality for plant operations tasks.</p>
        <span class="badge badge-blue">45 min</span>
        <span class="badge badge-orange">Groups of 3–4</span>
        <div style="margin-top:12px; font-size:11px; font-weight:700; color:{'#1E8449' if l1_done else '#6B7785'}">
            {'● MODULE COMPLETED' if l1_done else '○ STATUS: PENDING EVALUATION'}
        </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        l2_done = "Lab 2" in st.session_state.completed_labs
        st.markdown(f"""
        <div class="lab-card lab-card-orange {'lab-card-green' if l2_done else ''}">
        <h3>Lab 2 · Agentic Solution Lab</h3>
        <p style="font-size:13px;color:var(--c-muted);margin:8px 0;min-height:54px">Simulate how an agentic AI platform plans, queries data, and gives recommendations autonomously.</p>
        <span class="badge badge-blue">45 min</span>
        <span class="badge badge-orange">Groups of 4–5</span>
        <div style="margin-top:12px; font-size:11px; font-weight:700; color:{'#1E8449' if l2_done else '#6B7785'}">
            {'● MODULE COMPLETED' if l2_done else '○ STATUS: PENDING EVALUATION'}
        </div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        l3_done = "Lab 3" in st.session_state.completed_labs
        st.markdown(f"""
        <div class="lab-card lab-card-purple {'lab-card-green' if l3_done else ''}">
        <h3>Lab 3 · ML Lab</h3>
        <p style="font-size:13px;color:var(--c-muted);margin:8px 0;min-height:54px">Train a real neural network in your browser for industrial computer-vision PPE detection safety checks.</p>
        <span class="badge badge-blue">45 min</span>
        <span class="badge badge-orange">Groups of 2–3</span>
        <div style="margin-top:12px; font-size:11px; font-weight:700; color:{'#1E8449' if l3_done else '#6B7785'}">
            {'● MODULE COMPLETED' if l3_done else '○ STATUS: PENDING EVALUATION'}
        </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Trainee Telemetry System Stats")
    m1, m2, m3, m4, m5 = st.columns(5)
    done_count = len(st.session_state.completed_labs)
    metrics = [
        (f"{done_count} / 3", "Completed Labs"),
        (f"{int((done_count/3)*100)}%", "Progress Rate"),
        ("0", "Lines of Code Req."),
        ("100%", "Browser Stable"),
        ("Active", "Runtime Link Engine")
    ]
    for col, (val, lbl) in zip([m1, m2, m3, m4, m5], metrics):
        with col:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-val">{val}</div>
                <div class="metric-lbl">{lbl}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.info("👆 Select tabs at the top center of this dashboard matrix to instantly step through any training environment module.")

# ── VIEWPORT 2: LAB 1 (PROMPT ENGINEERING) ──────────────────────────────────
with tab_lab1:
    st.markdown("## Lab 1 — Prompt Engineering Lab")
    st.markdown('<span class="badge badge-blue">45 min</span> <span class="badge badge-orange">Groups of 3–4</span>', unsafe_allow_html=True)

    st.markdown("""
    <div class="lab-card">
    <b>Learning Objective:</b> Experience firsthand how the structure and specificity of a prompt
    directly changes the quality of AI output — transitioning prompt entry from casual typing into a reliable engineering skill.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-banner">📐 The R-T-C-F-C Framework Control</div>', unsafe_allow_html=True)
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
            <div style="background:white;border-radius:8px;padding:12px;border-top:4px solid {color};box-shadow:0 2px 6px rgba(0,0,0,0.07);height:160px;">
                <div style="font-size:15px;font-weight:700;color:{color}">{elem}</div>
                <div style="font-size:12px;color:#444;margin:6px 0">{purpose}</div>
                <div style="font-size:11px;color:#777;font-style:italic">{example}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="section-banner">Exercise 1 — Weak vs Strong Prompt Analysis</div>', unsafe_allow_html=True)
    tab_a, tab_b = st.tabs(["Pair A: Safety Checklist", "Pair B: Maintenance Report"])

    with tab_a:
        col_weak, col_strong = st.columns(2)
        with col_weak:
            st.markdown("**❌ WEAK Prompt Entry**")
            st.markdown('<div class="prompt-box prompt-weak">Give me a safety checklist.</div>', unsafe_allow_html=True)
        with col_strong:
            st.markdown("**✅ STRONG Prompt Framework**")
            st.markdown("""
            <div class="prompt-box">
            You are a safety officer at a steel plant's blast furnace unit [Role]. Create a 7-point pre-shift safety checklist for furnace operators [Task]. This is for a 6-hour shift on Hot Strip Mill 2 [Context]. Format as a numbered list with a ☐ checkbox before each item [Format]. Keep language simple — operators are not engineers [Constraint].
            </div>
            """, unsafe_allow_html=True)

        st.markdown("**📝 Structural Assessment Sandbox Buffer:**")
        c1, c2 = st.columns(2)
        with c1:
            st.text_area("Weak prompt output logs", key="l1_a_weak_field", height=140, placeholder="Paste casual model output stream...")
        with c2:
            st.text_area("Strong prompt output logs", key="l1_a_strong_field", height=140, placeholder="Paste engineered model output stream...")

    with tab_b:
        col_weak2, col_strong2 = st.columns(2)
        with col_weak2:
            st.markdown("**❌ WEAK Prompt Entry**")
            st.markdown('<div class="prompt-box prompt-weak">Write a maintenance report.</div>', unsafe_allow_html=True)
        with col_strong2:
            st.markdown("**✅ STRONG Prompt Framework**")
            st.markdown("""
            <div class="prompt-box">
            Write a maintenance incident report [Task]. Situation: A main bearing in Hot Strip Mill showed abnormal vibration (sensor reading: 8.2 mm/s, threshold: 4.5 mm/s) for 3 consecutive days [Context]. Maintenance team replaced bearing on 28 May 2025. Downtime: 4 hours [Context]. Format: Date / Equipment / Observation / Action Taken / Downtime / Next Inspection Date [Format].
            </div>
            """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.text_area("Weak output logs", key="l1_b_weak_field", height=140, placeholder="Paste text output content...")
        with c2:
            st.text_area("Strong output logs", key="l1_b_strong_field", height=140, placeholder="Paste text output content...")

    st.markdown('<div class="section-banner">Exercise 2 — Write Your Own Custom Prompt Constraint</div>', unsafe_allow_html=True)
    scenario_options = {
        "A": "Explain why predictive maintenance is better than reactive maintenance — for a furnace operator who has never heard of AI.",
        "B": "Write a short SOP for safe PPE usage in the casting section.",
        "C": "Summarise a conveyor belt motor trip at 2 AM (2 hours downtime) into 3 bullet points for a plant manager.",
        "D": "Create 5 quiz questions about blast furnace hazards for a trainee exam.",
    }
    sel_scen = st.selectbox("Pick target operational scenario configuration:", [f"Scenario {k}: {v}" for k, v in scenario_options.items()])

    st.markdown("**Build structured segment blocks below:**")
    cx1, cx2, cx3, cx4, cx5 = st.columns(5)
    p_parts = {}
    for col, lbl, ph in zip([cx1, cx2, cx3, cx4, cx5], ["Role", "Task", "Context", "Format", "Constraint"], ["Professional role...", "Core instruction...", "Data metrics...", "Layout structure...", "Operational limits..."]):
        with col:
            p_parts[lbl] = st.text_input(f"Define {lbl}:", placeholder=ph, key=f"l1_part_field_{lbl}")

    if any(p_parts.values()):
        comb_str = " ".join([f"[{k}: {v}]" for k, v in p_parts.items() if v])
        st.markdown("**Assembled Resulting Prompt Output Structure:**")
        st.markdown(f'<div class="prompt-box">{comb_str}</div>', unsafe_allow_html=True)

    st.text_area("Model Response Sandbox Evaluator Target:", key="l1_ex2_out_main", height=120, placeholder="Input system returned code data here...")

    st.markdown('<div class="section-banner">Exercise 3 — Sequential Chain Prompting Processes</div>', unsafe_allow_html=True)
    chain_prompts = [
        ("Starter — Diagnose", 'You are a maintenance engineer at a steel plant. I have a blast furnace bearing showing 75% failure probability within 5 days. List 3 possible causes and what data I should check for each.'),
        ("Step 2 — Action Plan", 'Now assume the first cause is correct. Write a step-by-step action plan for the shift engineer to follow in the next 48 hours.'),
        ("Step 3 — Write Email", 'Convert that action plan into a formal email I can send to my plant manager.'),
        ("Step 4 — Shorten Matrix", 'Now make the email shorter — maximum 5 sentences. Subject line included.'),
    ]
    for idx, (title, p_text) in enumerate(chain_prompts):
        with st.expander(f"Prompt Connection Sequence {idx+1}: {title}"):
            st.markdown(f'<div class="prompt-box">{p_text}</div>', unsafe_allow_html=True)
            st.text_area("Record Sequence Log Return Data:", key=f"l1_chain_field_{idx}", height=100, placeholder="Log response records...")

    st.markdown('<div class="section-banner">💬 Debrief Assessment Ledger</div>', unsafe_allow_html=True)
    for q in ["What's the plant risk if an operator gives vague context during a safety-critical task?", "How is writing a structured prompt similar to writing a good job card or work order?", "In chain prompting, what happened to the email between Step 3 and Step 4?", "Which of the 5 R-T-C-F-C elements had the biggest impact on output quality?"]:
        st.text_area(q, key=f"l1_debrief_field_{q[:15]}", height=70, placeholder="Input response insight observations...")

    if st.button("Commit Lab 1 Data Profile", type="primary", key="btn_save_l1"):
        st.session_state.completed_labs.add("Lab 1")
        st.toast("Lab 1 Completed.", icon="📝")
        st.rerun()

# ── VIEWPORT 3: LAB 2 (AGENTIC ORCHESTRATION) ────────────────────────────────
with tab_lab2:
    st.markdown("## Lab 2 — Agentic Solution Lab")
    st.markdown('<span class="badge badge-blue">45 min</span> <span class="badge badge-orange">Role-play simulation workflow</span>', unsafe_allow_html=True)

    st.markdown("""
    <div class="lab-card lab-card-orange">
    <b>Learning Objective:</b> Simulate how an agentic AI platform receives a goal, plans steps, queries databases, and generates a recommendation autonomously using the <b>ReAct (Reasoning + Acting)</b> loop.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-banner">👥 Role Allocations Matrix</div>', unsafe_allow_html=True)
    roles = [
        ("USER", "Plant Shift Manager", "Read the scenario aloud. You trigger the agent runtime loop.", "#0F3D61"),
        ("AGENT BRAIN", "Core AI Orchestrator", "Follow the 7-step script protocol. Speak items aloud.", "#15517F"),
        ("DATA CALLER 1", "Sensor Database API", "Read your sensor data constraints block when queried.", "#C5821A"),
        ("DATA CALLER 2", "Maintenance Log Ledger", "Read your recorded ledger cards when queried.", "#1E8449"),
        ("DATA CALLER 3", "Inventory Components Stock", "Read component balance profiles when metrics match.", "#B03A2E"),
        ("HUMAN APPROVER", "Plant Lead Executive", "Receive calculation summary recommendations. Overrule or sign-off.", "#3A4A5A"),
    ]
    rl_cols = st.columns(3)
    for idx, (role, persona, duty, color) in enumerate(roles):
        with rl_cols[idx % 3]:
            st.markdown(f"""
            <div style="background:white;border-radius:8px;padding:12px 14px;margin:6px 0;border-left:4px solid {color};box-shadow:0 2px 6px rgba(0,0,0,0.07);">
                <div style="font-size:13px;font-weight:700;color:{color}">{role}</div>
                <div style="font-size:12px;font-weight:600;color:#0F3D61">{persona}</div>
                <div style="font-size:12px;color:#666;margin-top:4px">{duty}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="section-banner">🚨 Target System Scenario Context</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="data-card data-card-blue">
        <b style="font-size:15px;color:#0F3D61">System Core Diagnostics: Blast Furnace 02</b><br><br>
        <span style="font-size:14px;line-height:1.8">
        Predictive telemetry arrays monitor an amber warning flag loop on asset bearing <b>MB-7</b> tracking an imminent <b>75% failure curve within a 5-day operation window</b>. Core engine requires multi-database parsing routines to optimize remediation.
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-banner">🃏 Enterprise DB System Data Cards</div>', unsafe_allow_html=True)
    dc1, dc2, dc3 = st.columns(3)
    with dc1:
        with st.expander("📡 DATA CARD 1 — Real-time Telemetry DB"):
            st.markdown('<div class="data-card data-card-blue"><b>MB-7 Vibration Profile:</b> 8.6 mm/s <span style="color:red">(Limit: 4.5 mm/s ⚠️)</span><br><b>MB-7 Thermal Core:</b> 94°C <span style="color:red">(Normal: &lt;75°C ⚠️)</span><br><b>Trendline Analysis:</b> Rising over 6 continuous days</div>', unsafe_allow_html=True)
    with dc2:
        with st.expander("🔧 DATA CARD 2 — Maintenance Lifecycle Log"):
            st.markdown('<div class="data-card data-card-green"><b>Lifecycle Interval:</b> 14 months active <span style="color:red">(Cycle Limit: 12 months ⚠️)</span><br><b>Lubrication Sync:</b> 3 weeks elapsed <span style="color:red">(Required: 2 weeks ⚠️)</span><br><b>Historical Event Risk:</b> Component failure downtime triggers standard ₹8.4 Lakh impact cost.</div>', unsafe_allow_html=True)
    with dc3:
        with st.expander("📦 DATA CARD 3 — ERP Inventory Tracking System"):
            st.markdown('<div class="data-card data-card-orange"><b>SKF-22230 Units in Stock:</b> 2 components available ✅<br><b>Swap Duration:</b> 6 operational hours required<br><b>Next Scheduled Line Stop:</b> 8 calendar days <span style="color:red">(Critical Delay Window ⚠️)</span></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-banner">🧠 Automated ReAct Framework Pipeline Traces</div>', unsafe_allow_html=True)
    agent_steps = [
        ("1", "Acknowledge Objective Goal", "Goal tracking initialized. MB-7 asset tracking limits breached. Beginning context verification passes.", "#0F3D61"),
        ("2", "Formulate Task Plan", "Iterating sub-queries across live streams: (a) raw telemetry feeds, (b) maintenance intervals, (c) supply chain parts logs.", "#15517F"),
        ("3", "Query Telemetry DB API", "Calling data endpoints for structural sensor trends and acceleration statistics.", "#C5821A"),
        ("4", "Query Lifecycle Database", "Requesting service history and tracking degradation logs.", "#1E8449"),
        ("5", "Query Supply Inventory API", "Verifying parts buffer volumes and physical distribution centers location maps.", "#B03A2E"),
        ("6", "Synthesise System Logic Matrix", "Consolidating constraints: bearing thermal thresholds critically high. Stock records show local items clear. Running line trade-offs.", "#C5821A"),
        ("7", "Compile System Recommendation", "CRITICAL RECOMMENDATION: Secure scheduling to execute component swap immediately following active delivery completion window in 72 hours. Elevate safety monitoring cycles.", "#1E8449")
    ]
    for num, title, script, color in agent_steps:
        st.markdown(f"""
        <div style="display:flex;gap:12px;align-items:flex-start;margin:8px 0;background:white;border-radius:8px;padding:12px 14px;border:1px solid #E2E8F0;">
            <div style="background:{color};color:white;width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px;flex-shrink:0;">{num}</div>
            <div>
                <div style="font-weight:600;font-size:13px;color:#0F3D61">{title}</div>
                <div style="font-style:italic;font-size:13px;color:#444;margin-top:3px">"{script}"</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-banner">📝 Core Data Extraction Capture Blocks</div>', unsafe_allow_html=True)
    f_c1, f_c2, f_c3 = st.columns(3)
    with f_c1:
        st.session_state.l2_notes["sensors"] = st.text_area("Log Telemetry Feeds Analytics:", value=st.session_state.l2_notes["sensors"], height=90, placeholder="Extract parameters...")
    with f_c2:
        st.session_state.l2_notes["maintenance"] = st.text_area("Log Maintenance Record Profiles:", value=st.session_state.l2_notes["maintenance"], height=90, placeholder="Extract parameters...")
    with f_c3:
        st.session_state.l2_notes["inventory"] = st.text_area("Log Inventory Balance Counts:", value=st.session_state.l2_notes["inventory"], height=90, placeholder="Extract parameters...")

    st.markdown('<div class="section-banner">👔 Executive Decision Control Interface</div>', unsafe_allow_html=True)
    st.radio("Sign-off Recommendation Action Level:", ["✅ Approve Action Path — Standardize deployment parameters post 72hr order completion", "🔄 Alter Action Path — Trigger instant system line emergency shutdown sequence", "❌ Override Logic — Suppress warning flags, cycle review parameters in 48 hours"], key="l2_radio_decision")
    st.text_area("Provide Business Justification Ledger Summary:", key="l2_just_input_box", height=80, placeholder="Define operational justifications...")

    st.markdown('<div class="section-banner">🔍 Edge Case Failure Mechanics & Structural Vulnerabilities</div>', unsafe_allow_html=True)
    st.text_area("How must the model's recommendation shift if inventory logs report zero physical safety stock metrics?", key="l2_edge_1", height=70, placeholder="Trace secondary backup decision workflows...")
    st.text_area("When execution optimization sequences compress to sub-second processing, how does real-time intervention reshape risk metrics?", key="l2_edge_2", height=70, placeholder="Analyze technical operational benefits...")

    st.markdown('<div class="section-banner">💬 Debrief Assessment Ledger</div>', unsafe_allow_html=True)
    for q in ["What data point had the biggest influence on the Agent Brain's recommendation?", "Can the Agent Brain ever be wrong? What is the human's role?", "Name one real-world AI agent (from the session) that follows this exact same loop."]:
        st.text_area(q, key=f"l2_deb_field_{q[:15]}", height=70, placeholder="Input response insight observations...")

    if st.button("Commit Lab 2 Data Profile", type="primary", key="btn_save_l2"):
        st.session_state.completed_labs.add("Lab 2")
        st.toast("Lab 2 Completed.", icon="🤖")
        st.rerun()

# ── VIEWPORT 4: LAB 3 (COMPUTER VISION INFERENCE) ────────────────────────────
with tab_lab3:
    st.markdown("## Lab 3 — ML Lab: Train a Real AI Model")
    st.markdown('<span class="badge badge-blue">45 min</span> <span class="badge badge-green">teachablemachine.withgoogle.com link layer</span>', unsafe_allow_html=True)

    st.markdown("""
    <div class="lab-card lab-card-green">
    <b>Learning Objective:</b> Train a real neural network image classifier in your browser. Experience what 'training data', 'model accuracy', 'confidence scores', and 'inference' actually mean — the same mechanics behind industrial computer-vision safety systems.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-banner">🚀 Step 1 — Initialize Environment Setup</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background:white;border-radius:8px;padding:16px 20px;border:1px solid #E2E8F0;margin:8px 0;">
        <ol style="font-size:13.5px;line-height:2.2;color:#1A1A2E;">
            <li>Access the interface workspace window: <a href="https://teachablemachine.withgoogle.com" target="_blank"><b>teachablemachine.withgoogle.com</b></a></li>
            <li>Select <b>Get Started</b> context links followed by <b>Image Project</b> configuration paths.</li>
            <li>Configure standard structure options: <b>Standard Image Model</b>.</li>
            <li>Map classification parameter labels: <code>Class 1</code> → <b>PPE ON</b> and <code>Class 2</code> → <b>PPE OFF</b>.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    c_open = st.checkbox("Teachable Machine cloud connection active and parameters mapped.", key="chk_l3_open")

    if c_open:
        st.markdown('<div class="section-banner">📸 Step 2 — Frame Image Capture Quantities</div>', unsafe_allow_html=True)
        img_c1, img_c2 = st.columns(2)
        with img_c1:
            st.markdown('<div class="data-card data-card-green"><b style="color:#1E8449">TARGET CLASS 1: PPE ON</b><br><br>• Mount safety helmet or standard protective headgear.<br>• Hold webcam collection action trigger loop.<br>• Target volume: <b>60–80 structured image frames</b>.</div>', unsafe_allow_html=True)
        with img_c2:
            st.markdown('<div class="data-card data-card-blue"><b style="color:#0F3D61">TARGET CLASS 2: PPE OFF</b><br><br>• Strip all structural headgear components completely.<br>• Preserve consistent background alignment vectors.<br>• Target volume: <b>60–80 structured image frames</b>.</div>', unsafe_allow_html=True)
        c_imgs = st.checkbox("Array dataset balance complete across target nodes.", key="chk_l3_imgs")

        if c_imgs:
            st.markdown('<div class="section-banner">⚙️ Step 3 — Compute Network Weights Optimization</div>', unsafe_allow_html=True)
            st.markdown('<div style="background:#0F3D61;color:white;border-radius:8px;padding:14px 18px;margin:8px 0;">Select the primary <b>Train Model</b> interface array. Retain screen focus path state while backpropagation algorithms calculate parameter distributions weights.</div>', unsafe_allow_html=True)
            c_train = st.checkbox("Network calculations compiled. Local inference loops engine active.", key="chk_l3_train")

            if c_train:
                st.markdown('<div class="section-banner">🧪 Step 4 — Matrix Verification Analysis & Confidence Logging</div>', unsafe_allow_html=True)
                
                t_conds = [
                    "Helmet on, facing forward",
                    "Helmet on, sideways",
                    "No helmet, forward",
                    "No helmet, dim lighting",
                    "Helmet tilted / partial",
                    "Different person with helmet"
                ]
                
                th_cols = st.columns([3, 2, 2, 2])
                th_cols[0].markdown("**Target Test Vector Matrix**")
                th_cols[1].markdown("**Predicted Return Class**")
                th_cols[2].markdown("**Confidence Index (%)**")
                th_cols[3].markdown("**Verification Pass (Y/N)**")
                st.markdown("<hr style='margin:4px 0'>", unsafe_allow_html=True)

                for cond in t_conds:
                    row_cols = st.columns([3, 2, 2, 2])
                    with row_cols[0]:
                        st.markdown(f"<div style='padding:6px 0;font-size:13px'>{cond}</div>", unsafe_allow_html=True)
                    with row_cols[1]:
                        s_pred = st.selectbox("", ["", "PPE ON", "PPE OFF"], key=f"sel_pred_{cond.replace(' ', '_')}", label_visibility="collapsed")
                    with row_cols[2]:
                        s_conf = st.number_input("", min_value=0, max_value=100, step=1, key=f"num_conf_{cond.replace(' ', '_')}", label_visibility="collapsed")
                    with row_cols[3]:
                        s_corr = st.selectbox("", ["", "Y", "N"], key=f"sel_corr_{cond.replace(' ', '_')}", label_visibility="collapsed")
                    st.session_state.l3_obs[cond] = {"pred": s_pred, "conf": s_conf, "correct": s_corr}

                f_entries = [v for v in st.session_state.l3_obs.values() if v["correct"] in ["Y", "N"]]
                if f_entries:
                    y_count = sum(1 for v in f_entries if v["correct"] == "Y")
                    calc_acc = round((y_count / len(f_entries)) * 100)
                    mean_conf = sum(v["conf"] for v in f_entries) / len(f_entries)
                    
                    st.markdown('<div class="section-banner">Real-time Performance Telemetry Metrics</div>', unsafe_allow_html=True)
                    ev_c1, ev_c2, ev_c3 = st.columns(3)
                    with ev_c1:
                        v_color = "#1E8449" if calc_acc >= 80 else ("#C5821A" if calc_acc >= 60 else "#B03A2E")
                        st.markdown(f'<div class="metric-box"><div class="metric-val" style="color:{v_color}">{calc_acc}%</div><div class="metric-lbl">Dataset Validation Accuracy</div></div>', unsafe_allow_html=True)
                    with ev_c2:
                        st.markdown(f'<div class="metric-box"><div class="metric-val" style="color:#0F3D61">{y_count}/{len(f_entries)}</div><div class="metric-lbl">True Positive Assertions</div></div>', unsafe_allow_html=True)
                    with ev_c3:
                        st.markdown(f'<div class="metric-box"><div class="metric-val" style="color:#15517F">{round(mean_conf)}%</div><div class="metric-lbl">Mean Network Certainty Index</div></div>', unsafe_allow_html=True)

                st.markdown("---")
                st.text_area("Analyze edge boundaries drift patterns when scene luminosity or angular shifts manifest:", key="txt_l3_edge_obs", height=70, placeholder="Log accuracy notes...")
                st.text_area("Define optimization procedures to extend neural map boundary boundaries stability:", key="txt_l3_opt_notes", height=70, placeholder="Log architectural adjustments...")

                st.markdown('<div class="section-banner">🏆 High-Value Industrial Extensions Sandbox</div>', unsafe_allow_html=True)
                challs = [
                    ("Multi-Class Layer Expansion", "Introduce class 3 structures: PARTIAL COMPLIANCE tracking displaced gear elements.", "#15517F"),
                    ("Adversarial System Spoofing Checks", "Render high-definition system image representations via flat mobile viewports to evaluate spoof patterns.", "#B03A2E"),
                    ("Dataset Variance Compression", "Diminish validation baseline volumes down to 20 samples to identify overfitting decay metrics.", "#C5821A"),
                    ("Luminance Disparity Evaluation", "Execute parameters optimization sweeps inside high exposure matrices and monitor twilight limits tracking.", "#0F3D61")
                ]
                ch_cols = st.columns(2)
                for idx, (title, info_str, c_hex) in enumerate(challs):
                    with ch_cols[idx % 2]:
                        st.checkbox(f"Initialize {title}", key=f"chk_ext_run_{idx}")
                        st.markdown(f'<div style="background:white;border-radius:8px;padding:10px 14px;border-left:3px solid {c_hex};margin-bottom:8px;font-size:12px;color:#444">{info_str}</div>', unsafe_allow_html=True)

                st.markdown('<div class="section-banner">🔗 Enterprise System Scales Contrast Alignment Map</div>', unsafe_allow_html=True)
                aligns = [
                    ("Local set: 80 active web frames gathered", "Enterprise networks process unified camera matrices multi-stream matrix arrays"),
                    ("Manual definition configuration maps: 2 labels", "Cloud databases deploy complex multi-tier ontological tags dictionaries"),
                    ("Local CPU run durations: 60 seconds", "Distributed clusters run cloud parallelized pipeline matrix routines"),
                    ("Single room validation test vectors parameters", "Production arrays pass extreme physical climate variations filter sets"),
                    ("Experimental pipeline limits target ~85%", "Mission-critical production gates require certified targets exceeding 99.4%")
                ]
                for l_str, e_str in aligns:
                    ax1, ax2 = st.columns(2)
                    with ax1: st.markdown(f'<div style="background:#EBF4FB;border-radius:6px;padding:8px 12px;font-size:12px;margin:3px 0">🧑‍💻 {l_str}</div>', unsafe_allow_html=True)
                    with ax2: st.markdown(f'<div style="background:#E9F7EF;border-radius:6px;padding:8px 12px;font-size:12px;margin:3px 0">🏭 {e_str}</div>', unsafe_allow_html=True)

                st.markdown('<div class="section-banner">💬 Debrief Assessment Ledger</div>', unsafe_allow_html=True)
                for q in ["Why did confidence drop when lighting changed? What does this mean for blast furnace deployment?", "If this model had 15% error at a real factory gate, what are the safety consequences?", "What is the human's role after a model is deployed?"]:
                    st.text_area(q, key=f"l3_deb_field_{q[:15]}", height=70, placeholder="Input response insight observations...")

    if st.button("Commit Lab 3 Data Profile", type="primary", key="btn_save_l3"):
        st.session_state.completed_labs.add("Lab 3")
        st.toast("Lab 3 Completed.", icon="📊")
        st.rerun()

# ── GLOBAL PROGRAM INTEGRATION NOTIFICATION BANNER ───────────────────────────
if len(st.session_state.completed_labs) == 3:
    st.markdown('<div style="margin-top:32px; border-bottom:2px dashed var(--c-line);"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background:var(--c-primary);color:#FFFFFF;border-radius:var(--radius);padding:24px;text-align:center;margin-top:24px;box-shadow:var(--shadow-md);">
        <div style="font-size:32px">🏆</div>
        <div style="font-size:20px;font-weight:700;color:#FFFFFF;margin-top:8px;">Curriculum Performance Evaluation Phase Complete</div>
        <div style="color:#D4E6F1;font-size:13px;margin-top:6px;max-width:700px;margin-left:auto;margin-right:auto;line-height:1.5;opacity:0.9;">
            All laboratory modules have successfully committed session state parameters. Trainee analysis profiles are compiled and available for enterprise integration records.
        </div>
    </div>
    """, unsafe_allow_html=True)
