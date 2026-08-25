"""
Streamlit Page Component for 🏛 Jurisdiction Navigator with Apple Design Aesthetic.
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
        f"{JURISDICTION_PREFIX}state": "-- Select State / UT --",
        f"{JURISDICTION_PREFIX}court": "-- Select Court Level --",
        f"{JURISDICTION_PREFIX}domain": "-- Select Legal Domain --",
        f"{JURISDICTION_PREFIX}question": "",
        f"{JURISDICTION_PREFIX}question_preset": "",
        f"{JURISDICTION_PREFIX}response": None,
        f"{JURISDICTION_PREFIX}decision": None,
        f"{JURISDICTION_PREFIX}context": None,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val


def reset_jurisdiction_state():
    """Reset Jurisdiction Navigator session state."""
    st.session_state[f"{JURISDICTION_PREFIX}state"] = "-- Select State / UT --"
    st.session_state[f"{JURISDICTION_PREFIX}court"] = "-- Select Court Level --"
    st.session_state[f"{JURISDICTION_PREFIX}domain"] = "-- Select Legal Domain --"
    st.session_state[f"{JURISDICTION_PREFIX}question"] = ""
    st.session_state[f"{JURISDICTION_PREFIX}question_preset"] = ""
    st.session_state[f"{JURISDICTION_PREFIX}response"] = None
    st.session_state[f"{JURISDICTION_PREFIX}decision"] = None
    st.session_state[f"{JURISDICTION_PREFIX}context"] = None
    st.rerun()


def render_jurisdiction_navigator_page():
    """Render the 🏛 Jurisdiction Navigator page view with Apple-style progressive step-cards."""
    inject_custom_css()
    init_jurisdiction_session_state()

    # Apple Keynote Header
    st.markdown("""
        <div class="apple-hero-container">
            <div class="apple-pill-badge">
                <span class="apple-pulse-dot"></span>
                <span>Contextual Procedural Navigator</span>
            </div>
            <div class="apple-hero-title">
                Jurisdiction Navigator<span class="blue-accent">.</span>
            </div>
            <div class="apple-hero-subtitle">
                Explore court workflows and legal stages tailored to your selected country, state, court tier, and legal domain.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Scope Notice Card
    st.markdown("""
        <div class="apple-card">
            <div class="apple-card-title">
                <span>📍</span> Jurisdiction Scope & Local Practice Directions
            </div>
            <p class="apple-card-desc">
                Procedures vary across High Courts and subordinate judicial districts. 
                NyayaPath delivers plain-language educational breakdowns based on general statutory rules.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Step 1 Card: Jurisdiction
    st.markdown("""
        <div class="apple-step-card">
            <div class="apple-step-header">
                <span class="apple-step-badge">1</span>
                <span>Select Region & Country</span>
            </div>
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
        <div class="apple-step-card">
            <div class="apple-step-header">
                <span class="apple-step-badge">2</span>
                <span>Select Court Tier & Legal Domain</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_cl, col_ld = st.columns(2)
    with col_cl:
        court_levels = ["-- Select Court Level --"] + get_court_levels_for_country(selected_country)
        selected_court = st.selectbox(
            "Court Level / Tier",
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

    # Apple-style Dynamic Context Pills
    state_disp = selected_state if selected_state != "-- Select State / UT --" else "State: Any"
    court_disp = selected_court if selected_court != "-- Select Court Level --" else "Court: Any"
    domain_disp = selected_domain if selected_domain != "-- Select Legal Domain --" else "Domain: Any"

    st.markdown(f"""
        <div class="apple-breadcrumb-bar">
            <span><strong>Context:</strong></span>
            <span class="apple-breadcrumb-tag">🌐 {selected_country}</span>
            <span>›</span>
            <span class="apple-breadcrumb-tag">📍 {state_disp}</span>
            <span>›</span>
            <span class="apple-breadcrumb-tag">🏛️ {court_disp}</span>
            <span>›</span>
            <span class="apple-breadcrumb-tag">⚖️ {domain_disp}</span>
        </div>
    """, unsafe_allow_html=True)

    # Step 3 Card: Question
    st.markdown("""
        <div class="apple-step-card">
            <div class="apple-step-header">
                <span class="apple-step-badge">3</span>
                <span>Enter Your Question</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Quick procedural question templates
    col_q1, col_q2, col_q3 = st.columns(3)
    with col_q1:
        if st.button("📝 Filing Stages Breakdown", use_container_width=True, key="preset_filing"):
            st.session_state[f"{JURISDICTION_PREFIX}question_preset"] = "What are the typical stages from initial filing to hearing in this court?"
            st.rerun()
    with col_q2:
        if st.button("📜 Writ Petition Process", use_container_width=True, key="preset_writ"):
            st.session_state[f"{JURISDICTION_PREFIX}question_preset"] = "What is the procedure for filing and listing a writ petition in the High Court?"
            st.rerun()
    with col_q3:
        if st.button("⚖️ Interim Injunction Flow", use_container_width=True, key="preset_injunction"):
            st.session_state[f"{JURISDICTION_PREFIX}question_preset"] = "What are the standard procedural steps for an application seeking interim injunction relief?"
            st.rerun()

    render_privacy_notice()

    preset_text = st.session_state.get(f"{JURISDICTION_PREFIX}question_preset", "")
    question_input = st.text_area(
        "What would you like to understand about court procedures in this jurisdiction?",
        value=preset_text,
        height=110,
        placeholder="e.g. What generally happens after a civil suit is filed in the District Court?",
        key=f"{JURISDICTION_PREFIX}input_question"
    )

    # Action Buttons (Submit & Reset)
    col_btn1, col_btn2, col_btn3 = st.columns([2, 1.2, 1])
    with col_btn1:
        submit_btn = st.button("Explain Jurisdiction Process", type="primary", use_container_width=True)
    with col_btn3:
        reset_btn = st.button("Reset All", use_container_width=True)

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

        with st.spinner("Analyzing jurisdiction rules and generating explanation..."):
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
                    💡 <strong>Educational Guidance:</strong> Rephrase your question to focus on general court processes (e.g. <em>"What are the typical stages of a civil lawsuit in District Courts?"</em>).
                </div>
            """, unsafe_allow_html=True)
        elif ai_resp.success:
            st.markdown("---")
            st.markdown(f"""
                <div class="apple-card">
                    <div class="apple-card-title">
                        <span>📍</span> Jurisdiction Context Verified
                    </div>
                    <div class="apple-card-desc">
                        <strong>Country:</strong> {context.country} &nbsp;|&nbsp; 
                        <strong>State/UT:</strong> {context.state} &nbsp;|&nbsp; 
                        <strong>Court Tier:</strong> {context.court_level} &nbsp;|&nbsp; 
                        <strong>Domain:</strong> {context.legal_domain}
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Structured Knowledge Article
            st.markdown(f"""
                <div class="apple-article-card">
                    <div class="apple-article-header">
                        <span class="apple-category-badge">{context.court_level} • {context.legal_domain}</span>
                        <span style="font-size: 0.8rem; color: #86868B;">📍 {context.state}, {context.country}</span>
                    </div>
                    <div class="apple-article-body">{ai_resp.text}</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
                <div class="apple-tip-card">
                    <strong>ℹ️ Official Verification Notice:</strong><br>
                    This explanation provides general educational guidance based on standard rules in {context.state}, {context.country}. 
                    Local court circulars and roster designations may vary. Always verify listing details through official court registries (e.g. <em>eCourts Services India</em>) or consult an enrolled attorney.
                </div>
            """, unsafe_allow_html=True)
            st.caption(f"💡 Reference ID: `{ai_resp.request_id}` | Educational information only.")
        else:
            st.markdown(f"""
                <div class="apple-refusal-card">
                    <div class="apple-refusal-title">
                        <span>⚠️</span>
                        <span>System Message</span>
                    </div>
                    <div class="apple-refusal-text">{ai_resp.text}</div>
                </div>
            """, unsafe_allow_html=True)
