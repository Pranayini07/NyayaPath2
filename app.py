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
    st.markdown("### 🧭 Navigation")
    selected_page = st.radio(
        "Go to page:",
        options=["🏠 Home", "🏛 Jurisdiction Navigator"],
        key="app_navigation"
    )
    st.markdown("---")

# ============================================================================
# PAGE ROUTING
# ============================================================================

if selected_page == "🏛 Jurisdiction Navigator":
    render_jurisdiction_navigator_page()

else: # 🏠 Home Page
    # Header & Trust Badges
    render_brand_header()
    render_trust_bar()

    # Information Scope Card
    render_information_scope_card()

    # Main Interface Container
    st.markdown("### Ask NyayaPath")
    render_privacy_notice()

    user_query = st.text_area(
        "Enter your question about court procedures, case stages, or legal terminology:",
        height=100,
        placeholder="Example: What are the typical stages of a civil court case?",
        key="user_input"
    )

    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        submit_button = st.button("Explain Procedure", type="primary", use_container_width=True)

    # Multi-Layer Safety Evaluation & Processing
    if submit_button and user_query:
        decision = evaluate_query(user_query)
        
        if not decision.allowed:
            # Display styled safe refusal card
            st.markdown(f"""
                <div class="np-refusal-card">
                    <div class="np-refusal-title">Information Scope Notice</div>
                    <div class="np-refusal-text">{decision.refusal_message}</div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("""
                <div class="np-tip-card">
                    💡 <strong>Educational Guidance:</strong> Try rephrasing your question to focus on general court processes (e.g. <em>"What happens during an evidence stage?"</em> or <em>"What is a court summons?"</em>).
                </div>
            """, unsafe_allow_html=True)
        else:
            with st.spinner("Understanding your question and generating educational explanation..."):
                ai_response = get_ai_response(user_query, decision)
                
                if ai_response.success:
                    # Structured Knowledge Article Container
                    st.markdown("---")
                    st.markdown(f"""
                        <div class="np-article-card">
                            <div class="np-article-header">
                                <span class="np-article-category">NyayaPath Educational Explanation</span>
                                <span class="np-article-transparency">🛡️ AI-Assisted Educational Content</span>
                            </div>
                            <div class="np-article-body">{ai_response.text}</div>
                        </div>
                    """, unsafe_allow_html=True)
                    st.caption(f"💡 Reference ID: {ai_response.request_id} | Educational legal information only.")
                else:
                    st.markdown(f"""
                        <div class="np-refusal-card">
                            <div class="np-refusal-title">System Message</div>
                            <div class="np-refusal-text">{ai_response.text}</div>
                        </div>
                    """, unsafe_allow_html=True)

    elif submit_button and not user_query:
        st.warning("Please enter a question before clicking 'Explain Procedure'.")

    # Feature Discovery Banner for Jurisdiction Navigator
    st.markdown("""
        <div class="np-discovery-card">
            <div>
                <div class="np-discovery-title">🏛 Want Context for a Specific State or Court?</div>
                <div class="np-discovery-text">Explore court processes tailored to your selected state, court level, and legal domain.</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ============================================================================
# SIDEBAR SHARED FOOTER & EXAMPLES
# ============================================================================

with st.sidebar:
    if selected_page == "🏠 Home":
        st.markdown("### 💡 Educational Examples")
        st.markdown("""
            **About Procedures:**
            - What are the stages of a civil court case?
            - How does a criminal trial proceed?
            - What happens during an appeal?
            
            **About Terminology:**
            - What does "plaintiff" mean?
            - What is a "motion" in court?
            - What does "burden of proof" mean?
            
            **About Case Flow:**
            - What happens after filing a lawsuit?
            - What is the discovery process?
            - What is the general purpose of a summons?
        """)
        st.markdown("---")

    st.markdown("### 🚫 Unsafe Query Scope")
    st.markdown("""
        - Personalized legal advice
        - Tactical legal strategy to win
        - Outcome or probability predictions
        - Personalized law interpretations
        - Custom legal document generation
    """)

# Footer
render_footer()
