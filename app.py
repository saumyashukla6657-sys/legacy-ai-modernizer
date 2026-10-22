import streamlit as st
import json
import os
from extractor import extract_modernization_evidence
from step1_prep import load_and_index_code

st.set_page_config(
    page_title="Agii Modernizer - Discovery Workbench",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Agii AI Modernizer: Legacy Discovery & Audit Workbench")
st.caption("Automated reverse-engineering, line-level evidence tracking, and risk analysis for legacy code.")

# Sidebar - File Controls
st.sidebar.header("📁 Source Input")
uploaded_file = st.sidebar.file_uploader("Upload Legacy File (.cob, .cbl, .txt)", type=["cob", "cbl", "txt"])

use_sample = st.sidebar.button("Use Sample: sample_loan.cob")

target_file_path = None

if uploaded_file is not None:
    os.makedirs("temp", exist_ok=True)
    temp_path = os.path.join("temp", uploaded_file.name)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    target_file_path = temp_path
elif use_sample or "sample_loan.cob" in os.listdir("data"):
    target_file_path = "data/sample_loan.cob"

# Main Layout
col_left, col_right = st.columns([1, 1], gap="large")

if target_file_path and os.path.exists(target_file_path):
    # Left Column: Line-numbered source viewer
    with col_left:
        st.subheader("📄 Legacy Source Code")
        annotated_code = load_and_index_code(target_file_path)
        st.code(annotated_code, language="cobol", line_numbers=False)

    # Right Column: AI Extraction & Human Review
    with col_right:
        st.subheader("🔍 Modernization Evidence & Audit")
        
        if st.button("🚀 Run AI Reverse-Engineering", type="primary"):
            with st.spinner("Parsing syntax, tracing logic, and flagging risks..."):
                artifact = extract_modernization_evidence(target_file_path)
                st.session_state["artifact"] = artifact

        if "artifact" in st.session_state:
            data = st.session_state["artifact"]
            
            # Program Summary Card
            st.success(f"**Program ID:** {data.program_name}")
            st.info(f"**Executive Summary:** {data.executive_summary}")

            # Business Rules Tab & Risk Tab
            tab_rules, tab_risks = st.tabs(["📋 Extracted Business Rules", "⚠️ Migration Risks"])

            with tab_rules:
                st.markdown("##### Human-in-the-Loop Rule Verification")
                for rule in data.business_rules:
                    with st.expander(f"{rule.rule_id} — Lines {rule.source_lines}"):
                        st.write(f"**Condition:** `{rule.legacy_condition}`")
                        st.write(f"**Action:** `{rule.action_taken}`")
                        st.write(f"**Business Logic:** {rule.description}")
                        st.checkbox(f"Approve & Validate {rule.rule_id}", key=rule.rule_id)

            with tab_risks:
                st.markdown("##### Risk Register")
                for rsk in data.risks:
                    color = "red" if rsk.severity in ["HIGH", "CRITICAL"] else "orange"
                    st.markdown(f":{color}[**[{rsk.severity}] {rsk.risk_id} — {rsk.category}**]")
                    st.write(f"**Issue:** {rsk.summary}")
                    st.write(f"**Recommended Action:** {rsk.remediation}")
                    st.divider()

            # Export Button
            st.download_button(
                label="📥 Export Audited Evidence Package (JSON)",
                data=data.model_dump_json(indent=2),
                file_name=f"{data.program_name}_evidence_package.json",
                mime="application/json"
            )
else:
    st.info("Upload a legacy file or load the sample from the sidebar to begin.")