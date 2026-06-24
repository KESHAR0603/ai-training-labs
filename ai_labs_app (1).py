import streamlit as st

st.set_page_config(
    page_title="AI Labs — Session Journey of AI",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── GLOBAL CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Reset & tokens ── */
:root {
  --navy:      #0F3D61;
  --navy2:     #15517F;
  --amber:     #C5821A;
  --amber-lt:  #FBF1E2;
  --green:     #1A7A45;
  --green-lt:  #E8F5EE;
  --red:       #B03A2E;
  --red-lt:    #FBEAE8;
  --ink:       #1B2430;
  --muted:     #6B7785;
  --line:      #E3E7EC;
  --surface:   #FFFFFF;
  --bg:        #F2F5F9;
  --r:         10px;
}
html, body, [class*="css"] {
  font-family: 'Inter', sans-serif !important;
  color: var(--ink);
}
.main .block-container {
  padding: 0 !important;
  max-width: 100% !important;
}
/* Hide default streamlit sidebar toggle & header */
[data-testid="collapsedControl"] { display: none !important; }
header[data-testid="stHeader"]   { display: none !important; }

/* ── HERO BANNER ── */
.hero {
  background: linear-gradient(120deg, #0B2C46 0%, #0F3D61 55%, #1A5F8A 100%);
  padding: 48px 60px 40px;
  border-bottom: 3px solid var(--amber);
}
.hero-eyebrow {
  font-size: 11px; font-weight: 700; letter-spacing: 2px;
  color: var(--amber); text-transform: uppercase; margin-bottom: 10px;
}
.hero-title {
  font-size: 36px; font-weight: 800; color: #fff;
  line-height: 1.15; margin-bottom: 8px; letter-spacing: -0.5px;
}
.hero-sub {
  font-size: 15px; color: #8BB8D4; max-width: 620px; line-height: 1.6;
}
.hero-badges { margin-top: 20px; display: flex; gap: 10px; flex-wrap: wrap; }
.hb {
  background: rgba(255,255,255,0.10); border: 1px solid rgba(255,255,255,0.18);
  color: #C8DFF0; border-radius: 999px; font-size: 12px; font-weight: 600;
  padding: 5px 14px; letter-spacing: 0.2px;
}

/* ── LAB HEADER STRIP ── */
.lab-strip {
  display: flex; align-items: center; gap: 16px;
  background: var(--surface); border-bottom: 1px solid var(--line);
  padding: 18px 60px;
  position: sticky; top: 0; z-index: 100;
  box-shadow: 0 2px 8px rgba(15,61,97,0.07);
}
.lab-pill {
  border-radius: 999px; padding: 6px 18px; font-size: 13px; font-weight: 700;
  cursor: pointer; border: 2px solid transparent; white-space: nowrap;
  text-decoration: none;
}
.pill-1 { background:#EAF1F7; color:var(--navy);  border-color:var(--navy); }
.pill-2 { background:var(--amber-lt); color:#7A4F10; border-color:var(--amber); }
.pill-3 { background:var(--green-lt); color:var(--green); border-color:var(--green); }
.strip-title { font-size: 13px; font-weight: 600; color: var(--muted); margin-left: auto; }

/* ── SECTION WRAPPER ── */
.lab-section { padding: 48px 60px; }
.lab-section:nth-child(odd) { background: var(--bg); }
.lab-section:nth-child(even) { background: var(--surface); }

/* ── LAB TITLE ── */
.lab-title-row { display: flex; align-items: center; gap: 14px; margin-bottom: 6px; }
.lab-num {
  width: 44px; height: 44px; border-radius: 50%; display: flex;
  align-items: center; justify-content: center;
  font-size: 18px; font-weight: 800; color: #fff; flex-shrink: 0;
}
.ln-1 { background: var(--navy); }
.ln-2 { background: var(--amber); }
.ln-3 { background: var(--green); }
.lab-title { font-size: 24px; font-weight: 800; color: var(--navy); letter-spacing: -0.3px; }
.lab-obj {
  background: var(--surface); border-left: 4px solid var(--navy);
  border-radius: 0 var(--r) var(--r) 0;
  padding: 12px 18px; font-size: 13.5px; color: var(--ink);
  margin: 12px 0 28px; line-height: 1.6;
  box-shadow: 0 1px 4px rgba(15,61,97,0.06);
}
.lab-obj-amber { border-left-color: var(--amber); }
.lab-obj-green { border-left-color: var(--green); }

/* ── SECTION BANNER ── */
.sec-banner {
  background: var(--navy); color: #fff; padding: 9px 16px;
  border-radius: var(--r); font-size: 13.5px; font-weight: 700;
  margin: 28px 0 14px; letter-spacing: 0.1px;
}
.sec-banner-amber { background: var(--amber); }
.sec-banner-green { background: var(--green); }

/* ── FRAMEWORK CARDS ── */
.fw-grid { display: grid; grid-template-columns: repeat(5,1fr); gap: 10px; margin-bottom: 4px; }
.fw-card {
  background: var(--surface); border-radius: var(--r); padding: 14px;
  border-top: 4px solid; box-shadow: 0 2px 6px rgba(15,61,97,0.07);
}
.fw-letter { font-size: 18px; font-weight: 800; margin-bottom: 4px; }
.fw-word   { font-size: 13px; font-weight: 700; margin-bottom: 6px; }
.fw-desc   { font-size: 11.5px; color: var(--muted); line-height: 1.4; margin-bottom: 6px; }
.fw-eg     { font-size: 11px; font-style: italic; color: #888; }

/* ── PROMPT BOXES ── */
.prompt-weak {
  background: #2B1714; color: #E8A9A2;
  border-left: 3px solid var(--red);
  border-radius: var(--r); padding: 14px 18px;
  font-family: 'JetBrains Mono', monospace; font-size: 12.5px; line-height: 1.7;
  margin: 8px 0;
}
.prompt-strong {
  background: var(--navy); color: #BFD9EC;
  border-left: 3px solid var(--amber);
  border-radius: var(--r); padding: 14px 18px;
  font-family: 'JetBrains Mono', monospace; font-size: 12.5px; line-height: 1.7;
  margin: 8px 0;
}
.prompt-chain {
  background: #0A2438; color: #A8CCE4;
  border-left: 3px solid var(--green);
  border-radius: var(--r); padding: 14px 18px;
  font-family: 'JetBrains Mono', monospace; font-size: 12.5px; line-height: 1.7;
  margin: 8px 0;
}
.label-weak   { display:inline-block; background:var(--red-lt); color:var(--red);
                border-radius:999px; font-size:11px; font-weight:700;
                padding:3px 10px; margin-bottom:6px; }
.label-strong { display:inline-block; background:#EAF1F7; color:var(--navy);
                border-radius:999px; font-size:11px; font-weight:700;
                padding:3px 10px; margin-bottom:6px; }

/* ── ROLE CARDS ── */
.role-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; margin:4px 0 20px; }
.role-card {
  background: var(--surface); border-radius: var(--r); padding: 14px 16px;
  border-left: 4px solid; box-shadow: 0 2px 6px rgba(15,61,97,0.06);
}
.role-title  { font-size: 12px; font-weight: 800; text-transform: uppercase;
               letter-spacing: 0.5px; margin-bottom: 3px; }
.role-person { font-size: 13px; font-weight: 600; color: var(--navy); margin-bottom: 5px; }
.role-duty   { font-size: 12px; color: var(--muted); line-height: 1.4; }

/* ── DATA CARDS ── */
.data-card {
  background: var(--surface); border-radius: var(--r); padding: 16px 20px;
  border: 1px solid var(--line); border-left: 4px solid;
  box-shadow: 0 2px 6px rgba(15,61,97,0.05); font-size: 13px; line-height: 1.7;
}
.dc-blue   { border-left-color: var(--navy); }
.dc-green  { border-left-color: var(--green); }
.dc-amber  { border-left-color: var(--amber); }
.warn { color: var(--red); font-weight: 600; }

/* ── AGENT STEPS ── */
.agent-step {
  display: flex; gap: 12px; align-items: flex-start;
  background: var(--surface); border-radius: var(--r);
  padding: 12px 16px; margin: 6px 0;
  border: 1px solid var(--line);
}
.agent-num {
  width: 30px; height: 30px; border-radius: 50%; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center;
  font-size: 13px; font-weight: 800; color: #fff;
}
.agent-label  { font-size: 12px; font-weight: 700; color: var(--navy); }
.agent-script { font-size: 12.5px; font-style: italic; color: var(--muted);
                margin-top: 2px; line-height: 1.5; }

/* ── SCENARIO ALERT ── */
.scenario-alert {
  background: #FFF8E6; border: 2px solid var(--amber);
  border-radius: var(--r); padding: 20px 24px; margin: 10px 0 20px;
}
.sa-head { font-size: 14px; font-weight: 800; color: #7A4F10; margin-bottom: 8px; }
.sa-body { font-size: 13.5px; color: var(--ink); line-height: 1.7; }

/* ── ML STEP CARDS ── */
.ml-step {
  display: flex; gap: 14px; align-items: flex-start;
  background: var(--surface); border-radius: var(--r);
  padding: 14px 18px; margin: 8px 0;
  border: 1px solid var(--line);
  box-shadow: 0 1px 3px rgba(15,61,97,0.05);
}
.ml-num {
  width: 32px; height: 32px; border-radius: 50%; flex-shrink: 0;
  background: var(--green); color: #fff;
  display: flex; align-items: center; justify-content: center;
  font-size: 14px; font-weight: 800;
}
.ml-label { font-size: 13px; font-weight: 700; color: var(--green); }
.ml-body  { font-size: 13px; color: var(--ink); line-height: 1.6; margin-top: 2px; }

/* ── SCALE TABLE ── */
.scale-row { display:grid; grid-template-columns:1fr 1fr; gap:8px; margin:6px 0; }
.scale-you  { background:#EAF1F7; border-radius:8px; padding:9px 14px;
              font-size:12.5px; color:var(--navy); }
.scale-ind  { background:var(--green-lt); border-radius:8px; padding:9px 14px;
              font-size:12.5px; color:var(--green); }

/* ── METRIC BOXES ── */
.metric-row { display:flex; gap:10px; flex-wrap:wrap; margin:12px 0; }
.metric-box {
  background: var(--surface); border-radius: var(--r);
  padding: 14px 20px; text-align:center;
  border: 1px solid var(--line);
  box-shadow: 0 1px 3px rgba(15,61,97,0.05);
  flex:1; min-width:110px;
}
.metric-val { font-size:26px; font-weight:800; color:var(--navy); }
.metric-lbl { font-size:10px; color:var(--muted); margin-top:3px;
              text-transform:uppercase; letter-spacing:0.5px; font-weight:600; }

/* ── DEBRIEF BOX ── */
.debrief-box {
  background: #F7F2EA; border-left: 4px solid var(--amber);
  border-radius: 0 var(--r) var(--r) 0;
  padding: 16px 20px; margin: 10px 0;
}
.debrief-q { font-size: 13px; font-weight: 600; color: var(--ink); margin-bottom: 2px; }

/* ── COMPLETION BANNER ── */
.complete-banner {
  background: linear-gradient(120deg, #0B2C46, #0F3D61);
  border-radius: var(--r); padding: 32px; text-align: center; margin-top: 20px;
}
.cb-icon { font-size: 40px; }
.cb-title { font-size: 22px; font-weight: 800; color: #fff; margin: 10px 0 8px; }
.cb-sub   { font-size: 13.5px; color: #8BB8D4; line-height: 1.6; }

/* ── Streamlit widget overrides ── */
div[data-testid="stTextArea"] textarea,
div[data-testid="stTextInput"] input {
  border-radius: 8px !important;
  border: 1.5px solid var(--line) !important;
  font-family: 'Inter', sans-serif !important;
  font-size: 13px !important;
}
div[data-testid="stTextArea"] textarea:focus,
div[data-testid="stTextInput"] input:focus {
  border-color: var(--navy) !important;
  box-shadow: 0 0 0 3px rgba(15,61,97,0.12) !important;
}
.stButton > button {
  border-radius: 8px !important; font-weight: 700 !important;
  font-size: 13px !important;
}
.stButton > button[kind="primary"] {
  background: var(--navy) !important; border: none !important; color: #fff !important;
}
div[data-testid="stSelectbox"] > div { border-radius: 8px !important; }
div[data-testid="stCheckbox"] label { font-size: 13.5px !important; font-weight: 500 !important; }
div[data-testid="stExpander"] {
  border-radius: var(--r) !important;
  border: 1.5px solid var(--line) !important;
}
.stTabs [data-baseweb="tab"] {
  font-size: 13px !important; font-weight: 600 !important;
}
.stSuccess { border-radius: var(--r) !important; }
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ─────────────────────────────────────────────────────────────
def init():
    defaults = {
        "l3_obs": {c: {"pred": "", "conf": 0, "correct": ""}
                   for c in ["Helmet on, facing forward", "Helmet on, sideways",
                              "No helmet, forward", "No helmet, dim lighting",
                              "Helmet tilted / partial", "Different person with helmet"]},
        "l2_notes": {"sensors": "", "maintenance": "", "inventory": ""},
        "completed": set(),
        "confirm_open": False, "images_done": False, "training_done": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
init()

# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero">
  <div class="hero-eyebrow">L&D Division · Training Programme 2025–26</div>
  <div class="hero-title">Session Journey of AI<br>Hands-On Lab Platform</div>
  <div class="hero-sub">
    Three interactive labs. One page. No navigation needed.<br>
    Scroll down to work through Prompt Engineering, Agentic AI, and Machine Learning — hands on.
  </div>
  <div class="hero-badges">
    <span class="hb">🛠️ Lab 1 — Prompt Lab</span>
    <span class="hb">🤖 Lab 2 — Agentic Solution Lab</span>
    <span class="hb">📊 Lab 3 — ML Lab</span>
    <span class="hb">45 min each · Zero coding</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── STICKY NAV STRIP ──────────────────────────────────────────────────────────
st.markdown("""
<div class="lab-strip">
  <a class="lab-pill pill-1" href="#lab1">🛠️ Lab 1 · Prompt</a>
  <a class="lab-pill pill-2" href="#lab2">🤖 Lab 2 · Agentic</a>
  <a class="lab-pill pill-3" href="#lab3">📊 Lab 3 · ML</a>
  <div class="strip-title">Prepared by Keshar Mishra · IT Department Intern</div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# LAB 1 — PROMPT LAB
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="lab1"></div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="lab-section">', unsafe_allow_html=True)

    st.markdown("""
    <div class="lab-title-row">
      <div class="lab-num ln-1">1</div>
      <div class="lab-title">Prompt Engineering Lab</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="lab-obj">
    <b>Learning Objective:</b> Experience firsthand how the structure and specificity of a prompt
    changes AI output quality — turning casual typing into a reliable engineering skill for the shop floor.
    <br><span style="color:var(--muted);font-size:12px">⏱ 45 min &nbsp;·&nbsp; Groups of 3–4 &nbsp;·&nbsp; ChatGPT or Claude (browser)</span>
    </div>
    """, unsafe_allow_html=True)

    # ── FRAMEWORK ──
    st.markdown('<div class="sec-banner">📐 The R-T-C-F-C Framework — 5 Elements of a Strong Prompt</div>',
                unsafe_allow_html=True)
    st.markdown("""
    <div class="fw-grid">
      <div class="fw-card" style="border-top-color:#0F3D61">
        <div class="fw-letter" style="color:#0F3D61">R</div>
        <div class="fw-word" style="color:#0F3D61">Role</div>
        <div class="fw-desc">Who is the AI playing?</div>
        <div class="fw-eg">"You are a safety engineer at a steel plant."</div>
      </div>
      <div class="fw-card" style="border-top-color:#15517F">
        <div class="fw-letter" style="color:#15517F">T</div>
        <div class="fw-word" style="color:#15517F">Task</div>
        <div class="fw-desc">What exactly do you want?</div>
        <div class="fw-eg">"Write a 7-point blast furnace checklist."</div>
      </div>
      <div class="fw-card" style="border-top-color:#C5821A">
        <div class="fw-letter" style="color:#C5821A">C</div>
        <div class="fw-word" style="color:#C5821A">Context</div>
        <div class="fw-desc">Plant conditions, data, history</div>
        <div class="fw-eg">"Temp hit 85°C in Hot Strip Mill 2."</div>
      </div>
      <div class="fw-card" style="border-top-color:#1A7A45">
        <div class="fw-letter" style="color:#1A7A45">F</div>
        <div class="fw-word" style="color:#1A7A45">Format</div>
        <div class="fw-desc">How should the output look?</div>
        <div class="fw-eg">"Numbered list with ☐ checkboxes."</div>
      </div>
      <div class="fw-card" style="border-top-color:#B03A2E">
        <div class="fw-letter" style="color:#B03A2E">C</div>
        <div class="fw-word" style="color:#B03A2E">Constraint</div>
        <div class="fw-desc">Rules, limits, compliance</div>
        <div class="fw-eg">"Only use IS 3901 safety standard."</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── EXERCISE 1 ──
    st.markdown('<div class="sec-banner">Exercise 1 — Weak vs Strong Prompt &nbsp;<span style="font-weight:400;font-size:12px">(15 min)</span></div>',
                unsafe_allow_html=True)
    st.caption("Copy each prompt into ChatGPT or Claude. Paste the AI response in the boxes below each pair.")

    tab_a, tab_b = st.tabs(["Pair A · Safety Checklist", "Pair B · Maintenance Report"])

    with tab_a:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<span class="label-weak">❌ WEAK</span>', unsafe_allow_html=True)
            st.markdown('<div class="prompt-weak">Give me a safety checklist.</div>', unsafe_allow_html=True)
            st.text_area("Paste weak prompt output here", key="l1_a_weak", height=160,
                         placeholder="Copy this prompt into ChatGPT/Claude and paste the response...")
        with c2:
            st.markdown('<span class="label-strong">✅ STRONG</span>', unsafe_allow_html=True)
            st.markdown("""<div class="prompt-strong">
You are a safety officer at a steel plant's blast furnace unit [Role].
Create a 7-point pre-shift safety checklist for furnace operators [Task].
This is for a 6-hour shift on Hot Strip Mill 2 [Context].
Format as a numbered list with a ☐ checkbox before each item [Format].
Keep language simple — operators are not engineers [Constraint].
</div>""", unsafe_allow_html=True)
            st.text_area("Paste strong prompt output here", key="l1_a_strong", height=160,
                         placeholder="Copy this prompt into ChatGPT/Claude and paste the response...")
        if st.session_state.get("l1_a_weak") and st.session_state.get("l1_a_strong"):
            st.success("✅ Great comparison! Notice how specific context and format instructions change the output.")

    with tab_b:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<span class="label-weak">❌ WEAK</span>', unsafe_allow_html=True)
            st.markdown('<div class="prompt-weak">Write a maintenance report.</div>', unsafe_allow_html=True)
            st.text_area("Paste weak prompt output here", key="l1_b_weak", height=160,
                         placeholder="Paste the response here...")
        with c2:
            st.markdown('<span class="label-strong">✅ STRONG</span>', unsafe_allow_html=True)
            st.markdown("""<div class="prompt-strong">
Write a maintenance incident report [Task].
Situation: A main bearing in Hot Strip Mill showed abnormal
vibration (8.2 mm/s, threshold: 4.5 mm/s) for 3 days [Context].
Team replaced bearing on 28 May 2025. Downtime: 4 hours [Context].
Format: Date / Equipment / Observation / Action Taken /
Downtime / Next Inspection Date [Format].
</div>""", unsafe_allow_html=True)
            st.text_area("Paste strong prompt output here", key="l1_b_strong", height=160,
                         placeholder="Paste the response here...")

    # ── EXERCISE 2 ──
    st.markdown('<div class="sec-banner">Exercise 2 — Build Your Own Prompt &nbsp;<span style="font-weight:400;font-size:12px">(15 min)</span></div>',
                unsafe_allow_html=True)
    st.caption("Pick one scenario. Fill each element below. Your prompt assembles automatically.")

    scenarios = {
        "A — Predictive vs Reactive Maintenance": "Explain why predictive maintenance is better than reactive maintenance — for a furnace operator who has never heard of AI.",
        "B — PPE SOP": "Write a short SOP for safe PPE usage in the casting section.",
        "C — Incident Summary": "Summarise a conveyor belt motor trip at 2 AM (2 hrs downtime) into 3 bullet points for a plant manager.",
        "D — Training Questions": "Create 5 quiz questions about blast furnace hazards for a trainee exam.",
    }
    chosen = st.selectbox("Pick your scenario", list(scenarios.keys()), key="l1_scenario")
    st.info(f"**Your scenario:** {scenarios[chosen]}")

    c1, c2, c3, c4, c5 = st.columns(5)
    r = c1.text_input("Role", placeholder="You are a...", key="pr")
    t = c2.text_input("Task", placeholder="Write / Create...", key="pt")
    c = c3.text_input("Context", placeholder="Plant data...", key="pc")
    f = c4.text_input("Format", placeholder="Bullet list...", key="pf")
    con = c5.text_input("Constraint", placeholder="Only use...", key="pcon")

    parts = {"Role": r, "Task": t, "Context": c, "Format": f, "Constraint": con}
    if any(parts.values()):
        assembled = " ".join(f"[{k}: {v}]" for k, v in parts.items() if v)
        st.markdown(f'<div class="prompt-strong">{assembled}</div>', unsafe_allow_html=True)

    st.text_area("Paste AI output", key="l1_ex2_out", height=130,
                 placeholder="Paste the AI's response here...")
    st.text_area("What would you change to improve it?", key="l1_ex2_improve", height=70,
                 placeholder="e.g. Add more context about temperature thresholds...")

    # ── EXERCISE 3 ──
    st.markdown('<div class="sec-banner">Exercise 3 — Chain Prompting &nbsp;<span style="font-weight:400;font-size:12px">(15 min · run all 4 in the same chat window)</span></div>',
                unsafe_allow_html=True)
    st.caption("Run these prompts IN ORDER in a single chat session. Each builds on the previous answer.")

    chains = [
        ("Starter · Diagnose",  "#0F3D61",
         "You are a maintenance engineer at a steel plant. I have a blast furnace bearing showing 75% failure probability within 5 days. List 3 possible causes and what data I should check for each."),
        ("Step 2 · Action Plan", "#15517F",
         "Now assume the first cause is correct. Write a step-by-step action plan for the shift engineer to follow in the next 48 hours."),
        ("Step 3 · Write Email", "#C5821A",
         "Convert that action plan into a formal email I can send to my plant manager."),
        ("Step 4 · Shorten",    "#1A7A45",
         "Now make the email shorter — maximum 5 sentences. Subject line included."),
    ]
    for i, (title, color, prompt_text) in enumerate(chains):
        with st.expander(f"Prompt {i+1}: {title}"):
            st.markdown(f'<div class="prompt-chain">{prompt_text}</div>', unsafe_allow_html=True)
            st.text_area(f"Paste AI output for Step {i+1}", key=f"l1_ch_{i}", height=110,
                         placeholder=f"Paste the response for Step {i+1} here...")

    # ── DEBRIEF ──
    st.markdown('<div class="sec-banner sec-banner-amber">💬 Debrief Questions</div>', unsafe_allow_html=True)
    debrief_qs = [
        "What's the plant risk if an operator gives vague context during a safety-critical task?",
        "How is writing a structured prompt similar to writing a good job card or work order?",
        "In chain prompting — what changed between Step 3 and Step 4?",
        "Which R-T-C-F-C element had the biggest impact on output quality?",
    ]
    d_cols = st.columns(2)
    for i, q in enumerate(debrief_qs):
        with d_cols[i % 2]:
            st.markdown(f'<div class="debrief-q">Q{i+1}. {q}</div>', unsafe_allow_html=True)
            st.text_area("", key=f"l1_db_{i}", height=75, label_visibility="collapsed",
                         placeholder="Your answer...")

    if st.button("✅ Mark Lab 1 Complete", type="primary", key="done1"):
        st.session_state.completed.add("Lab 1")
        st.balloons()
        st.success("Lab 1 complete! Scroll down to Lab 2.")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr style='margin:0;border-color:#E3E7EC'>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# LAB 2 — AGENTIC SOLUTION LAB
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="lab2"></div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="lab-section">', unsafe_allow_html=True)

    st.markdown("""
    <div class="lab-title-row">
      <div class="lab-num ln-2">2</div>
      <div class="lab-title">Agentic Solution Lab</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="lab-obj lab-obj-amber">
    <b>Learning Objective:</b> Simulate how an agentic AI platform receives a goal, plans steps,
    queries databases, and gives a recommendation autonomously — using the <b>ReAct (Reasoning + Acting)</b> loop.
    <br><span style="color:var(--muted);font-size:12px">⏱ 45 min &nbsp;·&nbsp; Groups of 4–5 &nbsp;·&nbsp; No devices required — role-play simulation</span>
    </div>
    """, unsafe_allow_html=True)

    # ── ROLES ──
    st.markdown('<div class="sec-banner">👥 Step 1 — Assign Roles (one card per group member)</div>',
                unsafe_allow_html=True)
    st.markdown("""
    <div class="role-grid">
      <div class="role-card" style="border-left-color:#0F3D61">
        <div class="role-title" style="color:#0F3D61">USER</div>
        <div class="role-person">Plant Shift Manager</div>
        <div class="role-duty">Read the scenario aloud. You trigger the agent.</div>
      </div>
      <div class="role-card" style="border-left-color:#15517F">
        <div class="role-title" style="color:#15517F">AGENT BRAIN</div>
        <div class="role-person">Core AI Orchestrator</div>
        <div class="role-duty">Follow the 7-step script. Speak each step aloud to the group.</div>
      </div>
      <div class="role-card" style="border-left-color:#C5821A">
        <div class="role-title" style="color:#C5821A">DATA CALLER 1</div>
        <div class="role-person">Sensor Database</div>
        <div class="role-duty">Read your data card ONLY when Agent Brain calls you.</div>
      </div>
      <div class="role-card" style="border-left-color:#1A7A45">
        <div class="role-title" style="color:#1A7A45">DATA CALLER 2</div>
        <div class="role-person">Maintenance Log</div>
        <div class="role-duty">Read your data card ONLY when called by Agent Brain.</div>
      </div>
      <div class="role-card" style="border-left-color:#B03A2E">
        <div class="role-title" style="color:#B03A2E">DATA CALLER 3</div>
        <div class="role-person">Spare Parts Inventory</div>
        <div class="role-duty">Read your data card ONLY when called by Agent Brain.</div>
      </div>
      <div class="role-card" style="border-left-color:#3A4A5A">
        <div class="role-title" style="color:#3A4A5A">HUMAN APPROVER</div>
        <div class="role-person">Plant Manager</div>
        <div class="role-duty">Receive the final recommendation. Approve or override.</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── SCENARIO ──
    st.markdown('<div class="sec-banner">🚨 Step 2 — The Scenario (USER reads aloud)</div>',
                unsafe_allow_html=True)
    st.markdown("""
    <div class="scenario-alert">
      <div class="sa-head">⏰ 11:15 AM — Blast Furnace 02 · YELLOW ALERT</div>
      <div class="sa-body">
        The Predictive Maintenance dashboard registers a <b>YELLOW ALERT</b> on Blast Furnace-02.<br>
        Main Bearing <b>MB-7</b> shows a <b>75% probability of failure within 5 days</b>.<br>
        I need the AI agent to investigate all available data and give me an optimal recommendation.
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── DATA CARDS ──
    st.markdown('<div class="sec-banner">🃏 Step 3 — Data Cards (open ONLY when called by Agent Brain)</div>',
                unsafe_allow_html=True)
    dc1, dc2, dc3 = st.columns(3)
    with dc1:
        with st.expander("📡 DATA CARD 1 — Sensor Database"):
            st.markdown("""
            <div class="data-card dc-blue">
            <b>MB-7 Vibration:</b> 8.6 mm/s &nbsp;<span class="warn">(Threshold: 4.5 mm/s ⚠️)</span><br>
            <b>MB-7 Temperature:</b> 94°C &nbsp;<span class="warn">(Normal: &lt;75°C ⚠️)</span><br>
            <b>Trend:</b> Rising monotonically for <b>6 consecutive days</b><br>
            <b>Last normal reading:</b> 5 days ago
            </div>""", unsafe_allow_html=True)
    with dc2:
        with st.expander("🔧 DATA CARD 2 — Maintenance Log"):
            st.markdown("""
            <div class="data-card dc-green">
            <b>Last replaced:</b> 14 months ago &nbsp;<span class="warn">(Cycle: 12 months ⚠️)</span><br>
            <b>Last lubrication:</b> 3 weeks ago &nbsp;<span class="warn">(Due: every 2 weeks ⚠️)</span><br>
            <b>Previous failure:</b> March 2023 → 18 hrs downtime<br>
            <b>Emergency repair cost:</b> ₹8.4 lakh
            </div>""", unsafe_allow_html=True)
    with dc3:
        with st.expander("📦 DATA CARD 3 — Spare Parts Inventory"):
            st.markdown("""
            <div class="data-card dc-amber">
            <b>SKF-22230 in stock:</b> 2 units ✅<br>
            <b>Replacement time:</b> 6 hours<br>
            <b>Next planned shutdown:</b> 8 days &nbsp;<span class="warn">(Too late ⚠️)</span><br>
            <b>Active order at risk:</b> ₹4.2 crore (due in 3 days)
            </div>""", unsafe_allow_html=True)

    # ── AGENT BRAIN SCRIPT ──
    st.markdown('<div class="sec-banner">🧠 Step 4 — Agent Brain Script (speak each step aloud)</div>',
                unsafe_allow_html=True)
    steps = [
        ("#0F3D61", "Acknowledge Goal",
         '"Goal received. MB-7 bearing has a failure alert. I will investigate and provide an optimised recommendation."'),
        ("#15517F", "State Plan",
         '"I need: (a) current sensor readings, (b) maintenance history, (c) spare parts availability. Then I calculate risk."'),
        ("#C5821A", "Call Sensor DB",
         '"DATA CALLER 1 — give me MB-7 current readings and trend."'),
        ("#1A7A45", "Call Maintenance Log",
         '"DATA CALLER 2 — give me MB-7 replacement and lubrication history."'),
        ("#B03A2E", "Call Inventory",
         '"DATA CALLER 3 — do we have the compatible bearing in stock? How long to replace?"'),
        ("#C5821A", "Synthesise",
         '"Bearing overdue, running at 94°C and 8.6 mm/s, both rising. Stock available. Emergency cost last time: ₹8.4 lakh. Active order: ₹4.2 crore."'),
        ("#1A7A45", "Recommendation → Human Approver",
         '"Replace MB-7 after the current order completes in 72 hours. Increase lubrication monitoring every 12 hours as interim. Estimated cost saving vs emergency failure: ₹6+ lakh."'),
    ]
    for i, (color, label, script) in enumerate(steps):
        st.markdown(f"""
        <div class="agent-step">
          <div class="agent-num" style="background:{color}">{i+1}</div>
          <div>
            <div class="agent-label">{label}</div>
            <div class="agent-script">{script}</div>
          </div>
        </div>""", unsafe_allow_html=True)

    # ── RECORD NOTES ──
    st.markdown('<div class="sec-banner">📝 Step 5 — Agent Brain Records Data</div>',
                unsafe_allow_html=True)
    n1, n2, n3 = st.columns(3)
    with n1:
        st.session_state.l2_notes["sensors"] = st.text_area(
            "From DATA CARD 1 · Sensors", height=100,
            value=st.session_state.l2_notes["sensors"],
            placeholder="Note key sensor readings...")
    with n2:
        st.session_state.l2_notes["maintenance"] = st.text_area(
            "From DATA CARD 2 · Maintenance", height=100,
            value=st.session_state.l2_notes["maintenance"],
            placeholder="Note the maintenance history...")
    with n3:
        st.session_state.l2_notes["inventory"] = st.text_area(
            "From DATA CARD 3 · Inventory", height=100,
            value=st.session_state.l2_notes["inventory"],
            placeholder="Note parts availability...")

    # ── HUMAN APPROVER ──
    st.markdown('<div class="sec-banner">👔 Step 6 — Human Approver Decision</div>',
                unsafe_allow_html=True)
    st.radio("Do you approve the Agent Brain's recommendation?",
             ["✅ Approve — Replace after 72 hours + increase lubrication monitoring",
              "🔄 Modify — Stop furnace immediately, don't risk the order",
              "❌ Override — Continue operations, re-evaluate in 2 days"],
             key="l2_decision")
    st.text_area("Justify your decision:", key="l2_justify", height=80,
                 placeholder="Why did you approve / modify / override?")

    # ── VULNERABILITY ──
    st.markdown('<div class="sec-banner">🔍 System Vulnerability Analysis</div>',
                unsafe_allow_html=True)
    v1, v2 = st.columns(2)
    with v1:
        st.text_area("What breaks if DATA CARD 3 said '0 units in stock'?",
                     key="l2_vuln1", height=90,
                     placeholder="How would the recommendation change?")
    with v2:
        st.text_area("This 7-step sequence runs in under 30 seconds on a real AI platform. How does that change plant operations?",
                     key="l2_vuln2", height=90,
                     placeholder="Think about night shifts, weekends, emergencies...")

    # ── DEBRIEF ──
    st.markdown('<div class="sec-banner sec-banner-amber">💬 Debrief Questions</div>',
                unsafe_allow_html=True)
    l2_qs = [
        "Which data point had the biggest influence on the Agent Brain's recommendation?",
        "Can the Agent Brain ever be wrong? What is the human's role in this loop?",
        "Name one real-world scenario where this exact agentic loop would run automatically.",
    ]
    d2_cols = st.columns(3)
    for i, q in enumerate(l2_qs):
        with d2_cols[i]:
            st.markdown(f'<div class="debrief-q">Q{i+1}. {q}</div>', unsafe_allow_html=True)
            st.text_area("", key=f"l2_db_{i}", height=80, label_visibility="collapsed",
                         placeholder="Your answer...")

    if st.button("✅ Mark Lab 2 Complete", type="primary", key="done2"):
        st.session_state.completed.add("Lab 2")
        st.balloons()
        st.success("Lab 2 complete! Scroll down to Lab 3.")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr style='margin:0;border-color:#E3E7EC'>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# LAB 3 — ML LAB
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="lab3"></div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="lab-section">', unsafe_allow_html=True)

    st.markdown("""
    <div class="lab-title-row">
      <div class="lab-num ln-3">3</div>
      <div class="lab-title">ML Lab — Train a Real AI Model</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="lab-obj lab-obj-green">
    <b>Learning Objective:</b> Train a real neural network image classifier in your browser —
    experiencing training data, confidence scores, and live inference firsthand.
    The same mechanics power industrial computer-vision safety systems at scale.
    <br><span style="color:var(--muted);font-size:12px">⏱ 45 min &nbsp;·&nbsp; Groups of 2–3 &nbsp;·&nbsp;
    <a href="https://teachablemachine.withgoogle.com" target="_blank">teachablemachine.withgoogle.com</a> + webcam</span>
    </div>
    """, unsafe_allow_html=True)

    # ── STEPS ──
    st.markdown('<div class="sec-banner sec-banner-green">🚀 Step-by-Step Instructions</div>',
                unsafe_allow_html=True)

    ml_steps = [
        ("Open Teachable Machine",
         'Go to <a href="https://teachablemachine.withgoogle.com" target="_blank"><b>teachablemachine.withgoogle.com</b></a> → <b>Get Started</b> → <b>Image Project</b> → <b>Standard Image Model</b>'),
        ("Set up your two classes",
         "Rename <b>Class 1</b> → <code>PPE ON</code> &nbsp; · &nbsp; Rename <b>Class 2</b> → <code>PPE OFF</code>. These are the two categories the model will learn to distinguish."),
        ("Collect PPE ON images",
         "Put on a safety helmet (or any hat). Click <b>Webcam → Hold to Record</b>. Vary head angle slightly. Collect <b>60–80 frames</b>. Tip: move left, right, tilt — variety improves accuracy."),
        ("Collect PPE OFF images",
         "Remove the helmet. <b>Same background and lighting as Class 1.</b> Collect <b>60–80 frames</b>. Match the count from Class 1."),
        ("Train the model",
         "Click the blue <b>Train Model</b> button. Wait 30–60 seconds. <b>Do NOT switch tabs during training.</b> A real gradient descent algorithm is adjusting neural network weights on your pixel data."),
        ("Test with live inference",
         "The preview window opens automatically. Try each condition in the table below. Record what the model predicts and its confidence score."),
    ]
    for i, (label, body) in enumerate(ml_steps):
        st.markdown(f"""
        <div class="ml-step">
          <div class="ml-num">{i+1}</div>
          <div>
            <div class="ml-label">{label}</div>
            <div class="ml-body">{body}</div>
          </div>
        </div>""", unsafe_allow_html=True)

    confirm_open = st.checkbox("✅ I have opened Teachable Machine and named my two classes (PPE ON / PPE OFF)")
    images_done  = st.checkbox("✅ I have collected 60–80 images for BOTH classes")
    training_done = st.checkbox("✅ Model training is complete — the preview window is active")

    # ── OBSERVATION TABLE ──
    if training_done:
        st.markdown('<div class="sec-banner sec-banner-green">🧪 Observation Table — Record Your Results</div>',
                    unsafe_allow_html=True)
        st.caption("Fill in each row as you test. Be honest — include failures. The accuracy score below auto-calculates.")

        test_conditions = [
            "Helmet on, facing forward",
            "Helmet on, sideways",
            "No helmet, forward",
            "No helmet, dim lighting",
            "Helmet tilted / partial",
            "Different person with helmet",
        ]
        hc = st.columns([3, 2, 2, 2])
        hc[0].markdown("**Test Condition**")
        hc[1].markdown("**Predicted Class**")
        hc[2].markdown("**Confidence %**")
        hc[3].markdown("**Correct? (Y/N)**")
        st.markdown("<hr style='margin:4px 0 8px'>", unsafe_allow_html=True)

        for cond in test_conditions:
            rc = st.columns([3, 2, 2, 2])
            with rc[0]:
                st.markdown(f"<div style='padding:6px 0;font-size:13px'>{cond}</div>",
                            unsafe_allow_html=True)
            pred    = rc[1].selectbox("", ["", "PPE ON", "PPE OFF"],
                                      key=f"pred_{cond}", label_visibility="collapsed")
            conf    = rc[2].number_input("", 0, 100,
                                         key=f"conf_{cond}", label_visibility="collapsed")
            correct = rc[3].selectbox("", ["", "Y", "N"],
                                      key=f"corr_{cond}", label_visibility="collapsed")
            st.session_state.l3_obs[cond] = {"pred": pred, "conf": conf, "correct": correct}

        # Auto-calculate
        filled = [v for v in st.session_state.l3_obs.values() if v["correct"] in ["Y", "N"]]
        if filled:
            correct_count = sum(1 for v in filled if v["correct"] == "Y")
            accuracy      = round(correct_count / len(filled) * 100)
            conf_avg      = round(sum(v["conf"] for v in filled) / len(filled))
            acc_color     = "#1A7A45" if accuracy >= 80 else "#C5821A" if accuracy >= 60 else "#B03A2E"
            st.markdown(f"""
            <div class="metric-row" style="margin-top:16px">
              <div class="metric-box">
                <div class="metric-val" style="color:{acc_color}">{accuracy}%</div>
                <div class="metric-lbl">Your model accuracy</div>
              </div>
              <div class="metric-box">
                <div class="metric-val" style="color:#0F3D61">{correct_count}/{len(filled)}</div>
                <div class="metric-lbl">Correct predictions</div>
              </div>
              <div class="metric-box">
                <div class="metric-val" style="color:#15517F">{conf_avg}%</div>
                <div class="metric-lbl">Avg confidence</div>
              </div>
            </div>""", unsafe_allow_html=True)
            if accuracy < 70:
                st.warning("⚠️ Below 70%. Try: more training images, consistent lighting, more varied angles.")
            elif accuracy < 90:
                st.info("👍 Good. Reaching industrial deployment level (>97%) requires millions of diverse frames.")
            else:
                st.success("🎉 Excellent for a lab model!")

    # ── REFLECTION ──
    st.markdown('<div class="sec-banner sec-banner-green">✍️ Reflection</div>',
                unsafe_allow_html=True)
    r1, r2 = st.columns(2)
    with r1:
        st.text_area("What did you notice about accuracy when lighting or angle changed?",
                     key="l3_note", height=90, placeholder="Write your observation...")
    with r2:
        st.text_area("What would you do to improve this model?",
                     key="l3_improve", height=90,
                     placeholder="More images? A 3rd class? Better lighting?")

    # ── CHALLENGE EXTENSIONS ──
    st.markdown('<div class="sec-banner sec-banner-green">🏆 Challenge Extensions (if time allows)</div>',
                unsafe_allow_html=True)
    ch1, ch2 = st.columns(2)
    challenges = [
        ("3-Class Test",       "#15517F", "Add PARTIAL PPE (helmet on, no vest). Retrain. Does accuracy drop?"),
        ("Spoofing Attack",    "#B03A2E", "Hold a phone showing a photo of a helmet. Does the model get fooled?"),
        ("Data Quantity Test", "#C5821A", "Retrain with only 20 images. Compare accuracy vs 80 images."),
        ("Lighting Test",      "#1A7A45", "Train in bright light, test in dim. Record the confidence score drop."),
    ]
    for i, (title, color, desc) in enumerate(challenges):
        col = ch1 if i % 2 == 0 else ch2
        with col:
            st.checkbox(f"✅ {title}", key=f"l3_ch_{i}")
            st.markdown(f"""
            <div style="background:white;border-radius:8px;padding:10px 14px;
            border-left:3px solid {color};margin-bottom:10px;font-size:12.5px;color:#444">
            {desc}
            </div>""", unsafe_allow_html=True)

    # ── SCALE COMPARISON ──
    st.markdown('<div class="sec-banner sec-banner-green">🔗 Your Lab vs Industrial Scale</div>',
                unsafe_allow_html=True)
    scale = [
        ("You captured 80 webcam images",         "Industrial plants stream millions of CCTV frames daily"),
        ("You manually labelled 2 classes",        "Uses annotation pipelines + semi-supervised labelling"),
        ("Model trained in 60 seconds locally",    "Runs on hundreds of cloud TPUs"),
        ("Tested in one room, one light setting",  "Operates across furnaces, dust, glare, extreme heat"),
        ("Your accuracy: ~85%",                    "Industrial deployment targets >97% before go-live"),
    ]
    for you, ind in scale:
        st.markdown(f"""
        <div class="scale-row">
          <div class="scale-you">🧑‍💻 {you}</div>
          <div class="scale-ind">🏭 {ind}</div>
        </div>""", unsafe_allow_html=True)

    # ── DEBRIEF ──
    st.markdown('<div class="sec-banner sec-banner-amber">💬 Debrief Questions</div>',
                unsafe_allow_html=True)
    l3_qs = [
        "Why did confidence drop when lighting changed? What does this mean for real deployment?",
        "If this model had 15% error at a real factory gate, what are the safety consequences?",
        "What is the human's role after a model is deployed?",
    ]
    d3c = st.columns(3)
    for i, q in enumerate(l3_qs):
        with d3c[i]:
            st.markdown(f'<div class="debrief-q">Q{i+1}. {q}</div>', unsafe_allow_html=True)
            st.text_area("", key=f"l3_db_{i}", height=80, label_visibility="collapsed",
                         placeholder="Your answer...")

    if st.button("✅ Mark Lab 3 Complete", type="primary", key="done3"):
        st.session_state.completed.add("Lab 3")
        st.balloons()
        st.success("🎉 All labs complete!")

    # ── COMPLETION BANNER ──
    if len(st.session_state.completed) == 3:
        st.markdown("""
        <div class="complete-banner">
          <div class="cb-icon">🏆</div>
          <div class="cb-title">All 3 Labs Complete!</div>
          <div class="cb-sub">
            You have experienced Prompt Engineering, Agentic AI simulation,<br>
            and real ML model training — the same technologies powering<br>
            modern industrial AI agent platforms at scale.
          </div>
        </div>""", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
