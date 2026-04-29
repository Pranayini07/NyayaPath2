"""
Judicial Court Process & Case Flow Explainer Bot

Main Streamlit application for the hackathon project.

This application provides a safe, educational interface for explaining:
- Judicial court procedures
- Case lifecycle stages
- Legal terminology

The system is designed to ONLY explain procedures and NEVER provide legal advice.
"""

import streamlit as st
from ai_handler import get_ai_response
from prompts import check_query_safety

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Judicial Court Process Explainer",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CUSTOM CSS FOR PROFESSIONAL APPEARANCE
# ============================================================================

st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            font-weight: bold;
            color: #1f4788;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        .sub-header {
            font-size: 1.1rem;
            color: #555;
            text-align: center;
            margin-bottom: 2rem;
        }
        .disclaimer-box {
            background-color: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 1rem;
            margin: 1.5rem 0;
            border-radius: 4px;
        }
        .response-box {
            background-color: #f8f9fa;
            border-left: 4px solid #1f4788;
            padding: 1.5rem;
            margin: 1rem 0;
            border-radius: 4px;
            min-height: 100px;
        }
        .error-box {
            background-color: #f8d7da;
            border-left: 4px solid #dc3545;
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 4px;
        }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# HEADER SECTION
# ============================================================================

st.markdown('<p class="main-header">⚖️ Judicial Court Process Explainer Bot</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-header">Learn about court procedures, case stages, and legal terminology in simple language</p>',
    unsafe_allow_html=True
)

# ============================================================================
# LEGAL DISCLAIMER (ALWAYS VISIBLE)
# ============================================================================

st.markdown("""
    <div class="disclaimer-box">
        <strong>⚠️ Important Disclaimer:</strong><br>
        This system is designed for educational purposes only. It explains general court procedures 
        and terminology but does NOT provide legal advice, interpret laws, predict outcomes, or 
        suggest actions. For legal guidance specific to your situation, please consult a qualified attorney.
    </div>
""", unsafe_allow_html=True)

# ============================================================================
# MAIN INTERFACE
# ============================================================================

# Input section
st.markdown("### Ask a Question")
user_query = st.text_area(
    "Enter your question about court procedures, case stages, or legal terminology:",
    height=100,
    placeholder="Example: What are the typical stages of a civil court case?",
    key="user_input"
)

# Submit button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    submit_button = st.button("Explain", type="primary", use_container_width=True)

# ============================================================================
# QUERY PROCESSING LOGIC
# ============================================================================

if submit_button and user_query:
    # Step 1: Safety pre-check (keyword-based guardrails)
    is_safe, refusal_message = check_query_safety(user_query)
    
    if not is_safe:
        # Block unsafe query - do NOT call AI
        st.markdown(f'<div class="error-box"><strong>Request Refused:</strong><br>{refusal_message}</div>', unsafe_allow_html=True)
        st.info("💡 **Tip:** Try asking about general procedures instead. For example: 'What are the stages of a court case?' or 'What does 'plaintiff' mean?'")
    else:
        # Step 2: Query passed safety check - proceed to AI
        with st.spinner("Processing your question..."):
            success, response = get_ai_response(user_query)
            
            if success:
                # Display AI response
                st.markdown("### Response")
                st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)
                
                # Additional reminder
                st.markdown("---")
                st.caption("💡 Remember: This explanation is for educational purposes only. For legal advice, consult a qualified attorney.")
            else:
                # Display error message
                st.markdown(f'<div class="error-box"><strong>Error:</strong><br>{response}</div>', unsafe_allow_html=True)

elif submit_button and not user_query:
    st.warning("Please enter a question before clicking 'Explain'.")

# ============================================================================
# SIDEBAR WITH EXAMPLE QUESTIONS
# ============================================================================

with st.sidebar:
    st.markdown("### 💡 Example Questions")
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
        - How long does a typical court case take?
    """)
    
    st.markdown("---")
    st.markdown("### 🚫 What I Cannot Do")
    st.markdown("""
        - Provide legal advice
        - Interpret laws or statutes
        - Predict case outcomes
        - Suggest strategies or actions
        - Generate legal documents
        - Analyze specific cases
    """)

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.caption("Built for public legal awareness and education | Hackathon Project 2024")

