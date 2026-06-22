import streamlit as st
import time
import json
import random

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Labs — L&D Division",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="collapsed" # Hides the sidebar automatically to maximize screen space
)

# ── GLOBAL CSS DESIGN SYSTEM (MATURE ENTERPRISE STYLING) ─────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* Design Tokens */
:root {
    --c-primary:    #0F3D61;   /* deep corporate navy — primary brand */
    --c-primary-2:  #15517F;   /* lighter navy for gradients/hover */
    --c-accent:     #C5821A;   /* single muted amber accent */
    --c-success:    #1E8449;   /* success green */
    --c-error:      #B03A2E;   /* failure red */
    --c-ink:        #1B2430;   /* body dark text */
    --c-muted:      #6B7785;   /* secondary gray text */
    --c-line:       #E3E7EC;   /* clean borders */
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
    background: linear-gradient(135deg, var(--c-primary) 0%, var(--c-primary-2) 100%);
    padding: 24px 32px;
    border-radius: var(--radius);
    color: #FFFFFF !important;
    margin-bottom: 24px;
    box-shadow: 0 4px 12px rgba(15, 61, 97, 0.12);
}
.master-header h1 { color: #FFFFFF !important; font-size: 26px; font-weight: 700; margin: 0; letter-spacing: -0.02em; }
.master-header p { color: #D4E6F1 !important; font-size: 13px; margin: 6px 0 0 0; opacity: 0.85; }

/* Section Typographic Banners */
.section-banner {
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--c-muted);
    border-bottom: 2px solid var(--c-line);
    padding-bottom: 6px;
    margin: 24px 0 16px 0;
}

/* Layout Content Cards */
.ui-card {
    background: var(--c-surface);
    border: 1px solid var(--c-line);
    border-radius: var(--radius);
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
}
.ui-card-title {
    font-size: 15px;
    font-weight: 600;
    color: var(--c-primary);
    margin-bottom: 4px;
}
.ui-card-desc {
    font-size: 13px;
    color: var(--c-muted);
    line-height: 1.5;
}

/* Code & Log Output Terminal Containers */
.terminal-block {
    background: #0F172A;
    color: #F8FAFC;
    font-family: 'Courier New', Courier, monospace;
    font-size: 13px;
    padding: 16px;
    border-radius: var(--radius);
    line-height: 1.6;
    margin: 12px 0;
    border: 1px solid #1E293B;
}

/* Premium Top-Tab Style Overrides */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background-color: transparent;
}
.stTabs [data-baseweb="tab"] {
    background-color: #EAECEE;
    border-radius: 6px 6px 0 0;
    padding: 10px 24px;
    font-weight: 600;
    font-size: 13px;
    color: var(--c-muted);
    border: none !important;
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

# ── MASTER UI HEADER (ALWAYS ANCHORED AT TOP) ────────────────────────────────
st.markdown("""
<div class="master-header">
    <h1>AI Engineering Technical Training Labs</h1>
    <p>Learning & Development Division Component Hub — Unified Interactive Sandbox Interface</p>
</div>
""", unsafe_allow_html=True)

# ── TAB COMPONENT CORE LAYOUT ────────────────────────────────────────────────
tab_overview, tab_lab1, tab_lab2, tab_lab3 = st.tabs([
    "📊 Hub Overview Matrix", 
    "✍️ Lab 1: Prompt Engineering", 
    "🤖 Lab 2: Agentic Solution", 
    "📈 Lab 3: Model Boundary Inference"
])

# ── TAB NAVIGATION: HUB OVERVIEW MATRIX ──────────────────────────────────────
with tab_overview:
    st.markdown('<div class="section-banner">Trainee Progress Telemetry</div>', unsafe_allow_html=True)
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Completed Laboratory Blocks", f"{len(st.session_state.completed_labs)} / 3 Modules")
    with m2:
        rate = int((len(st.session_state.completed_labs) / 3) * 100)
        st.metric("Curriculum Progress Rate", f"{rate}%")
    with m3:
        st.metric("System Operational Status", "Active Runtime Evaluation")
        
    st.markdown('<div class="section-banner">Laboratory Curriculum Overview</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        l1_done = "Lab 1" in st.session_state.completed_labs
        st.markdown(f"""
        <div class="ui-card">
            <div class="ui-card-title">Lab 1: Prompt Validation Sandbox</div>
            <div class="ui-card-desc">Evaluate engineering inputs against structural frameworks to convert loose language definitions into precise system task instructions.</div>
            <div style="margin-top:16px; font-size:11px; font-weight:700; color:{'#1E8449' if l1_done else '#6B7785'};">
                {'● MODULE COMPLETE' if l1_done else '○ STATUS: ACTION REQUIRED'}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        l2_done = "Lab 2" in st.session_state.completed_labs
        st.markdown(f"""
        <div class="ui-card">
            <div class="ui-card-title">Lab 2: Agentic Solution Simulation</div>
            <div class="ui-card-desc">Trace automated multi-step Reason-and-Act execution loops cross-checking distributed infrastructure logs.</div>
            <div style="margin-top:16px; font-size:11px; font-weight:700; color:{'#1E8449' if l2_done else '#6B7785'};">
                {'● MODULE COMPLETE' if l2_done else '○ STATUS: ACTION REQUIRED'}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        l3_done = "Lab 3" in st.session_state.completed_labs
        st.markdown(f"""
        <div class="ui-card">
            <div class="ui-card-title">Lab 3: Model Predictive Telemetry</div>
            <div class="ui-card-desc">Manipulate physical parameter metrics to trace real-time machine tool layer safety margin boundaries.</div>
            <div style="margin-top:16px; font-size:11px; font-weight:700; color:{'#1E8449' if l3_done else '#6B7785'};">
                {'● MODULE COMPLETE' if l3_done else '○ STATUS: ACTION REQUIRED'}
            </div>
        </div>
        """, unsafe_allow_html=True)

# ── TAB NAVIGATION: LAB 1 (PROMPT ENGINEERING) ──────────────────────────────
with tab_lab1:
    st.markdown('<div class="section-banner">Baseline Contrast Entry Controls</div>', unsafe_allow_html=True)
    c_l1_left, c_l1_right = st.columns(2)
    
    with c_l1_left:
        st.caption("Standard operational query omitting context rules:")
        st.code("Write a report on a broken pump at the industrial plant.")
        st.markdown("""
        <div class="terminal-block" style="background:#ECEFF1; color:#37474F;">
        <strong>System Output Evaluation (Baseline):</strong><br>
        The industrial pump is currently reported as non-functional. Maintenance crews should investigate the site to resolve potential issues. Please ensure standard operating procedures are verified during inspection.
        <br><br>
        <span style="color:#B03A2E; font-size:11px; font-weight:700;">⚠️ METRIC AUDIT FAILURE: NO ASSET METRICS / NO SAFETY RULES DETECTED</span>
        </div>
        """, unsafe_allow_html=True)

    with c_l1_right:
        st.caption("Trainee Engineering Workspace: Assemble your prompt input using the structural R-T-C-F-C rules (Include keywords: 'safety', 'vibration', 'checklist')")
        l1_user_prompt = st.text_area("Construct Framed Prompt Input Here:", height=108, key="txt_l1_main_input")
        
        if st.button("Execute Validation Scan", key="btn_execute_l1_scan"):
            if not l1_user_prompt.strip():
                st.warning("Input layer buffer is currently empty.")
            else:
                has_safety = any(w in l1_user_prompt.lower() for w in ["safety", "hazard", "lockout", "tagout"])
                has_vibration = any(w in l1_user_prompt.lower() for w in ["vibration", "hz", "mm/s", "sensor"])
                has_checklist = any(w in l1_user_prompt.lower() for w in ["checklist", "format", "step", "structured"])
                score = sum([has_safety, has_vibration, has_checklist])
                
                st.markdown('<div class="section-banner">Engineered Performance Output Matrix</div>', unsafe_allow_html=True)
                if score == 3:
                    st.markdown("""
                    <div class="terminal-block">
                    [SYSTEM INFERENCE VERIFIED: PRODUCTION READY TASK PROTOCOL]<br><br>
                    <strong>1. INITIAL HAZARD MITIGATION & ISOLATION</strong><br>
                    - Trigger immediate Lockout/Tagout (LOTO) protocols across upstream lines.<br>
                    - Confirm containment seals are pressurized below critical limits.<br><br>
                    <strong>2. TELEMETRY DIAGNOSTIC PROFILE</strong><br>
                    - Logged baseline structural vibration anomaly at peak 7.4 mm/s frequency.<br>
                    - Bearing cavitation detected matching localized thermal spikes.<br><br>
                    <strong>3. FIELD DEPLOYMENT CHECKLIST</strong><br>
                    - [ ] Flush chamber housing assembly.<br>
                    - [ ] Re-torque mounting anchor bolts to factory specifications.
                    </div>
                    """, unsafe_allow_html=True)
                    st.success("Target validation standards met successfully. All 3 framework context constraints mapped.")
                else:
                    st.markdown("""
                    <div class="terminal-block" style="background:#7F1D1D; color:#FEE2E2;">
                    [SYSTEM INFERENCE AUDIT FAILURE: CONSTRAINTS MISSING]<br><br>
                    The prompt entered did not contain the minimum enterprise data metrics required to override basic default responses. Met ({}/3) parameters. Ensure explicit strings for safety, vibration, and checklist options are configured.
                    </div>
                    """, unsafe_allow_html=True)
                    st.error("Validation mapping verification rejected.")

    st.markdown('<div class="section-banner">Module Context Evaluation Summary</div>', unsafe_allow_html=True)
    st.text_area("Record insights regarding prompt context constraints here:", height=70, key="txt_l1_debrief_field", placeholder="Log observations...")
    if st.button("Commit Lab 1 Progress Profile", type="primary", key="btn_commit_l1"):
        st.session_state.completed_labs.add("Lab 1")
        st.toast("Lab 1 data state successfully committed.", icon="📥")

# ── TAB NAVIGATION: LAB 2 (AGENTIC SOLUTION) ────────────────────────────────
with tab_lab2:
    st.markdown('<div class="section-banner">Complex System Incident Scenario Context</div>', unsafe_allow_html=True)
    st.markdown("""
    An automated alert warning flag signals an AI Agent that **Heavy Machinery Unit #4** is displaying elevated high-vibration boundaries. 
    The operational challenge requires processing multi-database cross-checks to evaluate scheduling an emergency shutdown versus finishing a priority line order.
    """, unsafe_allow_html=True)
    
    agent_steps = [
        {"title": "Initialize Execution Loop", "desc": "Agent sets primary target strategy and parses environment conditions.", "log": "THOUGHT: Analyzing Unit #4 telemetry alerts. Need to pull raw data metrics across sensor, maintenance records, and inventory components before delivering resolution."},
        {"title": "Execute System Cross-Checks", "desc": "Simulating parallel system API pulls across distinct corporate tracking applications.", "log": "ACTION: Querying Sensor Database (Vibration: 8.2mm/s, Temperature: 94°C) -> Querying Maintenance Ledger (Last Service: 14 days ago) -> Querying Storage Inventory (Replacement Bearings: Available in Warehouse B)."},
        {"title": "Generate Resolution Framework", "desc": "Processes complex risk-mitigation metrics to finalize the optimized deployment path.", "log": "THOUGHT: Asset vibration scores indicate high imminent mechanical risk if run continuously. Inventory levels confirm instant component availability. Mitigating total production cost failure by recommending structured operational shutdown sequence."}
    ]
    
    col_l2_left, col_l2_right = st.columns(2)
    
    with col_l2_left:
        st.markdown('<div class="section-banner">Interactive Sequence Controller</div>', unsafe_allow_html=True)
        if st.button("Advance Execution Step", key="btn_advance_l2_step", type="secondary"):
            if st.session_state.current_step_l2 < len(agent_steps):
                st.session_state.l2_logs.append(agent_steps[st.session_state.current_step_l2])
                st.session_state.current_step_l2 += 1
            else:
                st.info("Orchestration sequence completed successfully. Reset system state to re-run loop.")
                
        if st.button("Reset Simulation Link", key="btn_reset_l2_simulation"):
            st.session_state.current_step_l2 = 0
            st.session_state.l2_logs = []
            st.rerun()
            
        for index, step_block in enumerate(st.session_state.l2_logs):
            st.markdown(f"**Step {index+1}: {step_block['title']}**")
            st.caption(step_block['desc'])
            st.markdown(f'<div class="terminal-block">{step_block["log"]}</div>', unsafe_allow_html=True)
            
    with col_l2_right:
        st.markdown('<div class="section-banner">System Logic Mapping Matrix</div>', unsafe_allow_html=True)
        try:
            import graphviz
            dot = graphviz.Digraph(comment='Agent Workstream')
            dot.attr(bgcolor='#F4F6F9', color='#6B7785', fontname='Inter')
            dot.attr('node', shape='box', style='filled,rounded', color='#E3E7EC', fillcolor='#FFFFFF', fontname='Inter', fontsize='11')
            
            dot.node('A', 'Real-time Incident Alert\n(High Vibration Detected)')
            if st.session_state.current_step_l2 >= 1:
                dot.node('B', 'API Lookups\n(Sensors / Logs / Inventory)')
                dot.edge('A', 'B')
            if st.session_state.current_step_l2 >= 2:
                dot.node('C', 'Trade-off Analytics Evaluation\n(Risk vs. Target Batch Cost)')
                dot.edge('B', 'C')
            if st.session_state.current_step_l2 >= 3:
                dot.node('D', 'Optimized Recommendation Out\n(Controlled Stop Sequence)')
                dot.edge('C', 'D')
                
            st.graphviz_chart(dot, use_container_width=True)
        except Exception:
            st.info("Advancing the controller steps on the left will automatically build the trace workflow links here.")

    st.markdown('<div class="section-banner">Module Context Evaluation Summary</div>', unsafe_allow_html=True)
    st.text_area("Record insights regarding autonomous logic loops here:", height=70, key="txt_l2_debrief_field", placeholder="Log observations...")
    if st.button("Commit Lab 2 Progress Profile", type="primary", key="btn_commit_l2"):
        st.session_state.completed_labs.add("Lab 2")
        st.toast("Lab 2 data state successfully committed.", icon="📥")

# ── NAVIGATION: LAB 3 (MODEL BOUNDARY INFERENCE) ─────────────────────────────
with tab_lab3:
    st.markdown('<div class="section-banner">Continuous Parameter Telemetry Arrays</div>', unsafe_allow_html=True)
    col_l3_left, col_l3_right = st.columns(2)
    
    with col_l3_left:
        st.caption("Adjust telemetry variables to scale real-time risk predictions:")
        vibration_val = st.slider("Structural Vibration Intensity (mm/s Baseline)", 1.0, 15.0, 4.2, step=0.1, key="sld_vibration")
        temperature_val = st.slider("Thermal Core Temperature (°C Threshold)", 40, 140, 75, step=1, key="sld_temperature")
        runtime_val = st.slider("Active Operating Window (Continuous Uninterrupted Hours)", 0, 200, 48, step=1, key="sld_runtime")
        
    with col_l3_right:
        # Linear risk scoring mapping computation
        base_calc = (vibration_val * 4) + ((temperature_val - 40) * 0.4) + (runtime_val * 0.1)
        risk_score = min(int(base_calc), 100)
        
        m_col1, m_col2 = st.columns(2)
        with m_col1:
            st.metric("Calculated Boundary Risk Index", f"{risk_score}%")
        with m_col2:
            st.metric("Evaluation Safety State", "Verified Stable" if risk_score < 45 else "Action Required")
            
        if risk_score < 45:
            status_label = "STABLE OPERATING WINDOW (Low Mechanical Wear)"
            status_hex = "#1E8449" # Success dark green
        elif risk_score < 75:
            status_label = "ELEVATED TEMPERATURE/WEAR PROFILE (Monitor Metrics)"
            status_hex = "#C5821A" # Muted warning amber
        else:
            status_label = "CRITICAL FAIL MARGIN BOUNDARY (Immediate Shutdown Recommended)"
            status_hex = "#B03A2E" # Alert threat red
            
        st.markdown(f"""
        <div style="background:{status_hex}; color:#FFFFFF; padding:16px; border-radius:var(--radius); margin-top:14px; font-weight:700; text-align:center; font-size:14px; letter-spacing:-0.01em;">
            {status_label}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-banner">Module Context Evaluation Summary</div>', unsafe_allow_html=True)
    st.text_area("Record insights regarding continuous model tracking parameters here:", height=70, key="txt_l3_debrief_field", placeholder="Log observations...")
    if st.button("Commit Lab 3 Progress Profile", type="primary", key="btn_commit_l3"):
        st.session_state.completed_labs.add("Lab 3")
        st.toast("Lab 3 data state successfully committed.", icon="📥")

# ── GLOBAL PROGRAM COMPLETION NOTIFICATION ────────────────────────────────────
if len(st.session_state.completed_labs) == 3:
    st.markdown('<div style="margin-top: 32px; border-bottom: 2px dashed var(--c-line);"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background:var(--c-primary); color:#FFFFFF; border-radius:var(--radius); padding:24px; text-align:center; margin-top:24px; box-shadow:0 4px 14px rgba(15, 61, 97, 0.15);">
        <div style="font-size:18px; font-weight:700; color:#FFFFFF;">🏆 Technical Laboratory Evaluation Program Complete</div>
        <div style="color:#D4E6F1; font-size:13px; margin-top:6px; max-width:650px; margin-left:auto; margin-right:auto; line-height:1.5; opacity:0.9;">
            All core sandbox operations have been logged. Trainee assessment profile data is finalized and prepared for internal systems integration processing.
        </div>
    </div>
    """, unsafe_allow_html=True)

```
