"""
Apple-Grade Premium Design System for NyayaPath.
Provides explicit light-theme contrast rules, crisp typography, custom pill buttons,
and full dark-mode override for Streamlit widgets.
"""

import streamlit as st


def inject_custom_css():
    """
    Inject custom CSS to guarantee 100% text contrast, Apple styling,
    and prevent Streamlit dark-mode text masking.
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
                --apple-text-secondary: #515154;
                --apple-text-tertiary: #86868B;
                --apple-blue: #0071E3;
                --apple-blue-hover: #0077ED;
                --apple-blue-light: rgba(0, 113, 227, 0.08);
                --apple-emerald: #34C759;
                --apple-border: rgba(0, 0, 0, 0.08);
                --apple-border-strong: #D2D2D7;
                --apple-radius-sm: 10px;
                --apple-radius-md: 14px;
                --apple-radius-lg: 20px;
                --apple-radius-pill: 9999px;
                --apple-shadow-subtle: 0 2px 12px rgba(0, 0, 0, 0.03);
                --apple-shadow-card: 0 4px 20px rgba(0, 0, 0, 0.04);
                --apple-shadow-hover: 0 12px 32px rgba(0, 0, 0, 0.08);
            }

            /* ==========================================================================
               GLOBAL THEME OVERRIDES (Guarantees Contrast in Dark & Light Modes)
               ========================================================================== */
            .stApp, [data-testid="stAppViewContainer"], .main, .main .block-container {
                background-color: var(--apple-bg) !important;
                color: var(--apple-text-primary) !important;
                font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
                -webkit-font-smoothing: antialiased;
            }

            /* Clean up Streamlit Header & Navigation */
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

            /* Container Max-Width */
            .main .block-container {
                max-width: 840px !important;
                padding-top: 1.5rem !important;
                padding-bottom: 5rem !important;
            }

            /* ==========================================================================
               TEXT & WIDGET LABELS CONTRAST FIX
               ========================================================================== */
            /* Textarea Label & Placeholder */
            .stTextArea label, div[data-testid="stWidgetLabel"] label, div[data-testid="stWidgetLabel"] p {
                color: var(--apple-text-primary) !important;
                font-size: 0.925rem !important;
                font-weight: 600 !important;
                opacity: 1 !important;
            }

            .stTextArea textarea {
                background-color: #FFFFFF !important;
                color: var(--apple-text-primary) !important;
                border: 1.5px solid var(--apple-border-strong) !important;
                border-radius: var(--apple-radius-md) !important;
                font-size: 0.95rem !important;
                padding: 0.85rem 1rem !important;
                line-height: 1.5 !important;
                box-shadow: var(--apple-shadow-subtle) !important;
            }
            .stTextArea textarea:focus {
                border-color: var(--apple-blue) !important;
                box-shadow: 0 0 0 4px var(--apple-blue-light) !important;
            }
            .stTextArea textarea::placeholder {
                color: #86868B !important;
                opacity: 1 !important;
            }

            /* Selectbox Label & Value */
            .stSelectbox label, .stSelectbox label p {
                color: var(--apple-text-primary) !important;
                font-weight: 600 !important;
                opacity: 1 !important;
            }
            div[data-baseweb="select"] > div {
                background-color: #FFFFFF !important;
                border-color: var(--apple-border-strong) !important;
                border-radius: var(--apple-radius-md) !important;
                color: var(--apple-text-primary) !important;
            }
            div[data-baseweb="select"] * {
                color: var(--apple-text-primary) !important;
            }

            /* ==========================================================================
               HERO BRAND & HEADERS
               ========================================================================== */
            .apple-hero-container {
                text-align: center;
                margin-bottom: 2rem;
                padding: 0.5rem 0;
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
                margin-bottom: 0.85rem;
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
                margin-bottom: 0.6rem;
            }
            .apple-hero-title span.blue-accent {
                color: var(--apple-blue);
            }
            .apple-hero-subtitle {
                font-size: 1.05rem;
                font-weight: 400;
                color: var(--apple-text-secondary);
                max-width: 580px;
                margin: 0 auto;
                line-height: 1.5;
            }

            /* ==========================================================================
               TRUST BADGES ROW
               ========================================================================== */
            .apple-trust-row {
                display: flex;
                justify-content: center;
                gap: 0.65rem;
                flex-wrap: wrap;
                margin-top: 1.35rem;
                margin-bottom: 1.75rem;
            }
            .apple-trust-pill {
                display: inline-flex;
                align-items: center;
                gap: 0.4rem;
                background: #FFFFFF;
                border: 1px solid var(--apple-border);
                border-radius: var(--apple-radius-pill);
                padding: 0.4rem 0.9rem;
                font-size: 0.825rem;
                font-weight: 600;
                color: var(--apple-text-primary);
                box-shadow: var(--apple-shadow-subtle);
            }

            /* ==========================================================================
               CARDS & SCOPE TRANSPARENCY
               ========================================================================== */
            .apple-card {
                background-color: #FFFFFF;
                border: 1px solid var(--apple-border);
                border-radius: var(--apple-radius-lg);
                padding: 1.4rem 1.6rem;
                margin-bottom: 1.75rem;
                box-shadow: var(--apple-shadow-card);
            }
            .apple-card-title {
                font-size: 1rem;
                font-weight: 700;
                color: var(--apple-text-primary);
                display: flex;
                align-items: center;
                gap: 0.5rem;
                margin-bottom: 0.4rem;
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
                margin-top: 0.9rem;
                padding-top: 0.9rem;
                border-top: 1px solid rgba(0, 0, 0, 0.06);
            }
            .apple-grid-item {
                font-size: 0.825rem;
                color: var(--apple-text-primary);
                line-height: 1.5;
            }

            /* Privacy Shield */
            .apple-privacy-notice {
                background: rgba(52, 199, 89, 0.08);
                border: 1px solid rgba(52, 199, 89, 0.25);
                border-radius: var(--apple-radius-md);
                padding: 0.65rem 1rem;
                font-size: 0.825rem;
                color: #14532D;
                margin-bottom: 1.25rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }

            /* Article Container */
            .apple-article-card {
                background: #FFFFFF;
                border: 1px solid var(--apple-border);
                border-radius: var(--apple-radius-lg);
                padding: 1.85rem;
                margin-top: 1.5rem;
                margin-bottom: 1.75rem;
                box-shadow: var(--apple-shadow-hover);
            }
            .apple-article-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding-bottom: 0.9rem;
                margin-bottom: 1.25rem;
                border-bottom: 1px solid var(--apple-border);
                flex-wrap: wrap;
                gap: 0.5rem;
            }
            .apple-category-badge {
                background: var(--apple-blue-light);
                color: var(--apple-blue);
                border: 1px solid rgba(0, 113, 227, 0.18);
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
                font-size: 1.15rem;
                font-weight: 700;
                color: var(--apple-text-primary);
                margin-top: 1.4rem;
                margin-bottom: 0.5rem;
            }

            /* Safety Refusal & Tip Cards */
            .apple-refusal-card {
                background: rgba(255, 59, 48, 0.06);
                border: 1px solid rgba(255, 59, 48, 0.2);
                border-radius: var(--apple-radius-md);
                padding: 1.2rem 1.4rem;
                margin-top: 1.25rem;
                margin-bottom: 1.25rem;
            }
            .apple-refusal-title {
                font-size: 0.95rem;
                font-weight: 700;
                color: #DC2626;
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
                background: #FFFFFF;
                border: 1px solid var(--apple-border);
                border-left: 4px solid var(--apple-blue);
                border-radius: var(--apple-radius-md);
                padding: 1rem 1.2rem;
                font-size: 0.875rem;
                color: var(--apple-text-secondary);
                line-height: 1.55;
                margin-bottom: 1.5rem;
            }

            /* Step Cards (Jurisdiction Navigator) */
            .apple-step-card {
                background: #FFFFFF;
                border: 1px solid var(--apple-border);
                border-radius: var(--apple-radius-md);
                padding: 1.1rem 1.35rem;
                margin-bottom: 1rem;
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
                background: #FFFFFF;
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
                color: #FFFFFF !alignment;
                box-shadow: var(--apple-shadow-card);
            }
            .apple-discovery-title {
                font-size: 1.15rem;
                font-weight: 700;
                color: #FFFFFF !important;
                margin-bottom: 0.35rem;
                letter-spacing: -0.02em;
            }
            .apple-discovery-text {
                font-size: 0.9rem;
                color: rgba(255, 255, 255, 0.9) !important;
                line-height: 1.5;
            }

            /* ==========================================================================
               SIDEBAR & RADIO NAVIGATION CONTRAST FIX
               ========================================================================== */
            section[data-testid="stSidebar"] {
                background-color: var(--apple-sidebar-bg) !important;
                border-right: 1px solid var(--apple-border) !important;
            }
            section[data-testid="stSidebar"] .block-container {
                padding-top: 1.5rem !important;
            }
            section[data-testid="stSidebar"] * {
                color: var(--apple-text-primary) !important;
            }

            /* Radio Buttons Fix: Visible, Crisp Text & Apple Pill Layout */
            div[data-testid="stRadio"] div[role="radiogroup"] {
                gap: 0.4rem !important;
                display: flex !important;
                flex-direction: column !important;
            }
            div[data-testid="stRadio"] div[role="radiogroup"] label {
                display: flex !important;
                align-items: center !important;
                gap: 0.5rem !important;
                background: #FFFFFF !important;
                border: 1px solid var(--apple-border-strong) !important;
                border-radius: var(--apple-radius-md) !important;
                padding: 0.6rem 0.9rem !important;
                font-size: 0.9rem !important;
                font-weight: 600 !important;
                color: var(--apple-text-primary) !important;
                cursor: pointer !important;
                transition: all 0.2s ease !important;
                box-shadow: var(--apple-shadow-subtle) !important;
            }
            div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
                border-color: var(--apple-blue) !important;
                background: #F0F7FF !important;
                color: var(--apple-blue) !important;
            }
            div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"],
            div[data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) {
                background: var(--apple-blue) !important;
                border-color: var(--apple-blue) !important;
                color: #FFFFFF !important;
                box-shadow: 0 3px 10px rgba(0, 113, 227, 0.3) !important;
            }
            div[data-testid="stRadio"] div[role="radiogroup"] label * {
                color: inherit !important;
                font-size: 0.9rem !important;
                font-weight: 600 !important;
            }

            /* Sidebar Expanders Fix: Clear Dark Text on Clean White Cards */
            div[data-testid="stExpander"] {
                background-color: #FFFFFF !important;
                border: 1px solid var(--apple-border-strong) !important;
                border-radius: var(--apple-radius-md) !important;
                box-shadow: var(--apple-shadow-subtle) !important;
                margin-bottom: 0.6rem !important;
                overflow: hidden !important;
            }
            div[data-testid="stExpander"] details summary {
                background-color: #F5F5F7 !important;
                border-bottom: 1px solid var(--apple-border) !important;
                padding: 0.65rem 0.85rem !important;
            }
            div[data-testid="stExpander"] details summary * {
                color: var(--apple-text-primary) !important;
                font-weight: 600 !important;
                font-size: 0.875rem !important;
            }

            div[data-testid="stExpander"] div[data-testid="stExpanderDetails"] {
                background-color: #FFFFFF !important;
                padding: 0.75rem 0.85rem !important;
            }
            div[data-testid="stExpander"] div[data-testid="stExpanderDetails"] * {
                color: #2C2C2E !important;
                font-size: 0.85rem !important;
                line-height: 1.5 !important;
            }

            /* ==========================================================================
               BUTTONS (Primary & Secondary)
               ========================================================================== */
            /* Primary Action Button */
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

            /* Secondary Action Button */
            div.stButton > button:not([kind="primary"]) {
                background: #FFFFFF !important;
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
            }

            /* Engine Status Widget */
            .apple-sidebar-status {
                background: #FFFFFF;
                border: 1px solid var(--apple-border-strong);
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
                color: var(--apple-text-secondary) !important;
            }
            .apple-status-row:last-child {
                margin-bottom: 0;
            }
            .apple-status-val {
                font-weight: 600;
                color: var(--apple-emerald) !important;
            }

            /* Footer */
            .apple-footer {
                text-align: center;
                border-top: 1px solid var(--apple-border);
                padding-top: 2rem;
                margin-top: 4rem;
                font-size: 0.825rem;
                color: var(--apple-text-tertiary) !important;
            }
            .apple-footer-title {
                font-weight: 700;
                color: var(--apple-text-primary) !important;
                font-size: 0.95rem;
                margin-bottom: 0.35rem;
            }
            .apple-footer-text {
                font-size: 0.775rem;
                color: var(--apple-text-secondary) !important;
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
