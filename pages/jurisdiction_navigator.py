"""
Streamlit Page Component for 🏛 Jurisdiction Navigator with Civic Trust UI Design.
"""

import streamlit as st
from data.jurisdictions import (
    get_supported_countries,
    get_regions_for_country,
    get_court_levels_for_country,
    get_legal_domains
)
from services.jurisdiction_service import (
    JurisdictionContext,
    get_jurisdiction_response
)
from ui_theme import (
    inject_custom_css,
    render_privacy_notice
)

JURISDICTION_PREFIX = "jurisdiction_"


def init_jurisdiction_session_state():
    """Ensure all jurisdiction-specific session state keys exist without colliding with Home."""
    defaults = {
        f"{JURISDICTION_PREFIX}country": "India",
        f"{JURISDICTION_PREFIX}state": None,
        f"{JURISDICTION_PREFIX}court": None,
        f"{JURISDICTION_PREFIX}domain": None,
        f"{JURISDICTION_PREFIX}question": "",
        f"{JURISDICTION_PREFIX}response": None,
        f"{JURISDICTION_PREFIX}decision": None,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val


def reset_jurisdiction_state():
    """Reset Jurisdiction Navigator session state."""
    st.session_state[f"{JURISDICTION_PREFIX}state"] = None
    st.session_state[f"{JURISDICTION_PREFIX}court"] = None
    st.session_state[f"{JURISDICTION_PREFIX}domain"] = None
    st.session_state[f"{JURISDICTION_PREFIX}question"] = ""
    st.session_state[f"{JURISDICTION_PREFIX}response"] = None
    st.session_state[f"{JURISDICTION_PREFIX}decision"] = None
    st.rerun()


def render_jurisdiction_navigator_page():
    """Render the 🏛 Jurisdiction Navigator page view with progressive step-cards."""
    inject_custom_css()
    init_jurisdiction_session_state()

    # Header
    st.markdown("""
        <div class="np-brand-container">
            <div class="np-brand-title">🏛 Jurisdiction Navigator</div>
            <div class="np-brand-subtitle">Explore general court procedures tailored to your selected region and court level</div>
        </div>
    """, unsafe_allow_html=True)

    # Information Scope Notice
    st.markdown("""
        <div class="np-scope-card">
            <div class="np-scope-title">📍 Jurisdiction Context Scope</div>
            <p class="np-scope-text">
                Select your region, court level, and legal domain to receive structured educational guidance. 
                Procedures vary depending on local rules and matter specifics. NyayaPath does not provide legal advice or legal representation.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Step 1 Card: Jurisdiction
    st.markdown("""
        <div class="np-step-card">
            <div class="np-step-header"><span class="np-step-number">1</span> Select Jurisdiction & Region</div>
        </div>
    """, unsafe_allow_html=True)
    
    col_c, col_s = st.columns(2)
    with col_c:
        countries = get_supported_countries()
        selected_country = st.selectbox(
            "Country",
            options=countries,
            index=0,
            key=f"{JURISDICTION_PREFIX}select_country"
        )
        st.session_state[f"{JURISDICTION_PREFIX}country"] = selected_country

    with col_s:
        regions = ["-- Select State / UT --"] + get_regions_for_country(selected_country)
        selected_state = st.selectbox(
            "State / Union Territory",
            options=regions,
            index=0,
            key=f"{JURISDICTION_PREFIX}select_state"
        )

    # Step 2 Card: Court Level & Domain
    st.markdown("""
        <div class="np-step-card">
            <div class="np-step-header"><span class="np-step-number">2</span> Select Court Level & Legal Domain</div>
        </div>
    """, unsafe_allow_html=True)

    col_cl, col_ld = st.columns(2)
    with col_cl:
        court_levels = ["-- Select Court Level --"] + get_court_levels_for_country(selected_country)
        selected_court = st.selectbox(
            "Court Level",
            options=court_levels,
            index=0,
            key=f"{JURISDICTION_PREFIX}select_court"
        )

    with col_ld:
        domains = ["-- Select Legal Domain --"] + get_legal_domains()
        selected_domain = st.selectbox(
            "Legal Domain",
            options=domains,
            index=0,
            key=f"{JURISDICTION_PREFIX}select_domain"
        )

    # Step 3 Card: Question
    st.markdown("""
        <div class="np-step-card">
            <div class="np-step-header"><span class="np-step-number">3</span> Enter Your Question</div>
        </div>
    """, unsafe_allow_html=True)
    
    render_privacy_notice()
    question_input = st.text_area(
        "What would you like to understand about court procedures in this jurisdiction?",
        height=100,
        placeholder="e.g. What generally happens after a civil case is filed in this court?",
        key=f"{JURISDICTION_PREFIX}input_question"
    )

    # Action Buttons (Submit & Reset)
    col_btn1, col_btn2, col_btn3 = st.columns([2, 1.5, 1])
    with col_btn1:
        submit_btn = st.button("Explain Jurisdiction Process", type="primary", use_container_width=True)
    with col_btn3:
        reset_btn = st.button("↺ Start Over", use_container_width=True)

    if reset_btn:
        reset_jurisdiction_state()

    # Processing & Validation
    if submit_btn:
        if selected_state == "-- Select State / UT --":
            st.warning("Please select a State / Union Territory before continuing.")
            return
        if selected_court == "-- Select Court Level --":
            st.warning("Please select a Court Level before continuing.")
            return
        if selected_domain == "-- Select Legal Domain --":
            st.warning("Please select a Legal Domain before continuing.")
            return
        if not question_input or not question_input.strip():
            st.warning("Please enter your question before continuing.")
            return

        context = JurisdictionContext(
            country=selected_country,
            state=selected_state,
            court_level=selected_court,
            legal_domain=selected_domain
        )

        with st.spinner("Analyzing selected jurisdiction and retrieving educational explanation..."):
            decision, ai_resp = get_jurisdiction_response(question_input, context)
            st.session_state[f"{JURISDICTION_PREFIX}decision"] = decision
            st.session_state[f"{JURISDICTION_PREFIX}response"] = ai_resp
            st.session_state[f"{JURISDICTION_PREFIX}context"] = context

    # Render Results
    ai_resp = st.session_state.get(f"{JURISDICTION_PREFIX}response")
    decision = st.session_state.get(f"{JURISDICTION_PREFIX}decision")
    context = st.session_state.get(f"{JURISDICTION_PREFIX}context")

    if ai_resp and decision:
        if not decision.allowed:
            st.markdown(f"""
                <div class="np-refusal-card">
                    <div class="np-refusal-title">Information Scope Notice</div>
                    <div class="np-refusal-text">{decision.refusal_message}</div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("""
                <div class="np-tip-card">
                    💡 <strong>Educational Guidance:</strong> Rephrase your question to focus on general court processes (e.g. <em>"What are the typical stages of a civil lawsuit in District Courts?"</em>).
                </div>
            """, unsafe_allow_html=True)
        elif ai_resp.success:
            st.markdown("---")
            st.markdown(f"""
                <div class="np-scope-card">
                    <div class="np-scope-title">📍 Selected Jurisdiction Context</div>
                    <div class="np-scope-text">
                        <strong>Country:</strong> {context.country} &nbsp;|&nbsp; 
                        <strong>State/UT:</strong> {context.state} &nbsp;|&nbsp; 
                        <strong>Court Level:</strong> {context.court_level} &nbsp;|&nbsp; 
                        <strong>Legal Domain:</strong> {context.legal_domain}
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Structured Knowledge Article
            st.markdown(f"""
                <div class="np-article-card">
                    <div class="np-article-header">
                        <span class="np-article-category">Jurisdiction Educational Explanation</span>
                        <span class="np-article-transparency">📍 Context: {context.state}, {context.country}</span>
                    </div>
                    <div class="np-article-body">{ai_resp.text}</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
                <div class="np-tip-card">
                    <strong>ℹ️ Information Scope & Authoritative Sources:</strong><br>
                    This explanation provides general educational information based on the selected jurisdiction ({context.state}, {context.country}). 
                    Procedures can vary depending on specific local court rules, case facts, and judicial discretion. 
                    For authoritative information, verify details through official court portals (e.g. eCourts India) or consult a qualified advocate.
                </div>
            """, unsafe_allow_html=True)
            st.caption(f"💡 Reference ID: {ai_resp.request_id} | Educational legal information only.")
        else:
            st.markdown(f"""
                <div class="np-refusal-card">
                    <div class="np-refusal-title">System Message</div>
                    <div class="np-refusal-text">{ai_resp.text}</div>
                </div>
            """, unsafe_allow_html=True)
