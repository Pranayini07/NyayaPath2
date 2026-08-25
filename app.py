"""
Judicial Court Process & Case Flow Explainer Bot - NyayaPath

Main Streamlit application refactored with Apple-Grade Premium Design System.
"""

import streamlit as st
from safety import evaluate_query
from ai_handler import get_ai_response
from pages.jurisdiction_navigator import render_jurisdiction_navigator_page
from ui_theme import (
    inject_custom_css,
    render_brand_header,
    render_trust_bar,
    render_information_scope_card,
    render_privacy_notice,
    render_footer
)

# ============================================================================
# PAGE CONFIGURATION & THEME INJECTION
# ============================================================================

st.set_page_config(
    page_title="NyayaPath — Educational Court Process Portal",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="expanded"
)

inject_custom_css()

# ============================================================================
# NAVBAR NAVIGATION
# ============================================================================

with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 0.5rem 0 1.25rem 0;">
            <div style="font-size: 1.6rem; font-weight: 800; color: #1D1D1F; font-family: 'Plus Jakarta Sans', sans-serif; letter-spacing: -0.02em;">⚖️ NyayaPath</div>
            <div style="font-size: 0.775rem; color: #86868B; font-weight: 500;">Civic Legal Literacy Portal</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #86868B; margin-bottom: 0.5rem;">
            Navigation
        </div>
    """, unsafe_allow_html=True)
    
    selected_page = st.radio(
        "Navigation Options",
        options=["🏠 Home", "🏛 Jurisdiction Navigator"],
        key="app_navigation",
        label_visibility="collapsed"
    )
    st.markdown("---")

# ============================================================================
# PAGE ROUTING
# ============================================================================

if selected_page == "🏛 Jurisdiction Navigator":
    render_jurisdiction_navigator_page()

else:  # 🏠 Home Page
    # Apple Keynote Header & Trust Badges
    render_brand_header()
    render_trust_bar()

    # Scope & Transparency Card
    render_information_scope_card()

    # Main Inquiry Section Header
    st.markdown("""
        <div style="margin-top: 1.75rem; margin-bottom: 0.85rem;">
            <h3 style="margin-bottom: 0.2rem; color: #1D1D1F; font-weight: 700; letter-spacing: -0.02em;">🔍 Search Legal Procedures</h3>
            <p style="font-size: 0.925rem; color: #6E6E73; margin: 0;">
                Ask any question regarding court hearings, procedural stages, or legal terminology.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Quick Starter Topic Suggestions
    st.markdown("""
        <div style="font-size: 0.775rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; color: #86868B; margin-bottom: 0.65rem;">
            💡 Popular Topics:
        </div>
    """, unsafe_allow_html=True)

    # Topic Starter Buttons
    col_t1, col_t2, col_t3 = st.columns(3)
    
    if "quick_topic_selected" not in st.session_state:
        st.session_state["quick_topic_selected"] = ""

    with col_t1:
        if st.button("📋 Civil Suit Stages", use_container_width=True, key="quick_civil"):
            st.session_state["quick_topic_selected"] = "What are the typical stages of a civil court case from filing to final judgment?"
            st.rerun()
    with col_t2:
        if st.button("⚖️ Criminal Trial Flow", use_container_width=True, key="quick_criminal"):
            st.session_state["quick_topic_selected"] = "How does a criminal trial proceed from FIR and charge sheet to trial?"
            st.rerun()
    with col_t3:
        if st.button("📜 What is a Summons?", use_container_width=True, key="quick_summons"):
            st.session_state["quick_topic_selected"] = "What is a court summons and what generally happens after receiving one?"
            st.rerun()

    col_t4, col_t5, col_t6 = st.columns(3)
    with col_t4:
        if st.button("🔄 Appeals Process", use_container_width=True, key="quick_appeal"):
            st.session_state["quick_topic_selected"] = "What are the grounds and general procedure for filing an appeal in court?"
            st.rerun()
    with col_t5:
        if st.button("🔓 How Bail Works", use_container_width=True, key="quick_bail"):
            st.session_state["quick_topic_selected"] = "What is the general concept and procedure of bail in criminal matters?"
            st.rerun()
    with col_t6:
        if st.button("📑 Burden of Proof", use_container_width=True, key="quick_proof"):
            st.session_state["quick_topic_selected"] = "What does 'burden of proof' mean and how does it differ in civil vs criminal cases?"
            st.rerun()

    # Privacy Shield Callout
    render_privacy_notice()

    # Initial text value from quick topic if selected
    initial_text = st.session_state.get("quick_topic_selected", "")
    
    user_query = st.text_area(
        "Enter your question about court procedures, case stages, or legal terminology:",
        value=initial_text,
        height=110,
        placeholder="e.g. What are the key stages of a civil case after filing a plaint?",
        key="user_input"
    )

    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        submit_button = st.button("Explain Procedure", type="primary", use_container_width=True)

    # Safety Evaluation & AI Processing
    if submit_button and user_query:
        decision = evaluate_query(user_query)
        
        if not decision.allowed:
            st.markdown(f"""
                <div class="apple-refusal-card">
                    <div class="apple-refusal-title">
                        <span>🛡️</span>
                        <span>Information Scope Notice</span>
                    </div>
                    <div class="apple-refusal-text">{decision.refusal_message}</div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("""
                <div class="apple-tip-card">
                    💡 <strong>Educational Guidance:</strong> NyayaPath cannot provide personalized guidance on specific personal disputes. Rephrase your question to focus on general legal procedures (e.g. <em>"What happens during an evidence hearing?"</em> or <em>"What is an interim order?"</em>).
                </div>
            """, unsafe_allow_html=True)
        else:
            with st.spinner("Processing educational explanation..."):
                ai_response = get_ai_response(user_query, decision)
                
                if ai_response.success:
                    st.markdown("---")
                    st.markdown(f"""
                        <div class="apple-article-card">
                            <div class="apple-article-header">
                                <span class="apple-category-badge">Educational Explanation</span>
                                <span style="font-size: 0.8rem; color: #86868B;">🛡️ AI-Assisted Educational Content</span>
                            </div>
                            <div class="apple-article-body">{ai_response.text}</div>
                        </div>
                    """, unsafe_allow_html=True)
                    st.caption(f"💡 Reference ID: `{ai_response.request_id}` | Educational information only. Not legal counsel.")
                else:
                    st.markdown(f"""
                        <div class="apple-refusal-card">
                            <div class="apple-refusal-title">
                                <span>⚠️</span>
                                <span>System Message</span>
                            </div>
                            <div class="apple-refusal-text">{ai_response.text}</div>
                        </div>
                    """, unsafe_allow_html=True)

    elif submit_button and not user_query:
        st.warning("Please enter a question before clicking 'Explain Procedure'.")

    # Discovery Banner for Jurisdiction Navigator
    st.markdown("""
        <div class="apple-discovery-banner">
            <div class="apple-discovery-title">🏛 Need Context for a Specific State or Court Tier?</div>
            <div class="apple-discovery-text">
                Use the <strong>Jurisdiction Navigator</strong> to explore legal procedures customized to your state, court level (District, High Court), and legal domain.
            </div>
        </div>
    """, unsafe_allow_html=True)

# ============================================================================
# SIDEBAR SHARED CONTENT
# ============================================================================

with st.sidebar:
    if selected_page == "🏠 Home":
        st.markdown("""
            <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #86868B; margin-bottom: 0.5rem;">
                Sample Inquiries
            </div>
        """, unsafe_allow_html=True)
        
        with st.expander("📌 Procedural Workflows", expanded=True):
            st.markdown("""
                - *What are the stages of a civil suit?*
                - *How does a criminal trial proceed?*
                - *What happens during an appeal?*
            """)
        with st.expander("📖 Legal Terminology", expanded=False):
            st.markdown("""
                - *What does "plaintiff" mean?*
                - *What is a "written statement"?*
                - *What is the "burden of proof"?*
            """)
        with st.expander("📑 Court Documents", expanded=False):
            st.markdown("""
                - *What is the purpose of an affidavit?*
                - *What is a stay order?*
                - *What is a Vakalatnama?*
            """)
        st.markdown("---")

    st.markdown("""
        <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #86868B; margin-bottom: 0.5rem;">
            Out-of-Scope Requests
        </div>
        <div style="font-size: 0.8rem; color: #6E6E73; line-height: 1.55; margin-bottom: 1rem;">
            • Specific personal legal advice<br>
            • Litigation strategy to win<br>
            • Outcome predictions or odds<br>
            • Customized document generation
        </div>
    """, unsafe_allow_html=True)

    # Engine Status Widget
    st.markdown("""
        <div class="apple-sidebar-status">
            <div class="apple-status-row">
                <span>AI Engine:</span>
                <span class="apple-status-val">Gemini AI</span>
            </div>
            <div class="apple-status-row">
                <span>Safety Guardrails:</span>
                <span class="apple-status-val">Active (v2.4)</span>
            </div>
            <div class="apple-status-row">
                <span>Data Retention:</span>
                <span class="apple-status-val">Zero (No PII)</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Footer
render_footer()
