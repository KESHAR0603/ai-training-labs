import streamlit as st
import time
import json
import random

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Labs — L&D Division",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── GLOBAL CORPORATE DESIGN SYSTEM (CSS) ─────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* Typography & Layout Fundamentals */
html, body, [class*="css"] { 
    font-family: 'Inter', sans-serif; 
    color: #1E293B;
}

.main { 
    background: #F8FAFC; 
}

/* Typographic Scale & Visual Hierarchy */
.app-title {
    font-size: 24px;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 4px;
    letter-spacing: -0.02em;
}

.app-subtitle {
    font-size: 13px;
    font-weight: 400;
    color: #64748B;
    margin-bottom: 24px;
}

.section-banner {
    font-size: 14px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #475569;
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 6px;
    margin-top: 24px;
    margin-bottom: 16px;
}

/* Standardized Card & Container Architecture */
.lab-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    padding: 16px 20px;
    margin-bottom: 16px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 140px; /* Equal-height alignment pattern */
}

.card-title {
    font-size: 15px;
    font-weight: 600;
    color: #0F172A;
    margin-bottom: 4px;
}

.card-desc {
    font-size: 13px;
    color: #475569;
    line-height: 1.5;
}

/* Micro-Components & Data Tags */
.status-tag {
    display: inline-flex;
    align-items: center;
    font-size: 11px;
    font-weight: 600;
    padding: 2px 8px;
    border-radius: 4px;
    margin-top: 12px;
    width: max-content;
}

.tag-incomplete { background: #F1F5F9; color: #475569; border: 1px solid #E2E8F0; }
.tag-complete { background: #ECFDF5; color: #065F46; border: 1px solid #A7F3D0; }

.sandbox-output {
    background: #0F172A;
    color: #F8FAFC;
    font-family: 'Courier New', Courier, monospace;
    font-size: 13px;
    padding: 16px;
    border-radius: 8px;
    line-height: 1.6;
    margin: 12px 0;
}

/* Premium Sidebar Interface */
section[data-testid="stSidebar"] {
    background: #0F172A !important;
    padding-top: 20px;
}
section[data-testid="stSidebar"] * { color: #F8FAFC !important; }

.sidebar-heading {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #94A3B8 !important;
    margin-top: 20px;
    margin-bottom: 8px;
    padding-left: 4px;
}

.sidebar-footer {
    font-size: 11px;
    color: #64748B !important;
    margin-top: 40px;
    border-top: 1px solid #1E293B;
    padding-top: 12px;
    padding-left: 4px;
}

/* Streamlit Native Component Tuning */
div[data-testid="stMetricValue"] > div {
    font-size: 22px !important;
    font-weight: 700 !important;
    color: #0F172A !important;
}
div[data-testid="stMetricLabel"] > div {
    font-size: 12px !important;
    color: #64748B !important;
}
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE INITIALIZATION ─────────────────────────────────────────────
if "completed_labs" not in st.session_state:
    st.session_state.completed_labs = set()
if "current_step_l2" not in st.session_state:
    st.session_state.current_step_l2 = 0
if "l2_logs" not in st.session_state:
    st.session_state.l2_logs = []

# ── SIDEBAR ARCHITECTURE ─────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div style="font-size: 16px; font-weight: 700; color: #FFFFFF; letter-spacing: -0.01em; margin-bottom: 2px;">Enterprise AI Labs</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 12px; color: #94A3B8 !important; margin-bottom: 20px;">Learning & Development Division</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #1E293B; margin-bottom: 16px;"></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-heading">Navigation</div>', unsafe_allow_html=True)
    current_page = st.radio(
        label="Select Workspace",
        options=["Overview Dashboard", "Lab 1: Prompt Validation", "Lab 2: Agentic Framework", "Lab 3: Telemetry Inference"],
        label_visibility="collapsed"
    )
    
    st.markdown('<div class="sidebar-heading">Program Progress</div>', unsafe_allow_html=True)
    progress_percent = int((len(st.session_state.completed_labs) / 3) * 100)
    st.progress(progress_percent / 100)
    st.markdown(f'<div style="font-size: 12px; color: #E2E8F0 !important; margin-top: 4px;">Track Progress: {len(st.session_state.completed_labs)} / 3 Modules Complete</div>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="sidebar-footer">User ID: KM-LD-2026<br>Status: Evaluation Mode</div>', unsafe_allow_html=True)

# ── NAVIGATION: OVERVIEW DASHBOARD ───────────────────────────────────────────
if current_page == "Overview Dashboard":
    st.markdown('<div class="app-title">Technical Training Portal</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">Interactive laboratory sandbox environments for evaluating advanced enterprise AI solutions.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-banner">Available Laboratory Modules</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        is_done = "Lab 1" in st.session_state.completed_labs
        tag_cls = "tag-complete" if is_done else "tag-incomplete"
        tag_txt = "Status: Complete" if is_done else "Status: Pending Action"
        st.markdown(f"""
        <div class="lab-card">
            <div>
                <div class="card-title">Lab 1: Prompt Validation</div>
                <div class="card-desc">Evaluate inputs using structural evaluation frameworks to transform loose language inputs into precise automation instruction scripts.</div>
            </div>
            <div class="status-tag {tag_cls}">{tag_txt}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Access Lab 1", use_container_width=True):
            st.info("Please use the left sidebar navigation matrix to step directly into Lab 1.")
            
    with col2:
        is_done = "Lab 2" in st.session_state.completed_labs
        tag_cls = "tag-complete" if is_done else "tag-incomplete"
        tag_txt = "Status: Complete" if is_done else "Status: Pending Action"
        st.markdown(f"""
        <div class="lab-card">
            <div>
                <div class="card-title">Lab 2: Agentic Framework</div>
                <div class="card-desc">Simulate multi-step Reason-and-Act (ReAct) architectures executing system cross-checks across distributed asset parameters.</div>
            </div>
            <div class="status-tag {tag_cls}">{tag_txt}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Access Lab 2", use_container_width=True):
            st.info("Please use the left sidebar navigation matrix to step directly into Lab 2.")
            
    with col3:
        is_done = "Lab 3" in st.session_state.completed_labs
        tag_cls = "tag-complete" if is_done else "tag-incomplete"
        tag_txt = "Status: Complete" if is_done else "Status: Pending Action"
        st.markdown(f"""
        <div class="lab-card">
            <div>
                <div class="card-title">Lab 3: Telemetry Inference</div>
                <div class="card-desc">Model continuous sensor streams against deep multi-dimensional boundaries to instantly trace and map asset failure risks.</div>
            </div>
            <div class="status-tag {tag_cls}">{tag_txt}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Access Lab 3", use_container_width=True):
            st.info("Please use the left sidebar navigation matrix to step directly into Lab 3.")

# ── NAVIGATION: LAB 1 ────────────────────────────────────────────────────────
elif current_page == "Lab 1: Prompt Validation":
    st.markdown('<div class="app-title">Lab 1: Prompt Validation Sandbox</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">Study how structural prompt validation constraints modify language model inference quality.</div>', unsafe_allow_html=True)
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown('<div class="section-banner">Baseline Unstructured Entry Control</div>', unsafe_allow_html=True)
        st.caption("Standard operational query omitting context rules:")
        st.code("Write a report on a broken pump at the industrial plant.")
        
        st.markdown('<div class="section-banner">Baseline System Response Output</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="sandbox-output" style="background:#F1F5F9; color:#334155; border:1px solid #E2E8F0;">
        <strong>System Output Evaluation:</strong><br>
        The industrial pump is currently reported as non-functional. Maintenance crews should investigate the site to resolve potential issues. Please ensure standard operating procedures are verified during inspection.
        <br><br>
        <span style="color:#94A3B8; font-size:11px; font-weight:600;">⚠️ METRIC AUDIT FAILURE: NO ASSET METRICS / NO SAFETY RULES DETECTED</span>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        st.markdown('<div class="section-banner">Active Trainee Engineering Workspace</div>', unsafe_allow_html=True)
        st.markdown("""
        Assemble your prompt following the **R-T-C-F-C** framework rules:<br>
        1. **Role** (Expert engineer) &nbsp;|&nbsp; 2. **Task** (Analyze pump failure) &nbsp;|&nbsp; 3. **Context** (Include safety thresholds) &nbsp;|&nbsp; 4. **Format** (Structured checklist) &nbsp;|&nbsp; 5. **Constraints** (Include vibration limits)
        """, unsafe_allow_html=True)
        
        trainee_input = st.text_area(
            "Construct Structured Prompt Input:",
            height=140,
            placeholder="Type your engineered framework prompt script here..."
        )
        
        if st.button("Execute Validation Scan", type="secondary"):
            if not trainee_input.strip():
                st.warning("Input buffer empty. Provide prompt input to execute evaluation analysis.")
            else:
                with st.spinner("Processing framework tokens..."):
                    time.sleep(1.2)
                
                # Dynamic scoring matrix
                has_safety = any(w in trainee_input.lower() for w in ["safety", "hazard", "lockout", "tagout", "protocol"])
                has_vibration = any(w in trainee_input.lower() for w in ["vibration", "frequency", "hz", "sensor", "mm/s", "amplitude"])
                has_checklist = any(w in trainee_input.lower() for w in ["checklist", "format", "step", "bullet", "structured"])
                
                score = sum([has_safety, has_vibration, has_checklist])
                
                st.markdown('<div class="section-banner">Engineered Architecture Output</div>', unsafe_allow_html=True)
                
                if score == 3:
                    st.markdown("""
                    <div class="sandbox-output">
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
                    <div class="sandbox-output" style="background:#7F1D1D; color:#FEE2E2;">
                    [SYSTEM INFERENCE AUDIT FAILURE: CONSTRAINTS MISSING]<br><br>
                    The prompt entered did not contain the minimum enterprise data metrics required to override basic default responses. Ensure explicit structural parameters for asset safety, vibration telemetry, and structural formatting options are included.
                    </div>
                    """, unsafe_allow_html=True)
                    st.error(f"Validation verification failed. Met ({score}/3) metrics. Verify prompt contains safety, vibration, and checklist requirements.")

    # Shared Debrief Section
    st.markdown('<div class="section-banner">Module Context Evaluation Summary</div>', unsafe_allow_html=True)
    st.text_area("Record architectural insights regarding prompt constraints here:", height=80, key="l1_notes", placeholder="Log your observations...")
    
    if st.button("Mark Lab 1 Complete", type="primary"):
        st.session_state.completed_labs.add("Lab 1")
        st.toast("Progress Saved: Lab 1 successfully committed to profile.", icon="📥")

# ── NAVIGATION: LAB 2 ────────────────────────────────────────────────────────
elif current_page == "Lab 2: Agentic Framework":
    st.markdown('<div class="app-title">Lab 2: Agentic Framework Simulation</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">Observe autonomous orchestration layers tracing system anomalies across separate mock system metrics.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-banner">Complex System Incident Scenario Context</div>', unsafe_allow_html=True)
    st.markdown("""
    An automated system warning flag alerts an AI Agent that **Heavy Machinery Unit #4** is displaying abnormal high-vibration alarms. 
    The operational challenge requires evaluating whether to maintain full throughput runtime to complete a priority line batch order or execute an immediate safe technical sequence shutdown.
    """, unsafe_allow_html=True)
    
    steps = [
        {"title": "Initialize Execution Loop", "desc": "Agent sets primary target strategy and parses environment conditions.", "log": "THOUGHT: Analyzing Unit #4 telemetry alerts. Need to pull raw data metrics across sensor, maintenance records, and inventory components before delivering resolution."},
        {"title": "Execute System Cross-Checks", "desc": "Simulating parallel system API pulls across distinct corporate tracking applications.", "log": "ACTION: Querying Sensor Database (Vibration: 8.2mm/s, Temperature: 94°C) -> Querying Maintenance Ledger (Last Service: 14 days ago) -> Querying Storage Inventory (Replacement Bearings: Available in Warehouse B)."},
        {"title": "Generate Resolution Framework", "desc": "Processes complex risk-mitigation metrics to finalize the optimized deployment path.", "log": "THOUGHT: Asset vibration scores indicate high imminent mechanical risk if run continuously. Inventory levels confirm instant component availability. Mitigating total production cost failure by recommending structured operational shutdown sequence."}
    ]
    
    c1, c2 = st.columns([1, 1])
    
    with c1:
        st.markdown('<div class="section-banner">Interactive Sequence Controller</div>', unsafe_allow_html=True)
        if st.button("Advance Execution Step", type="secondary"):
            if st.session_state.current_step_l2 < len(steps):
                curr = steps[st.session_state.current_step_l2]
                st.session_state.l2_logs.append(curr)
                st.session_state.current_step_l2 += 1
            else:
                st.info("Orchestration sequence completed successfully. Reset system state to re-run execution loop.")
        
        if st.button("Reset Framework State"):
            st.session_state.current_step_l2 = 0
            st.session_state.l2_logs = []
            st.rerun()

        for idx, log_item in enumerate(st.session_state.l2_logs):
            st.markdown(f'**Step {idx+1}: {log_item["title"]}**')
            st.caption(log_item["desc"])
            st.markdown(f'<div class="sandbox-output">{log_item["log"]}</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="section-banner">System Logic Mapping Matrix</div>', unsafe_allow_html=True)
        try:
            import graphviz
            dot = graphviz.Digraph(comment='Agent Logic Workstream')
            dot.attr(bgcolor='#F8FAFC', color='#475569', fontname='Inter')
            dot.attr('node', shape='box', style='filled,rounded', color='#E2E8F0', fillcolor='#FFFFFF', fontname='Inter', fontsize='11')
            
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
            st.info("System mapping matrix diagram active. Advance execution controller steps to trace data links.")

    st.markdown('<div class="section-banner">Module Context Evaluation Summary</div>', unsafe_allow_html=True)
    st.text_area("Record architectural insights regarding autonomous logic loops here:", height=80, key="l2_notes", placeholder="Log your observations...")
    
    if st.button("Mark Lab 2 Complete", type="primary"):
        st.session_state.completed_labs.add("Lab 2")
        st.toast("Progress Saved: Lab 2 successfully committed to profile.", icon="📥")

# ── NAVIGATION: LAB 3 ────────────────────────────────────────────────────────
elif current_page == "Lab 2: Agentic Framework":
    pass  # Standard structural guard container block
    
elif current_page == "Lab 3: Telemetry Inference":
    st.markdown('<div class="app-title">Lab 3: Predictive Telemetry Simulation</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">Manipulate environmental sensor inputs to track model confidence thresholds against failure boundaries.</div>', unsafe_allow_html=True)
    
    col_ctrl, col_metrics = st.columns([1, 1])
    
    with col_ctrl:
        st.markdown('<div class="section-banner">Continuous Sensor Parameter Controls</div>', unsafe_allow_html=True)
        vibration = st.slider("Structural Vibration Intensity (mm/s Baseline)", 1.0, 15.0, 4.2, step=0.1)
        temperature = st.slider("Thermal Core Temperature (°C Threshold)", 40, 140, 75, step=1)
        runtime_hrs = st.slider("Active Operating Window (Continuous Uninterrupted Hours)", 0, 200, 48, step=1)

    with col_metrics:
        st.markdown('<div class="section-banner">Inference Analytical Monitoring Metrics</div>', unsafe_allow_html=True)
        
        # Linear risk scoring mapping computation
        base_risk = (vibration * 4) + ((temperature - 40) * 0.4) + (runtime_hrs * 0.1)
        calculated_risk = min(int(base_risk), 100)
        
        if calculated_risk < 45:
            alert_state = "NORMAL (Low Wear)"
            status_color = "#059669" # Stable Dark Green
        elif calculated_risk < 75:
            alert_state = "ELEVATED (Attention Required)"
            status_color = "#D97706" # Warning Amber
        else:
            alert_state = "CRITICAL FAILURE RISK (Imminent Hazard)"
            status_color = "#DC2626" # Threat Red

        m1, m2 = st.columns(2)
        with m1:
            st.metric("Risk Score Index", f"{calculated_risk}%")
        with m2:
            st.metric("Evaluation Status", "Verified Stable" if calculated_risk < 45 else "Action Required")
            
        st.markdown(f"""
        <div style="background:{status_color}; color:#FFFFFF; padding:14px 18px; border-radius:8px; margin-top:16px;">
            <div style="font-size:11px; text-transform:uppercase; font-weight:600; opacity:0.85; letter-spacing:0.02em;">Model Boundary Status Report</div>
            <div style="font-size:15px; font-weight:700; margin-top:2px;">{alert_state}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-banner">Module Context Evaluation Summary</div>', unsafe_allow_html=True)
    st.text_area("Record architectural insights regarding continuous sensor inference lines here:", height=80, key="l3_notes", placeholder="Log your observations...")
    
    if st.button("Mark Lab 3 Complete", type="primary"):
        st.session_state.completed_labs.add("Lab 3")
        st.toast("Progress Saved: Lab 3 successfully committed to profile.", icon="📥")

# ── GLOBAL PROGRAM COMPLETION LOGIC ──────────────────────────────────────────
if len(st.session_state.completed_labs) == 3:
    st.markdown('<div style="margin-top: 40px; border-bottom: 1px solid #E2E8F0;"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#0F172A; color:#FFFFFF; border-radius:8px; padding:24px; text-align:center; margin-top:24px;">
        <div style="font-size:20px; font-weight:700; color:#FFFFFF; letter-spacing:-0.01em;">Technical Laboratory Program Complete</div>
        <div style="color:#94A3B8; font-size:13px; margin-top:4px; max-width:600px; margin-left:auto; margin-right:auto; line-height:1.5;">
            All three core modules have been processed. Trainee data records indicate alignment with operational evaluation metrics. Workspace status logged as ready for production integration assessments.
        </div>
    </div>
    """, unsafe_allow_html=True)
