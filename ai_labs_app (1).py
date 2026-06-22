import streamlit as st
import time
import json
import random

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Labs — L&D Division",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="collapsed" # Hide sidebar by default to maximize main UI space
)

# ── GLOBAL CSS DESIGN SYSTEM ──────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --c-primary:    #0F3D61;   /* deep corporate navy */
    --c-primary-2:  #15517F;
    --c-accent:     #C5821A;   /* amber accent */
    --c-success:    #1E8449;   
    --c-error:      #B03A2E;   
    --c-ink:        #1B2430;   
    --c-muted:      #6B7785;   
    --c-line:       #E3E7EC;   
    --c-surface:    #FFFFFF;
    --c-bg:         #F4F6F9;
    --radius:       10px;
}

html, body, [class*="css"] { 
    font-family: 'Inter', sans-serif; 
    color: var(--c-ink);
}

.main { 
    background-color: var(--c-bg); 
}

/* Master Header Banner */
.master-header {
    background: linear-gradient(135deg, #0F3D61 0%, #1A5276 100%);
    padding: 24px 32px;
    border-radius: var(--radius);
    color: #FFFFFF !important;
    margin-bottom: 24px;
    box-shadow: 0 4px 12px rgba(15, 61, 97, 0.15);
}
.master-header h1 { color: #FFFFFF !important; font-size: 26px; font-weight: 700; margin: 0; }
.master-header p { color: #D4E6F1 !important; font-size: 14px; margin: 4px 0 0 0; opacity: 0.9; }

/* Structural Content Banners */
.section-banner {
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--c-muted);
    border-bottom: 2px solid var(--c-line);
    padding-bottom: 6px;
    margin: 20px 0 14px 0;
}

/* Unified Card System */
.ui-card {
    background: var(--c-surface);
    border: 1px solid var(--c-line);
    border-radius: var(--radius);
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.02);
}
.ui-card-title {
    font-size: 16px;
    font-weight: 600;
    color: var(--c-primary);
    margin-bottom: 6px;
}
.ui-card-desc {
    font-size: 13px;
    color: var(--c-muted);
    line-height: 1.5;
}

/* Code Output Blocks */
.terminal-block {
    background: #0F172A;
    color: #F8FAFC;
    font-family: 'Courier New', Courier, monospace;
    font-size: 13px;
    padding: 16px;
    border-radius: var(--radius);
    line-height: 1.6;
    margin: 12px 0;
}

/* Style the top navigation tabs to look premium */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background-color: transparent;
}
.stTabs [data-baseweb="tab"] {
    background-color: #EAECEE;
    border-radius: 6px 6px 0 0;
    padding: 10px 20px;
    font-weight: 600;
    font-size: 14px;
    color: var(--c-muted);
}
.stTabs [aria-selected="true"] {
    background-color: var(--c-primary) !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ── INITIALIZE SESSION STATES ────────────────────────────────────────────────
if "completed_labs" not in st.session_state:
    st.session_state.completed_labs = set()
if "current_step_l2" not in st.session_state:
    st.session_state.current_step_l2 = 0
if "l2_logs" not in st.session_state:
    st.session_state.l2_logs = []

# ── MASTER UI BANNER (ALWAYS VISIBLE AT TOP) ──────────────────────────────────
st.markdown("""
<div class="master-header">
    <h1>AI Engineering Training Portal</h1>
    <p>Learning & Development Division — Unified Laboratory Workspace</p>
</div>
""", unsafe_allow_html=True)

# ── CENTRAL UNIFIED UI TAB SYSTEM ────────────────────────────────────────────
tab_overview, tab_lab1, tab_lab2, tab_lab3 = st.tabs([
    "📊 Hub Overview", 
    "✍️ Lab 1: Prompt Sandbox", 
    "🤖 Lab 2: Agentic Simulation", 
    "📈 Lab 3: Predictive Inference"
])

# ── TAB: OVERVIEW ────────────────────────────────────────────────────────────
with tab_overview:
    st.markdown('<div class="section-banner">Program Trainee Metric Overview</div>', unsafe_allow_html=True)
    
    # Live Trackers
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Total Completed Modules", f"{len(st.session_state.completed_labs)} / 3")
    with m2:
        progress_val = len(st.session_state.completed_labs) / 3
        st.metric("Program Progress Rate", f"{int(progress_val * 100)}%")
    with m3:
        st.metric("Workspace Status", "Active Runtime")
        
    st.markdown('<div class="section-banner">Unified Core Syllabi</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="ui-card">
            <div class="ui-card-title">Lab 1: Prompt Validation</div>
            <div class="ui-card-desc">Evaluate engineering inputs against structural validation controls to optimize underlying model responses.</div>
            <div style="margin-top:12px; font-size:11px; font-weight:600; color:{'#1E8449' if 'Lab 1' in st.session_state.completed_labs else '#6B7785'};">
                {'● COMPLETED' if 'Lab 1' in st.session_state.completed_labs else '○ PENDING REVIEW'}
            </div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="ui-card">
            <div class="ui-card-title">Lab 2: Agentic Framework</div>
            <div class="ui-card-desc">Trace automated multi-database orchestration routines evaluating complex industrial downtime risks.</div>
            <div style="margin-top:12px; font-size:11px; font-weight:600; color:{'#1E8449' if 'Lab 2' in st.session_state.completed_labs else '#6B7785'};">
                {'● COMPLETED' if 'Lab 2' in st.session_state.completed_labs else '○ PENDING REVIEW'}
            </div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="ui-card">
            <div class="ui-card-title">Lab 3: Predictive Inference</div>
            <div class="ui-card-desc">Map physical sensor boundaries against real-time predictive degradation safety curves.</div>
            <div style="margin-top:12px; font-size:11px; font-weight:600; color:{'#1E8449' if 'Lab 3' in st.session_state.completed_labs else '#6B7785'};">
                {'● COMPLETED' if 'Lab 3' in st.session_state.completed_labs else '○ PENDING REVIEW'}
            </div>
        </div>
        """, unsafe_allow_html=True)

# ── TAB: LAB 1 ───────────────────────────────────────────────────────────────
with tab_lab1:
    st.markdown('<div class="section-banner">Baseline Unstructured Entry Control</div>', unsafe_allow_html=True)
    col_l1, col_r1 = st.columns(2)
    
    with col_l1:
        st.caption("Standard operational query omitting context rules:")
        st.code("Write a report on a broken pump at the industrial plant.")
        st.markdown("""
        <div class="terminal-block" style="background:#ECEFF1; color:#37474F;">
        <strong>System Output Evaluation:</strong><br>
        The industrial pump is currently reported as non-functional. Maintenance crews should investigate the site to resolve potential issues.
        <br><br>
        <span style="color:#B03A2E; font-size:11px; font-weight:700;">⚠️ FAILURE: NO TECHNICAL METRICS DETECTED</span>
        </div>
        """, unsafe_allow_html=True)

    with col_r1:
        st.caption("Assemble prompt using R-T-C-F-C constraints (Include keywords: 'safety', 'vibration', 'checklist'):")
        trainee_input = st.text_area("Construct Prompt Input Here:", height=108, key="l1_input_box")
        
        if st.button("Execute Validation Scan", key="btn_l1"):
            if not trainee_input.strip():
                st.warning("Please provide input text to scan.")
            else:
                has_safety = any(w in trainee_input.lower() for w in ["safety", "hazard", "lockout"])
                has_vibration = any(w in trainee_input.lower() for w in ["vibration", "hz", "mm/s"])
                has_checklist = any(w in trainee_input.lower() for w in ["checklist", "format", "step"])
                score = sum([has_safety, has_vibration, has_checklist])
                
                if score == 3:
                    st.markdown("""
                    <div class="terminal-block">
                    [SYSTEM INFERENCE VERIFIED: PRODUCTION READY TASK PROTOCOL]<br>
                    1. INITIAL HAZARD MITIGATION: Trigger LOTO protocols.<br>
                    2. TELEMETRY PROFILE: Logged vibration anomaly at peak 7.4 mm/s.<br>
                    3. CHECKLIST: Flush chamber housing and torque anchor bolts.
                    </div>
                    """, unsafe_allow_html=True)
                    st.success("Target validation standards met successfully.")
                else:
                    st.markdown("""
                    <div class="terminal-block" style="background:#B03A2E; color:#FDEDEC;">
                    [SYSTEM INFERENCE AUDIT FAILURE: CONSTRAINTS MISSING] ({}/3) parameters found.
                    </div>
                    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-banner">Module Context Evaluation Summary</div>', unsafe_allow_html=True)
    st.text_area("Record insights regarding prompt constraints here:", height=65, key="notes_l1")
    if st.button("Commit Lab 1 Progress", type="primary"):
        st.session_state.completed_labs.add("Lab 1")
        st.toast("Lab 1 Complete!")

# ── TAB: LAB 2 ───────────────────────────────────────────────────────────────
with tab_lab2:
    st.markdown('<div class="section-banner">Complex System Incident Scenario Context</div>', unsafe_allow_html=True)
    st.markdown("Evaluating autonomous orchestration layers tracing system warning flag anomalies on **Heavy Machinery Unit #4**.")
    
    steps = [
        {"title": "Initialize Execution Loop", "log": "THOUGHT: Analyzing Unit #4 telemetry alarms. Querying database metrics."},
        {"title": "Execute System Cross-Checks", "log": "ACTION: Querying Sensor DB (Vibration: 8.2mm/s) -> Querying Storage Inventory (Replacement parts available)."},
        {"title": "Generate Resolution Framework", "log": "THOUGHT: Mechanical risk high. Recommending immediate controlled shutdown sequence."}
    ]
    
    cl1, cl2 = st.columns(2)
    with cl1:
        if st.button("Advance Execution Step", key="btn_l2"):
            if st.session_state.current_step_l2 < len(steps):
                st.session_state.l2_logs.append(steps[st.session_state.current_step_l2])
                st.session_state.current_step_l2 += 1
        if st.button("Reset Simulation Link", key="btn_reset_l2"):
            st.session_state.current_step_l2 = 0
            st.session_state.l2_logs = []
            st.rerun()
            
        for idx, item in enumerate(st.session_state.l2_logs):
            st.markdown(f"**Step {idx+1}: {item['title']}**")
            st.markdown(f'<div class="terminal-block">{item["log"]}</div>', unsafe_allow_html=True)
            
    with cl2:
        try:
            import graphviz
            dot = graphviz.Digraph()
            dot.attr(bgcolor='#F4F6F9', color='#6B7785')
            dot.attr('node', shape='box', style='filled,rounded', color='#E3E7EC', fillcolor='#FFFFFF')
            dot.node('A', 'Real-time Alarm Trigger')
            if st.session_state.current_step_l2 >= 1: dot.node('B', 'Cross-System API Polls'); dot.edge('A', 'B')
            if st.session_state.current_step_l2 >= 3: dot.node('C', 'Action Recommended'); dot.edge('B', 'C')
            st.graphviz_chart(dot, use_container_width=True)
        except:
            st.info("System mapping logic active.")

    st.markdown('<div class="section-banner">Module Context Evaluation Summary</div>', unsafe_allow_html=True)
    st.text_area("Record insights regarding agentic logic loops here:", height=65, key="notes_l2")
    if st.button("Commit Lab 2 Progress", type="primary"):
        st.session_state.completed_labs.add("Lab 2")
        st.toast("Lab 2 Complete!")

# ── TAB: LAB 3 ───────────────────────────────────────────────────────────────
with tab_lab3:
    st.markdown('<div class="section-banner">Continuous Sensor Parameter Controls & Inference Monitoring</div>', unsafe_allow_html=True)
    cl3_1, cl3_2 = st.columns(2)
    
    with cl3_1:
        vibration = st.slider("Vibration Intensity (mm/s)", 1.0, 15.0, 4.2)
        temperature = st.slider("Thermal Core Temp (°C)", 40, 140, 75)
        runtime = st.slider("Continuous Operational Hours", 0, 200, 48)
        
    with cl3_2:
        risk = min(int((vibration * 4) + ((temperature - 40) * 0.4) + (runtime * 0.1)), 100)
        st.metric("Calculated Boundary Risk Score", f"{risk}%")
        
        color = "#1E8449" if risk < 45 else ("#C5821A" if risk < 75 else "#B03A2E")
        status_lbl = "STABLE OPERATING WINDOW" if risk < 45 else ("ELEVATED RISK - MONITOR" if risk < 75 else "CRITICAL RISK - ACTION REQUIRED")
        st.markdown(f"""
        <div style="background:{color}; color:white; padding:12px; border-radius:6px; font-weight:700; text-align:center;">
            {status_lbl}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-banner">Module Context Evaluation Summary</div>', unsafe_allow_html=True)
    st.text_area("Record insights regarding predictive streams here:", height=65, key="notes_l3")
    if st.button("Commit Lab 3 Progress", type="primary"):
        st.session_state.completed_labs.add("Lab 3")
        st.toast("Lab 3 Complete!")

# ── GLOBAL PROGRAM COMPLETION BANNER ─────────────────────────────────────────
if len(st.session_state.completed_labs) == 3:
    st.markdown("""
    <div style="background:var(--c-primary); color:white; border-radius:var(--radius); padding:20px; text-align:center; margin-top:24px;">
        <div style="font-size:18px; font-weight:700;">🏆 All Training Modules Successfully Committed</div>
        <div style="font-size:13px; opacity:0.85; margin-top:2px;">Evaluation records show alignment with corporate L&D division integration criteria.</div>
    </div>
    """, unsafe_allow_html=True)
