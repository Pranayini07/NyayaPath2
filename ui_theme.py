"""
Apple-Grade Premium Design System for NyayaPath.
Delivers a clean, elegant, minimalist Apple aesthetic with frosted glass elements,
unified color hierarchy, precise micro-interactions, and high-legibility typography.
"""

import streamlit as st


def inject_custom_css():
    """
    Inject Apple-style CSS variables, glassmorphic card layouts, crisp typography,
    and Streamlit dark-mode overrides for an ultra-premium experience.
    """
    st.markdown("""
        <style>
            /* Import Apple SF Pro-like Clean Google Fonts */
            @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700;800&display=swap');

            :root {
                --apple-bg: #F5F5F7;
                --apple-card-bg: #FFFFFF;
                --apple-sidebar-bg: #FAFAFC;
                --apple-text-primary: #1D1D1F;
                --apple-text-secondary: #6E6E73;
                --apple-text-tertiary: #86868B;
                --apple-blue: #0071E3;
                --apple-blue-hover: #0077ED;
                --apple-blue-light: rgba(0, 113, 227, 0.08);
                --apple-emerald: #34C759;
                --apple-emerald-light: rgba(52, 199, 89, 0.1);
                --apple-gold: #FF9500;
                --apple-gold-light: rgba(255, 149, 0, 0.1);
                --apple-red: #FF3B30;
                --apple-red-light: rgba(255, 59, 48, 0.08);
                --apple-border: rgba(0, 0, 0, 0.08);
                --apple-border-strong: #D2D2D7;
                --apple-radius-sm: 10px;
                --apple-radius-md: 14px;
                --apple-radius-lg: 20px;
                --apple-radius-pill: 9999px;
                --apple-shadow-subtle: 0 2px 12px rgba(0, 0, 0, 0.03), 0 1px 3px rgba(0, 0, 0, 0.02);
                --apple-shadow-card: 0 4px 20px rgba(0, 0, 0, 0.04), 0 1px 3px rgba(0, 0, 0, 0.02);
                --apple-shadow-hover: 0 12px 32px rgba(0, 0, 0, 0.08), 0 2px 6px rgba(0, 0, 0, 0.04);
            }

            /* Force Apple Neutral Background on Entire App (Overrides Streamlit Dark Mode conflict) */
            .stApp, [data-testid="stAppViewContainer"], .main {
                background-color: var(--apple-bg) !important;
                color: var(--apple-text-primary) !important;
                font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, sans-serif !important;
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale;
            }

            /* Clean up Streamlit Header & Multipage Navigation */
            header[data-testid="stHeader"] {
                background: transparent !important;
                box-shadow: none !important;
            }
            div[data-testid="stSidebarNav"] {
                display: none !important;
            }
            .stDeployButton {
                display: none !important;
            }

            /* Main Content Container Alignment */
            .main .block-container {
                max-width: 840px !important;
                padding-top: 2rem !important;
                padding-bottom: 5rem !important;
            }

            /* ==========================================================================
               HERO & BRAND SECTION (Apple Keynote Minimalism)
               ========================================================================== */
            .apple-hero-container {
                text-align: center;
                margin-bottom: 2.25rem;
                padding: 1rem 0 0.5rem 0;
            }
            .apple-pill-badge {
                display: inline-flex;
                align-items: center;
                gap: 0.45rem;
                background-color: var(--apple-blue-light);
                border: 1px solid rgba(0, 113, 227, 0.18);
                border-radius: var(--apple-radius-pill);
                padding: 0.35rem 0.95rem;
                font-size: 0.775rem;
                font-weight: 600;
                color: var(--apple-blue);
                letter-spacing: 0.03em;
                text-transform: uppercase;
                margin-bottom: 1rem;
            }
            .apple-pulse-dot {
                width: 6px;
                height: 6px;
                background-color: var(--apple-emerald);
                border-radius: 50%;
                box-shadow: 0 0 0 3px rgba(52, 199, 89, 0.2);
            }

            .apple-hero-title {
                font-size: 2.75rem;
                font-weight: 800;
                color: var(--apple-text-primary);
                letter-spacing: -0.03em;
                line-height: 1.1;
                margin-bottom: 0.65rem;
            }
            .apple-hero-title span.blue-accent {
                background: linear-gradient(135deg, #1D1D1F 30%, #0071E3 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .apple-hero-subtitle {
                font-size: 1.1rem;
                font-weight: 400;
                color: var(--apple-text-secondary);
                max-width: 580px;
                margin: 0 auto;
                line-height: 1.5;
                letter-spacing: -0.01em;
            }

            /* ==========================================================================
               TRUST BADGES (Apple Pill Style)
               ========================================================================== */
            .apple-trust-row {
                display: flex;
                justify-content: center;
                gap: 0.65rem;
                flex-wrap: wrap;
                margin-top: 1.5rem;
                margin-bottom: 2rem;
            }
            .apple-trust-pill {
                display: inline-flex;
                align-items: center;
                gap: 0.4rem;
                background: var(--apple-card-bg);
                border: 1px solid var(--apple-border);
                border-radius: var(--apple-radius-pill);
                padding: 0.4rem 0.9rem;
                font-size: 0.825rem;
                font-weight: 500;
                color: var(--apple-text-primary);
                box-shadow: var(--apple-shadow-subtle);
                transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
            }
            .apple-trust-pill:hover {
                border-color: var(--apple-blue);
                transform: translateY(-1px);
                box-shadow: var(--apple-shadow-card);
            }

            /* ==========================================================================
               CARDS & TRANSPARENCY CONTAINER
               ========================================================================== */
            .apple-card {
                background-color: var(--apple-card-bg);
                border: 1px solid var(--apple-border);
                border-radius: var(--apple-radius-lg);
                padding: 1.5rem 1.65rem;
                margin-bottom: 1.75rem;
                box-shadow: var(--apple-shadow-card);
                transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            }
            .apple-card:hover {
                box-shadow: var(--apple-shadow-hover);
                border-color: rgba(0, 0, 0, 0.12);
            }
            .apple-card-title {
                font-size: 1rem;
                font-weight: 700;
                color: var(--apple-text-primary);
                letter-spacing: -0.015em;
                display: flex;
                align-items: center;
                gap: 0.5rem;
                margin-bottom: 0.5rem;
            }
            .apple-card-desc {
                font-size: 0.9rem;
                color: var(--apple-text-secondary);
                line-height: 1.55;
                margin: 0;
            }

            .apple-grid-split {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 0.85rem;
                margin-top: 1rem;
                padding-top: 1rem;
                border-top: 1px solid rgba(0, 0, 0, 0.05);
            }
            .apple-grid-item {
                font-size: 0.825rem;
                color: var(--apple-text-primary);
                line-height: 1.5;
            }

            /* ==========================================================================
               PRIVACY SHIELD NOTICE
               ========================================================================== */
            .apple-privacy-notice {
                background: rgba(52, 199, 89, 0.06);
                border: 1px solid rgba(52, 199, 89, 0.2);
                border-radius: var(--apple-radius-md);
                padding: 0.65rem 1rem;
                font-size: 0.825rem;
                color: #15803D;
                margin-bottom: 1.25rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }

            /* ==========================================================================
               ARTICLE RESPONSE CARD
               ========================================================================== */
            .apple-article-card {
                background: var(--apple-card-bg);
                border: 1px solid var(--apple-border);
                border-radius: var(--apple-radius-lg);
                padding: 2rem;
                margin-top: 1.75rem;
                margin-bottom: 2rem;
                box-shadow: var(--apple-shadow-hover);
            }
            .apple-article-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding-bottom: 1rem;
                margin-bottom: 1.25rem;
                border-bottom: 1px solid var(--apple-border);
                flex-wrap: wrap;
                gap: 0.5rem;
            }
            .apple-category-badge {
                background: var(--apple-blue-light);
                color: var(--apple-blue);
                border: 1px solid rgba(0, 113, 227, 0.15);
                font-size: 0.775rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.04em;
                padding: 0.3rem 0.75rem;
                border-radius: var(--apple-radius-pill);
            }
            .apple-article-body {
                font-size: 1rem;
                line-height: 1.65;
                color: var(--apple-text-primary);
            }
            .apple-article-body h3 {
                font-size: 1.2rem;
                font-weight: 700;
                color: var(--apple-text-primary);
                letter-spacing: -0.02em;
                margin-top: 1.5rem;
                margin-bottom: 0.6rem;
            }

            /* ==========================================================================
               SAFETY REFUSAL & TIP CARDS
               ========================================================================== */
            .apple-refusal-card {
                background: var(--apple-red-light);
                border: 1px solid rgba(255, 59, 48, 0.2);
                border-radius: var(--apple-radius-md);
                padding: 1.25rem 1.4rem;
                margin-top: 1.25rem;
                margin-bottom: 1.25rem;
            }
            .apple-refusal-title {
                font-size: 0.95rem;
                font-weight: 700;
                color: var(--apple-red);
                margin-bottom: 0.35rem;
                display: flex;
                align-items: center;
                gap: 0.4rem;
            }
            .apple-refusal-text {
                font-size: 0.875rem;
                color: #991B1B;
                line-height: 1.55;
                margin: 0;
            }

            .apple-tip-card {
                background: var(--apple-card-bg);
                border: 1px solid var(--apple-border);
                border-left: 4px solid var(--apple-blue);
                border-radius: var(--apple-radius-md);
                padding: 1rem 1.2rem;
                font-size: 0.875rem;
                color: var(--apple-text-secondary);
                line-height: 1.55;
                margin-bottom: 1.5rem;
            }

            /* ==========================================================================
               STEP WIZARD CARDS (Jurisdiction Navigator)
               ========================================================================== */
            .apple-step-card {
                background: var(--apple-card-bg);
                border: 1px solid var(--apple-border);
                border-radius: var(--apple-radius-md);
                padding: 1.15rem 1.35rem;
                margin-bottom: 1.1rem;
                box-shadow: var(--apple-shadow-subtle);
            }
            .apple-step-header {
                font-size: 0.85rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.04em;
                color: var(--apple-text-primary);
                display: flex;
                align-items: center;
                gap: 0.55rem;
            }
            .apple-step-badge {
                background: var(--apple-text-primary);
                color: #FFFFFF;
                border-radius: 50%;
                width: 1.5rem;
                height: 1.5rem;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                font-size: 0.775rem;
                font-weight: 700;
            }

            /* Dynamic Breadcrumb Bar */
            .apple-breadcrumb-bar {
                background: var(--apple-card-bg);
                border: 1px solid var(--apple-border);
                border-radius: var(--apple-radius-md);
                padding: 0.85rem 1.2rem;
                margin-bottom: 1.35rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
                font-size: 0.85rem;
                color: var(--apple-text-primary);
                flex-wrap: wrap;
                box-shadow: var(--apple-shadow-subtle);
            }
            .apple-breadcrumb-tag {
                background: var(--apple-bg);
                border: 1px solid var(--apple-border-strong);
                border-radius: var(--apple-radius-pill);
                padding: 0.25rem 0.7rem;
                font-size: 0.8rem;
                font-weight: 600;
                color: var(--apple-text-primary);
            }

            /* Feature Banner */
            .apple-discovery-banner {
                background: linear-gradient(135deg, #1D1D1F 0%, #0071E3 100%);
                border-radius: var(--apple-radius-lg);
                padding: 1.6rem 1.8rem;
                margin-top: 2.25rem;
                margin-bottom: 1.5rem;
                color: #FFFFFF;
                box-shadow: var(--apple-shadow-card);
            }
            .apple-discovery-title {
                font-size: 1.15rem;
                font-weight: 700;
                color: #FFFFFF;
                margin-bottom: 0.35rem;
                letter-spacing: -0.02em;
            }
            .apple-discovery-text {
                font-size: 0.9rem;
                color: rgba(255, 255, 255, 0.85);
                line-height: 1.5;
            }

            /* ==========================================================================
               SIDEBAR (Apple Minimalist Sidebar)
               ========================================================================== */
            section[data-testid="stSidebar"] {
                background-color: var(--apple-sidebar-bg) !important;
                border-right: 1px solid var(--apple-border) !important;
            }
            section[data-testid="stSidebar"] .block-container {
                padding-top: 1.75rem !important;
            }

            /* Radio Buttons Clean Apple Pill Override */
            div[data-testid="stRadio"] > label {
                display: none !important;
            }
            div[data-testid="stRadio"] div[role="radiogroup"] {
                gap: 0.35rem !important;
            }
            div[data-testid="stRadio"] div[role="radiogroup"] label {
                background: transparent !important;
                border: 1px solid transparent !important;
                border-radius: var(--apple-radius-sm) !important;
                padding: 0.55rem 0.85rem !important;
                font-size: 0.9rem !important;
                font-weight: 600 !important;
                color: var(--apple-text-primary) !important;
                transition: all 0.2s ease !important;
                cursor: pointer !important;
                width: 100% !important;
            }
            div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
                background: rgba(0, 0, 0, 0.04) !important;
            }
            div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
                background: #FFFFFF !important;
                border-color: var(--apple-border) !important;
                color: var(--apple-blue) !important;
                box-shadow: var(--apple-shadow-subtle) !important;
            }

            /* Expander Containers in Sidebar */
            div[data-testid="stExpander"] {
                background-color: var(--apple-card-bg) !important;
                border: 1px solid var(--apple-border) !important;
                border-radius: var(--apple-radius-md) !important;
                box-shadow: var(--apple-shadow-subtle) !important;
                margin-bottom: 0.5rem !important;
            }
            div[data-testid="stExpander"] details summary span {
                font-size: 0.85rem !important;
                font-weight: 600 !important;
                color: var(--apple-text-primary) !important;
            }

            /* ==========================================================================
               STREAMLIT CONTROLS (BUTTONS, TEXTAREAS, SELECTBOXES)
               ========================================================================== */
            /* Primary Button (Apple Signature Blue Pill) */
            div.stButton > button[kind="primary"] {
                background: linear-gradient(180deg, #0077ED 0%, #0066CC 100%) !important;
                color: #FFFFFF !important;
                border: none !important;
                border-radius: var(--apple-radius-pill) !important;
                padding: 0.65rem 1.6rem !important;
                font-weight: 600 !important;
                font-size: 0.95rem !important;
                letter-spacing: -0.01em !important;
                box-shadow: 0 4px 14px rgba(0, 113, 227, 0.25) !important;
                transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
            }
            div.stButton > button[kind="primary"]:hover {
                transform: scale(1.015) !important;
                box-shadow: 0 6px 20px rgba(0, 113, 227, 0.35) !important;
            }
            div.stButton > button[kind="primary"]:active {
                transform: scale(0.98) !important;
            }

            /* Secondary Button */
            div.stButton > button:not([kind="primary"]) {
                background: var(--apple-card-bg) !important;
                color: var(--apple-text-primary) !important;
                border: 1px solid var(--apple-border-strong) !important;
                border-radius: var(--apple-radius-pill) !important;
                font-weight: 500 !important;
                font-size: 0.875rem !important;
                transition: all 0.2s ease !important;
                box-shadow: var(--apple-shadow-subtle) !important;
            }
            div.stButton > button:not([kind="primary"]):hover {
                background: var(--apple-bg) !important;
                border-color: var(--apple-blue) !important;
                color: var(--apple-blue) !important;
                transform: translateY(-1px) !important;
            }

            /* Textarea Input */
            .stTextArea textarea {
                background-color: var(--apple-card-bg) !important;
                color: var(--apple-text-primary) !important;
                border: 1px solid var(--apple-border-strong) !important;
                border-radius: var(--apple-radius-md) !important;
                font-size: 0.95rem !important;
                padding: 0.85rem 1rem !important;
                line-height: 1.5 !important;
                transition: all 0.2s ease !important;
            }
            .stTextArea textarea:focus {
                border-color: var(--apple-blue) !important;
                box-shadow: 0 0 0 4px var(--apple-blue-light) !important;
            }

            /* Selectbox Input */
            div[data-baseweb="select"] > div {
                background-color: var(--apple-card-bg) !important;
                border-color: var(--apple-border-strong) !important;
                border-radius: var(--apple-radius-md) !important;
                color: var(--apple-text-primary) !important;
            }

            /* Engine Status Card in Sidebar */
            .apple-sidebar-status {
                background: var(--apple-card-bg);
                border: 1px solid var(--apple-border);
                border-radius: var(--apple-radius-md);
                padding: 0.85rem 1rem;
                font-size: 0.8rem;
                box-shadow: var(--apple-shadow-subtle);
                margin-top: 1.5rem;
            }
            .apple-status-row {
                display: flex;
                align-items: center;
                justify-content: space-between;
                margin-bottom: 0.35rem;
                color: var(--apple-text-secondary);
            }
            .apple-status-row:last-child {
                margin-bottom: 0;
            }
            .apple-status-val {
                font-weight: 600;
                color: var(--apple-emerald);
            }

            /* Footer */
            .apple-footer {
                text-align: center;
                border-top: 1px solid var(--apple-border);
                padding-top: 2rem;
                margin-top: 4rem;
                font-size: 0.825rem;
                color: var(--apple-text-tertiary);
            }
            .apple-footer-title {
                font-weight: 700;
                color: var(--apple-text-primary);
                font-size: 0.95rem;
                margin-bottom: 0.35rem;
            }
            .apple-footer-text {
                font-size: 0.775rem;
                max-width: 580px;
                margin: 0.4rem auto 0 auto;
                line-height: 1.5;
            }
        </style>
    """, unsafe_allow_html=True)


def render_brand_header():
    """Render Apple-style minimalist hero header."""
    st.markdown("""
        <div class="apple-hero-container">
            <div class="apple-pill-badge">
                <span class="apple-pulse-dot"></span>
                <span>Civic Legal Knowledge Platform</span>
            </div>
            <div class="apple-hero-title">
                NyayaPath<span class="blue-accent">.</span>
            </div>
            <div class="apple-hero-subtitle">
                Accessible, plain-language judicial court process education and procedural guidance for every citizen.
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_trust_bar():
    """Render Apple-style trust pills row."""
    st.markdown("""
        <div class="apple-trust-row">
            <div class="apple-trust-pill">
                <span>📖</span> Plain Language
            </div>
            <div class="apple-trust-pill">
                <span>🔒</span> Zero Data Retention
            </div>
            <div class="apple-trust-pill">
                <span>🛡️</span> Active Safety Engine
            </div>
            <div class="apple-trust-pill">
                <span>🏛️</span> Jurisdiction-Aware
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_information_scope_card():
    """Render Apple-style clean card with scope transparency."""
    st.markdown("""
        <div class="apple-card">
            <div class="apple-card-title">
                <span>ⓘ</span> Educational Purpose & Scope Transparency
            </div>
            <p class="apple-card-desc">
                NyayaPath provides neutral educational information to help citizens understand legal processes, terminology, and typical court stages.
            </p>
            <div class="apple-grid-split">
                <div class="apple-grid-item">
                    ✅ <strong>What it provides:</strong> General procedural breakdowns, document functions, and case flow explanations.
                </div>
                <div class="apple-grid-item">
                    🚫 <strong>What it avoids:</strong> Personalized legal counsel, case strategy, outcome predictions, or formal representation.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_privacy_notice():
    """Render Apple privacy shield badge."""
    st.markdown("""
        <div class="apple-privacy-notice">
            <span>🔒</span>
            <span><strong>Privacy Shield:</strong> Never enter sensitive personal identifiers (SSN/Aadhaar), bank details, or private case numbers.</span>
        </div>
    """, unsafe_allow_html=True)


def render_footer():
    """Render Apple minimal civic footer."""
    st.markdown("""
        <div class="apple-footer">
            <div class="apple-footer-title">
                NyayaPath — Public Legal Information Platform
            </div>
            <div>Educational Purpose • AI Safety-Engine Protected • eCourts Aligned</div>
            <div class="apple-footer-text">
                Disclaimer: NyayaPath provides educational information only and does not constitute formal legal counsel. 
                Always verify court procedures with official court registries or consult a licensed attorney. © 2026 NyayaPath.
            </div>
        </div>
    """, unsafe_allow_html=True)
