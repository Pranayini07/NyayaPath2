"""
Judicial Court Process & Case Flow Explainer Bot - NyayaPath

Main Streamlit application refactored with Trusted Civic Technology UI Design System.
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
    page_title="NyayaPath — Public Legal Information & Education",
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
        <div style="text-align: center; padding: 0.5rem 0 1rem 0;">
            <div style="font-size: 1.8rem; font-weight: 800; color: #0F2942; font-family: 'Outfit', sans-serif;">⚖️ NYAYAPATH</div>
            <div style="font-size: 0.775rem; color: #64748B; font-weight: 500;">Civic Legal Literacy Portal</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="np-sidebar-nav-header">🧭 Navigation</div>', unsafe_allow_html=True)
    selected_page = st.radio(
        "Navigation",
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
    # Header & Trust Badges
    render_brand_header()
    render_trust_bar()

    # Information Scope & Transparency Card
    render_information_scope_card()

    # Main Inquiry Section Header
    st.markdown("""
        <div style="margin-top: 1.5rem; margin-bottom: 0.75rem;">
            <h3 style="margin-bottom: 0.2rem; color: #0F2942;">🔍 Ask NyayaPath</h3>
            <p style="font-size: 0.9rem; color: #64748B; margin: 0;">
                Ask any question about judicial processes, court hearings, case stages, or legal terms.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Quick Starter Topic Suggestions
    st.markdown("""
        <div class="np-chips-container">
            <div class="np-chips-label">💡 Explore Common Procedural Topics:</div>
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

    # Privacy Notice directly above input box
    render_privacy_notice()

    # Initial value from quick topic if chosen
    initial_text = st.session_state.get("quick_topic_selected", "")
    
    user_query = st.text_area(
        "Enter your question about court procedures, case stages, or legal terminology:",
        value=initial_text,
        height=110,
        placeholder="e.g. What are the key stages of a civil case after filing a plaint?",
        key="user_input"
    )

    col1, col2, col3 = st.columns([1, 1.6, 1])
    with col2:
        submit_button = st.button("✨ Explain Court Procedure", type="primary", use_container_width=True)

    # Multi-Layer Safety Evaluation & Processing
    if submit_button and user_query:
        decision = evaluate_query(user_query)
        
        if not decision.allowed:
            # Display styled safe refusal card
            st.markdown(f"""
                <div class="np-refusal-card">
                    <div class="np-refusal-title">
                        <span>🛡️</span>
                        <span>Information Scope Notice</span>
                    </div>
                    <div class="np-refusal-text">{decision.refusal_message}</div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("""
                <div class="np-tip-card">
                    💡 <strong>Educational Guidance:</strong> NyayaPath cannot give personalized counsel on specific personal disputes. Try rephrasing your question to focus on general court processes (e.g. <em>"What happens during an evidence stage in civil court?"</em> or <em>"What is the general purpose of an injunction?"</em>).
                </div>
            """, unsafe_allow_html=True)
        else:
            with st.spinner("Analyzing question and generating plain-language educational explanation..."):
                ai_response = get_ai_response(user_query, decision)
                
                if ai_response.success:
                    # Structured Knowledge Article Container
                    st.markdown("---")
                    st.markdown(f"""
                        <div class="np-article-card">
                            <div class="np-article-header">
                                <span class="np-article-category">📖 NyayaPath Educational Article</span>
                                <span class="np-article-transparency">🛡️ AI-Assisted Educational Content</span>
                            </div>
                            <div class="np-article-body">{ai_response.text}</div>
                        </div>
                    """, unsafe_allow_html=True)
                    st.caption(f"💡 Reference ID: `{ai_response.request_id}` | Educational legal information only. Not legal advice.")
                else:
                    st.markdown(f"""
                        <div class="np-refusal-card">
                            <div class="np-refusal-title">
                                <span>⚠️</span>
                                <span>System Message</span>
                            </div>
                            <div class="np-refusal-text">{ai_response.text}</div>
                        </div>
                    """, unsafe_allow_html=True)

    elif submit_button and not user_query:
        st.warning("Please enter a question before clicking 'Explain Court Procedure'.")

    # Feature Discovery Banner for Jurisdiction Navigator
    st.markdown("""
        <div class="np-discovery-card">
            <div>
                <div class="np-discovery-title">🏛 Need State or Court-Specific Guidance?</div>
                <div class="np-discovery-text">
                    Use the <strong>Jurisdiction Navigator</strong> to explore procedures customized to your state, court tier (District, High Court), and legal domain.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ============================================================================
# SIDEBAR SHARED FOOTER & EXAMPLES
# ============================================================================

with st.sidebar:
    if selected_page == "🏠 Home":
        st.markdown('<div class="np-sidebar-nav-header">💡 Sample Inquiries</div>', unsafe_allow_html=True)
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
        with st.expander("📑 Court Filings & Documents", expanded=False):
            st.markdown("""
                - *What is the purpose of an affidavit?*
                - *What is a stay order?*
                - *What is a Vakalatnama?*
            """)
        st.markdown("---")

    st.markdown('<div class="np-sidebar-nav-header">🚫 Out-of-Scope Requests</div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="font-size: 0.8rem; color: #64748B; line-height: 1.55; margin-bottom: 1rem;">
            • Specific personal legal advice<br>
            • Litigation tactics to win<br>
            • Outcome predictions or odds<br>
            • Customized document drafting
        </div>
    """, unsafe_allow_html=True)

    # Engine Status Widget
    st.markdown("""
        <div class="np-engine-status-card">
            <div class="np-status-row">
                <span>AI Knowledge Model:</span>
                <span class="np-status-tag">● Gemini AI</span>
            </div>
            <div class="np-status-row">
                <span>Multi-Layer Safety:</span>
                <span class="np-status-tag">● Active (v2.4)</span>
            </div>
            <div class="np-status-row">
                <span>PII Storage:</span>
                <span class="np-status-tag">● None (Zero Retention)</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Civic Footer
render_footer()
