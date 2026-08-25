"""
UI Theme and Design System for NyayaPath - Trusted Civic Technology Design.
Provides modern, accessible, clean, and attractive styling for public legal education.
"""

import streamlit as st


def inject_custom_css():
    """
    Inject custom CSS for institutional trust, modern aesthetic hierarchy,
    responsive card layouts, glassmorphism, and crisp readability.
    """
    st.markdown("""
        <style>
            /* Import Modern Clean Google Fonts */
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

            :root {
                --np-navy-900: #071526;
                --np-navy-800: #0F2942;
                --np-navy-700: #1B3B5F;
                --np-blue-600: #2563EB;
                --np-blue-500: #3B82F6;
                --np-blue-50: #EFF6FF;
                --np-gold-500: #F59E0B;
                --np-gold-600: #D97706;
                --np-emerald-500: #10B981;
                --np-emerald-50: #ECFDF5;
                --np-slate-900: #0F172A;
                --np-slate-800: #1E293B;
                --np-slate-700: #334155;
                --np-slate-600: #475569;
                --np-slate-500: #64748B;
                --np-slate-400: #94A3B8;
                --np-slate-200: #E2E8F0;
                --np-slate-100: #F1F5F9;
                --np-slate-50: #F8FAFC;
                --np-white: #FFFFFF;
                --np-radius-sm: 8px;
                --np-radius-md: 12px;
                --np-radius-lg: 16px;
                --np-radius-full: 9999px;
                --np-shadow-sm: 0 1px 3px rgba(0,0,0,0.05), 0 1px 2px rgba(0,0,0,0.03);
                --np-shadow-md: 0 4px 14px -2px rgba(15, 41, 66, 0.08), 0 2px 6px -1px rgba(15, 41, 66, 0.04);
                --np-shadow-lg: 0 10px 25px -3px rgba(15, 41, 66, 0.1), 0 4px 10px -2px rgba(15, 41, 66, 0.05);
            }

            /* Global Typography & Resets */
            html, body, [class*="css"], .stMarkdown {
                font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                color: var(--np-slate-800);
            }

            h1, h2, h3, h4, .np-brand-title, .np-heading {
                font-family: 'Outfit', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                letter-spacing: -0.015em;
            }

            /* Main Page Container & Spacing */
            .main .block-container {
                max-width: 860px;
                padding-top: 1.75rem;
                padding-bottom: 4rem;
            }

            /* Streamlit Top Header Bar & Default Multipage Nav Cleanup */
            header[data-testid="stHeader"] {
                background: transparent;
            }
            div[data-testid="stSidebarNav"] {
                display: none !important;
            }

            /* ==========================================================================
               HERO & BRAND HEADER
               ========================================================================== */
            .np-hero-container {
                text-align: center;
                margin-bottom: 2rem;
                padding: 1.5rem 1rem 0.5rem 1rem;
                position: relative;
            }
            .np-hero-badge {
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                background: linear-gradient(135deg, rgba(37, 99, 235, 0.08) 0%, rgba(15, 41, 66, 0.05) 100%);
                border: 1px solid rgba(37, 99, 235, 0.2);
                border-radius: var(--np-radius-full);
                padding: 0.35rem 1rem;
                font-size: 0.8rem;
                font-weight: 600;
                color: var(--np-blue-600);
                margin-bottom: 0.85rem;
                letter-spacing: 0.02em;
                text-transform: uppercase;
            }
            .np-pulse-dot {
                width: 7px;
                height: 7px;
                background-color: var(--np-emerald-500);
                border-radius: 50%;
                box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.25);
                display: inline-block;
                animation: npPulse 2s infinite;
            }
            @keyframes npPulse {
                0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.5); }
                70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
                100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
            }

            .np-brand-title {
                font-size: 2.5rem;
                font-weight: 800;
                color: var(--np-navy-900);
                line-height: 1.15;
                margin-bottom: 0.5rem;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 0.6rem;
            }
            .np-brand-title span.np-gold-text {
                background: linear-gradient(135deg, #0F2942 30%, #2563EB 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .np-brand-subtitle {
                font-size: 1.05rem;
                font-weight: 500;
                color: var(--np-slate-600);
                max-width: 620px;
                margin: 0 auto 1.25rem auto;
                line-height: 1.55;
            }

            /* ==========================================================================
               TRUST BADGES BAR
               ========================================================================== */
            .np-trust-bar {
                display: flex;
                justify-content: center;
                gap: 0.75rem;
                flex-wrap: wrap;
                margin-bottom: 1.75rem;
            }
            .np-trust-badge {
                display: inline-flex;
                align-items: center;
                gap: 0.45rem;
                background-color: var(--np-white);
                border: 1px solid var(--np-slate-200);
                border-radius: var(--np-radius-full);
                padding: 0.4rem 0.95rem;
                font-size: 0.825rem;
                font-weight: 600;
                color: var(--np-slate-700);
                box-shadow: var(--np-shadow-sm);
                transition: all 0.2s ease;
            }
            .np-trust-badge:hover {
                border-color: var(--np-blue-500);
                transform: translateY(-1px);
                box-shadow: var(--np-shadow-md);
            }
            .np-trust-badge-icon {
                font-size: 0.95rem;
            }

            /* ==========================================================================
               INFORMATION SCOPE & TRANSPARENCY CARD
               ========================================================================== */
            .np-scope-card {
                background: linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 100%);
                border: 1px solid var(--np-slate-200);
                border-left: 4px solid var(--np-navy-800);
                border-radius: var(--np-radius-md);
                padding: 1.25rem 1.4rem;
                margin-bottom: 1.75rem;
                box-shadow: var(--np-shadow-sm);
                transition: all 0.2s ease;
            }
            .np-scope-card:hover {
                box-shadow: var(--np-shadow-md);
            }
            .np-scope-header {
                display: flex;
                align-items: center;
                gap: 0.5rem;
                font-size: 0.95rem;
                font-weight: 700;
                color: var(--np-navy-800);
                margin-bottom: 0.5rem;
            }
            .np-scope-text {
                font-size: 0.875rem;
                color: var(--np-slate-600);
                line-height: 1.6;
                margin: 0;
            }
            .np-scope-pillars {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 0.75rem;
                margin-top: 0.85rem;
                padding-top: 0.85rem;
                border-top: 1px dashed var(--np-slate-200);
            }
            .np-pillar-item {
                font-size: 0.8rem;
                display: flex;
                align-items: flex-start;
                gap: 0.4rem;
                color: var(--np-slate-700);
            }
            .np-pillar-icon {
                flex-shrink: 0;
                margin-top: 0.1rem;
            }

            /* ==========================================================================
               INTERACTIVE QUICK PROMPT CHIPS
               ========================================================================== */
            .np-chips-container {
                margin-bottom: 1.25rem;
            }
            .np-chips-label {
                font-size: 0.8rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.04em;
                color: var(--np-slate-500);
                margin-bottom: 0.5rem;
                display: flex;
                align-items: center;
                gap: 0.35rem;
            }
            .np-chip-grid {
                display: flex;
                flex-wrap: wrap;
                gap: 0.5rem;
                margin-bottom: 0.5rem;
            }
            .np-topic-chip {
                background: var(--np-white);
                border: 1px solid var(--np-slate-200);
                border-radius: var(--np-radius-full);
                padding: 0.35rem 0.85rem;
                font-size: 0.825rem;
                font-weight: 500;
                color: var(--np-slate-700);
                box-shadow: 0 1px 2px rgba(0,0,0,0.03);
                transition: all 0.2s ease;
                display: inline-flex;
                align-items: center;
                gap: 0.35rem;
            }
            .np-topic-chip:hover {
                background-color: var(--np-blue-50);
                border-color: var(--np-blue-500);
                color: var(--np-blue-600);
                transform: translateY(-1px);
            }

            /* ==========================================================================
               PRIVACY & SECURITY REMINDER
               ========================================================================== */
            .np-privacy-box {
                background: linear-gradient(135deg, #F0FDF4 0%, #ECFDF5 100%);
                border: 1px solid #BBF7D0;
                border-radius: var(--np-radius-sm);
                padding: 0.65rem 0.95rem;
                font-size: 0.825rem;
                color: #166534;
                margin-top: 0.4rem;
                margin-bottom: 1.1rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
                box-shadow: 0 1px 2px rgba(22, 101, 52, 0.04);
            }

            /* ==========================================================================
               KNOWLEDGE ARTICLE & AI RESPONSE CARD
               ========================================================================== */
            .np-article-card {
                background-color: var(--np-white);
                border: 1px solid var(--np-slate-200);
                border-radius: var(--np-radius-lg);
                box-shadow: var(--np-shadow-md);
                padding: 1.85rem;
                margin-top: 1.5rem;
                margin-bottom: 1.75rem;
                transition: all 0.25s ease;
            }
            .np-article-card:hover {
                box-shadow: var(--np-shadow-lg);
            }
            .np-article-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid var(--np-slate-100);
                padding-bottom: 1rem;
                margin-bottom: 1.35rem;
                flex-wrap: wrap;
                gap: 0.5rem;
            }
            .np-article-category {
                font-size: 0.775rem;
                font-weight: 800;
                text-transform: uppercase;
                letter-spacing: 0.06em;
                color: var(--np-navy-800);
                background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
                padding: 0.35rem 0.75rem;
                border-radius: var(--np-radius-sm);
                border: 1px solid #BFDBFE;
            }
            .np-article-transparency {
                font-size: 0.8rem;
                font-weight: 500;
                color: var(--np-slate-500);
                display: flex;
                align-items: center;
                gap: 0.4rem;
                background-color: var(--np-slate-50);
                padding: 0.3rem 0.65rem;
                border-radius: var(--np-radius-full);
                border: 1px solid var(--np-slate-200);
            }
            .np-article-body {
                font-size: 1rem;
                line-height: 1.7;
                color: var(--np-slate-800);
            }
            .np-article-body h3 {
                color: var(--np-navy-800);
                font-size: 1.15rem;
                font-weight: 700;
                margin-top: 1.4rem;
                margin-bottom: 0.6rem;
                border-bottom: 1px solid var(--np-slate-100);
                padding-bottom: 0.35rem;
            }
            .np-article-body p {
                margin-bottom: 0.9rem;
            }
            .np-article-body ul, .np-article-body ol {
                padding-left: 1.3rem;
                margin-bottom: 1rem;
            }
            .np-article-body li {
                margin-bottom: 0.45rem;
                line-height: 1.6;
            }

            /* ==========================================================================
               REFUSAL & SAFETY CARDS
               ========================================================================== */
            .np-refusal-card {
                background: linear-gradient(180deg, #FEF2F2 0%, #FFF5F5 100%);
                border: 1px solid #FECACA;
                border-left: 4px solid #EF4444;
                border-radius: var(--np-radius-md);
                padding: 1.35rem 1.4rem;
                margin-top: 1.25rem;
                margin-bottom: 1.25rem;
                box-shadow: var(--np-shadow-sm);
            }
            .np-refusal-title {
                font-size: 1rem;
                font-weight: 700;
                color: #991B1B;
                display: flex;
                align-items: center;
                gap: 0.5rem;
                margin-bottom: 0.45rem;
            }
            .np-refusal-text {
                font-size: 0.9rem;
                color: #7F1D1D;
                line-height: 1.6;
                margin: 0;
            }

            /* Tip / Guidance Box */
            .np-tip-card {
                background-color: var(--np-slate-50);
                border: 1px solid var(--np-slate-200);
                border-left: 4px solid var(--np-blue-500);
                border-radius: var(--np-radius-sm);
                padding: 0.95rem 1.15rem;
                font-size: 0.875rem;
                color: var(--np-slate-700);
                line-height: 1.55;
                margin-bottom: 1.25rem;
                box-shadow: var(--np-shadow-sm);
            }

            /* ==========================================================================
               JURISDICTION PROGRESSIVE STEP CARDS
               ========================================================================== */
            .np-step-card {
                background: var(--np-white);
                border: 1px solid var(--np-slate-200);
                border-radius: var(--np-radius-md);
                padding: 1.2rem 1.35rem;
                margin-bottom: 1.1rem;
                box-shadow: var(--np-shadow-sm);
                transition: all 0.2s ease;
            }
            .np-step-card:hover {
                border-color: #CBD5E1;
                box-shadow: var(--np-shadow-md);
            }
            .np-step-header {
                font-size: 0.9rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                color: var(--np-navy-800);
                margin-bottom: 0.85rem;
                display: flex;
                align-items: center;
                gap: 0.6rem;
            }
            .np-step-number {
                background: linear-gradient(135deg, var(--np-navy-800) 0%, var(--np-navy-700) 100%);
                color: var(--np-white);
                border-radius: 50%;
                width: 1.6rem;
                height: 1.6rem;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                font-size: 0.8rem;
                font-weight: 800;
                box-shadow: 0 2px 4px rgba(15, 41, 66, 0.15);
            }

            /* Jurisdiction Active Breadcrumb Bar */
            .np-breadcrumb-bar {
                background: linear-gradient(135deg, #F8FAFC 0%, #EFF6FF 100%);
                border: 1px solid #DBEAFE;
                border-radius: var(--np-radius-md);
                padding: 0.85rem 1.15rem;
                margin-bottom: 1.35rem;
                display: flex;
                align-items: center;
                gap: 0.6rem;
                font-size: 0.85rem;
                color: var(--np-navy-800);
                flex-wrap: wrap;
            }
            .np-breadcrumb-tag {
                background: var(--np-white);
                border: 1px solid #BFDBFE;
                border-radius: var(--np-radius-full);
                padding: 0.25rem 0.65rem;
                font-size: 0.8rem;
                font-weight: 600;
                color: var(--np-blue-600);
            }

            /* ==========================================================================
               DISCOVERY CARD
               ========================================================================== */
            .np-discovery-card {
                background: linear-gradient(135deg, #0F2942 0%, #1E3A8A 100%);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: var(--np-radius-lg);
                padding: 1.5rem 1.6rem;
                margin-top: 2.25rem;
                margin-bottom: 1.5rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
                color: var(--np-white);
                box-shadow: var(--np-shadow-lg);
                position: relative;
                overflow: hidden;
            }
            .np-discovery-card::after {
                content: "⚖️";
                position: absolute;
                right: -10px;
                bottom: -20px;
                font-size: 6rem;
                opacity: 0.08;
                pointer-events: none;
            }
            .np-discovery-title {
                font-size: 1.1rem;
                font-weight: 700;
                color: #FFFFFF;
                margin-bottom: 0.3rem;
                display: flex;
                align-items: center;
                gap: 0.4rem;
            }
            .np-discovery-text {
                font-size: 0.875rem;
                color: #CBD5E1;
                line-height: 1.5;
            }

            /* ==========================================================================
               STREAMLIT WIDGET OVERRIDES & POLISH
               ========================================================================== */
            /* Primary Button */
            div.stButton > button[kind="primary"] {
                background: linear-gradient(135deg, #0F2942 0%, #1E3A8A 100%) !important;
                color: #FFFFFF !important;
                border: none !important;
                border-radius: var(--np-radius-md) !important;
                padding: 0.65rem 1.4rem !important;
                font-weight: 700 !important;
                font-size: 0.95rem !important;
                letter-spacing: 0.01em !important;
                box-shadow: 0 4px 12px rgba(15, 41, 66, 0.2) !important;
                transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
            }
            div.stButton > button[kind="primary"]:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 6px 18px rgba(30, 58, 138, 0.3) !important;
            }
            div.stButton > button[kind="primary"]:active {
                transform: translateY(0) !important;
            }

            /* Secondary / Standard Button */
            div.stButton > button:not([kind="primary"]) {
                background-color: var(--np-white) !important;
                color: var(--np-slate-700) !important;
                border: 1px solid var(--np-slate-200) !important;
                border-radius: var(--np-radius-md) !important;
                font-weight: 600 !important;
                font-size: 0.9rem !important;
                transition: all 0.2s ease !important;
            }
            div.stButton > button:not([kind="primary"]):hover {
                border-color: var(--np-slate-400) !important;
                background-color: var(--np-slate-50) !important;
                transform: translateY(-1px) !important;
            }

            /* Textarea & Inputs */
            .stTextArea textarea {
                border-radius: var(--np-radius-md) !important;
                border: 1.5px solid var(--np-slate-200) !important;
                font-family: inherit !important;
                font-size: 0.95rem !important;
                padding: 0.85rem !important;
                transition: all 0.2s ease !important;
                background-color: var(--np-white) !important;
            }
            .stTextArea textarea:focus {
                border-color: var(--np-blue-500) !important;
                box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12) !important;
            }

            /* Selectbox */
            div[data-baseweb="select"] > div {
                border-radius: var(--np-radius-md) !important;
                border-color: var(--np-slate-200) !important;
            }

            /* Sidebar Styling */
            section[data-testid="stSidebar"] {
                background-color: #F8FAFC !important;
                border-right: 1px solid var(--np-slate-200) !important;
            }
            section[data-testid="stSidebar"] .block-container {
                padding-top: 2rem !important;
            }

            /* Sidebar Navigation Box */
            .np-sidebar-nav-header {
                display: flex;
                align-items: center;
                gap: 0.4rem;
                font-size: 0.8rem;
                font-weight: 800;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                color: var(--np-slate-500);
                margin-bottom: 0.6rem;
            }

            /* Sidebar Engine Status Card */
            .np-engine-status-card {
                background: var(--np-white);
                border: 1px solid var(--np-slate-200);
                border-radius: var(--np-radius-md);
                padding: 0.85rem 1rem;
                margin-top: 1.5rem;
                font-size: 0.8rem;
                box-shadow: var(--np-shadow-sm);
            }
            .np-status-row {
                display: flex;
                align-items: center;
                justify-content: space-between;
                margin-bottom: 0.35rem;
                color: var(--np-slate-600);
            }
            .np-status-row:last-child {
                margin-bottom: 0;
            }
            .np-status-tag {
                font-weight: 700;
                color: var(--np-emerald-500);
                display: inline-flex;
                align-items: center;
                gap: 0.3rem;
            }

            /* ==========================================================================
               FOOTER STYLING
               ========================================================================== */
            .np-footer {
                text-align: center;
                border-top: 1px solid var(--np-slate-200);
                padding-top: 2rem;
                margin-top: 3.5rem;
                font-size: 0.85rem;
                color: var(--np-slate-500);
            }
            .np-footer-brand {
                font-family: 'Outfit', sans-serif;
                font-weight: 700;
                font-size: 0.95rem;
                color: var(--np-navy-900);
                margin-bottom: 0.35rem;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 0.4rem;
            }
            .np-footer-links {
                display: flex;
                justify-content: center;
                gap: 1.25rem;
                margin: 0.5rem 0;
                font-size: 0.8rem;
                color: var(--np-slate-600);
            }
            .np-footer-notice {
                font-size: 0.775rem;
                color: var(--np-slate-400);
                max-width: 580px;
                margin: 0.5rem auto 0 auto;
                line-height: 1.5;
            }

            /* Responsive Adjustments */
            @media (max-width: 640px) {
                .np-brand-title {
                    font-size: 1.9rem;
                }
                .np-scope-pillars {
                    grid-template-columns: 1fr;
                }
                .np-trust-bar {
                    gap: 0.5rem;
                }
                .np-article-card {
                    padding: 1.25rem;
                }
            }
        </style>
    """, unsafe_allow_html=True)


def render_brand_header():
    """Render institutional civic brand hero header."""
    st.markdown("""
        <div class="np-hero-container">
            <div class="np-hero-badge">
                <span class="np-pulse-dot"></span>
                <span>Civic Legal Literacy Platform</span>
            </div>
            <div class="np-brand-title">
                ⚖️ <span class="np-gold-text">NYAYAPATH</span>
            </div>
            <div class="np-brand-subtitle">
                Accessible, plain-language judicial court process education & procedural guidance for citizens.
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_trust_bar():
    """Render institutional trust and safety badges bar."""
    st.markdown("""
        <div class="np-trust-bar">
            <div class="np-trust-badge">
                <span class="np-trust-badge-icon">📖</span>
                <span>Plain Language Procedures</span>
            </div>
            <div class="np-trust-badge">
                <span class="np-trust-badge-icon">🔒</span>
                <span>Zero Data Retention</span>
            </div>
            <div class="np-trust-badge">
                <span class="np-trust-badge-icon">🛡️</span>
                <span>Active Safety Guardrails</span>
            </div>
            <div class="np-trust-badge">
                <span class="np-trust-badge-icon">🏛️</span>
                <span>Jurisdiction-Aware</span>
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_information_scope_card():
    """Render clear, non-alarming two-column information scope transparency card."""
    st.markdown("""
        <div class="np-scope-card">
            <div class="np-scope-header">
                <span>ⓘ</span>
                <span>Educational Purpose & Transparency Scope</span>
            </div>
            <p class="np-scope-text">
                NyayaPath helps citizens understand general court workflows, standard litigation stages, and legal terminology.
            </p>
            <div class="np-scope-pillars">
                <div class="np-pillar-item">
                    <span class="np-pillar-icon">✅</span>
                    <span><strong>What it provides:</strong> General court procedures, document explanations, and neutral case flow steps.</span>
                </div>
                <div class="np-pillar-item">
                    <span class="np-pillar-icon">🚫</span>
                    <span><strong>What it avoids:</strong> Personalized legal counsel, litigation strategy, predictions, or legal representation.</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_privacy_notice():
    """Render subtle privacy reminder."""
    st.markdown("""
        <div class="np-privacy-box">
            <span>🔒</span>
            <span><strong>Privacy Shield Active:</strong> Do not enter sensitive personally identifiable information (Aadhaar/SSN), bank details, or private case numbers.</span>
        </div>
    """, unsafe_allow_html=True)


def render_footer():
    """Render civic footer with official references."""
    st.markdown("""
        <div class="np-footer">
            <div class="np-footer-brand">
                ⚖️ NYAYAPATH — Independent Civic Legal Education Platform
            </div>
            <div class="np-footer-links">
                <span>📚 Public Legal Education</span>
                <span>•</span>
                <span>🛡️ AI Safety-Protected</span>
                <span>•</span>
                <span>🏛️ eCourts Aligned</span>
            </div>
            <div class="np-footer-notice">
                Disclaimer: NyayaPath provides purely educational information and does not constitute formal legal counsel. 
                For specific legal proceedings, always verify details with official court registries or consult an enrolled advocate. © 2026 NyayaPath.
            </div>
        </div>
    """, unsafe_allow_html=True)
