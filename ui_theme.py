"""
UI Theme and Design System for NyayaPath - Trusted Civic Technology Design.
"""

import streamlit as st


def inject_custom_css():
    """
    Inject custom CSS for institutional trust, calm visual hierarchy,
    responsive card layouts, and crisp readability.
    """
    st.markdown("""
        <style>
            /* Import Inter Font */
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

            html, body, [class*="css"] {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            }

            /* Main Page Container Padding */
            .main .block-container {
                max-width: 820px;
                padding-top: 2rem;
                padding-bottom: 3rem;
            }

            /* Brand Header */
            .np-brand-container {
                text-align: center;
                margin-bottom: 1.5rem;
            }
            .np-brand-title {
                font-size: 2.2rem;
                font-weight: 700;
                color: #0F2942;
                letter-spacing: -0.02em;
                margin-bottom: 0.25rem;
            }
            .np-brand-subtitle {
                font-size: 1.05rem;
                font-weight: 500;
                color: #475569;
                margin-bottom: 1.25rem;
            }

            /* Trust Badges Bar */
            .np-trust-bar {
                display: flex;
                justify-content: center;
                gap: 1.25rem;
                flex-wrap: wrap;
                margin-bottom: 1.75rem;
            }
            .np-trust-badge {
                display: inline-flex;
                align-items: center;
                gap: 0.4rem;
                background-color: #F8FAFC;
                border: 1px solid #E2E8F0;
                border-radius: 9999px;
                padding: 0.35rem 0.85rem;
                font-size: 0.825rem;
                font-weight: 500;
                color: #334155;
            }
            .np-trust-badge-icon {
                font-size: 0.9rem;
            }

            /* Information Scope Card (Disclaimer) */
            .np-scope-card {
                background-color: #F8FAFC;
                border: 1px solid #E2E8F0;
                border-left: 4px solid #0F2942;
                border-radius: 8px;
                padding: 1.1rem 1.25rem;
                margin-bottom: 1.75rem;
            }
            .np-scope-title {
                font-size: 0.925rem;
                font-weight: 600;
                color: #0F2942;
                display: flex;
                align-items: center;
                gap: 0.4rem;
                margin-bottom: 0.4rem;
            }
            .np-scope-text {
                font-size: 0.875rem;
                color: #475569;
                line-height: 1.5;
                margin: 0;
            }

            /* Privacy Notice Box */
            .np-privacy-box {
                background-color: #F0FDF4;
                border: 1px solid #DCFCE7;
                border-radius: 6px;
                padding: 0.65rem 0.9rem;
                font-size: 0.825rem;
                color: #166534;
                margin-top: 0.5rem;
                margin-bottom: 1rem;
                display: flex;
                align-items: center;
                gap: 0.4rem;
            }

            /* Knowledge Article Response Container */
            .np-article-card {
                background-color: #FFFFFF;
                border: 1px solid #E2E8F0;
                border-radius: 10px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.04);
                padding: 1.75rem;
                margin-top: 1.25rem;
                margin-bottom: 1.5rem;
            }
            .np-article-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid #F1F5F9;
                padding-bottom: 0.85rem;
                margin-bottom: 1.25rem;
            }
            .np-article-category {
                font-size: 0.75rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                color: #0F2942;
                background-color: #EFF6FF;
                padding: 0.25rem 0.6rem;
                border-radius: 4px;
            }
            .np-article-transparency {
                font-size: 0.8rem;
                color: #64748B;
                display: flex;
                align-items: center;
                gap: 0.3rem;
            }
            .np-article-body {
                font-size: 0.975rem;
                line-height: 1.65;
                color: #1E293B;
            }

            /* Refusal / Warning Box */
            .np-refusal-card {
                background-color: #FEF2F2;
                border: 1px solid #FEE2E2;
                border-left: 4px solid #EF4444;
                border-radius: 8px;
                padding: 1.25rem;
                margin-top: 1rem;
                margin-bottom: 1rem;
            }
            .np-refusal-title {
                font-size: 0.95rem;
                font-weight: 600;
                color: #991B1B;
                margin-bottom: 0.4rem;
            }
            .np-refusal-text {
                font-size: 0.875rem;
                color: #7F1D1D;
                line-height: 1.5;
            }

            /* Tip / Guidance Box */
            .np-tip-card {
                background-color: #F8FAFC;
                border: 1px solid #E2E8F0;
                border-left: 4px solid #64748B;
                border-radius: 6px;
                padding: 0.85rem 1.1rem;
                font-size: 0.875rem;
                color: #334155;
                margin-bottom: 1.25rem;
            }

            /* Step Card Layout for Jurisdiction Navigator */
            .np-step-card {
                background-color: #FFFFFF;
                border: 1px solid #E2E8F0;
                border-radius: 8px;
                padding: 1.25rem;
                margin-bottom: 1.25rem;
            }
            .np-step-header {
                font-size: 0.875rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.04em;
                color: #0F2942;
                margin-bottom: 0.85rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }
            .np-step-number {
                background-color: #0F2942;
                color: #FFFFFF;
                border-radius: 9999px;
                width: 1.4rem;
                height: 1.4rem;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                font-size: 0.75rem;
                font-weight: 700;
            }

            /* Discovery Card for Home Page */
            .np-discovery-card {
                background-color: #EFF6FF;
                border: 1px solid #DBEAFE;
                border-radius: 8px;
                padding: 1.25rem;
                margin-top: 2rem;
                margin-bottom: 1.5rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .np-discovery-title {
                font-size: 0.95rem;
                font-weight: 600;
                color: #1E40AF;
                margin-bottom: 0.2rem;
            }
            .np-discovery-text {
                font-size: 0.85rem;
                color: #1E3A8A;
            }

            /* Footer Styling */
            .np-footer {
                text-align: center;
                border-top: 1px solid #E2E8F0;
                padding-top: 1.5rem;
                margin-top: 3rem;
                font-size: 0.825rem;
                color: #64748B;
            }
            .np-footer-brand {
                font-weight: 600;
                color: #0F2942;
                margin-bottom: 0.25rem;
            }
            .np-footer-notice {
                font-size: 0.775rem;
                color: #94A3B8;
                margin-top: 0.4rem;
            }
        </style>
    """, unsafe_allow_html=True)


def render_brand_header():
    """Render institutional civic brand header."""
    st.markdown("""
        <div class="np-brand-container">
            <div class="np-brand-title">⚖️ NYAYAPATH</div>
            <div class="np-brand-subtitle">Public Legal Information & Judicial Court Process Education</div>
        </div>
    """, unsafe_allow_html=True)


def render_trust_bar():
    """Render trust badges bar."""
    st.markdown("""
        <div class="np-trust-bar">
            <div class="np-trust-badge">
                <span class="np-trust-badge-icon">📖</span> Educational Information
            </div>
            <div class="np-trust-badge">
                <span class="np-trust-badge-icon">🔒</span> Privacy-Conscious
            </div>
            <div class="np-trust-badge">
                <span class="np-trust-badge-icon">🛡️</span> AI-Assisted & Safety-Aware
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_information_scope_card():
    """Render non-alarming information scope card."""
    st.markdown("""
        <div class="np-scope-card">
            <div class="np-scope-title">ⓘ Information Scope & Purpose</div>
            <p class="np-scope-text">
                NyayaPath provides general educational information about court procedures, case flows, and legal terminology. 
                It does <strong>not</strong> provide personalized legal advice, suggest litigation tactics, predict court outcomes, 
                or represent you in legal matters. For personal legal counsel, please consult a qualified advocate.
            </p>
        </div>
    """, unsafe_allow_html=True)


def render_privacy_notice():
    """Render subtle privacy reminder."""
    st.markdown("""
        <div class="np-privacy-box">
            <span>🔒</span>
            <span><strong>Privacy Reminder:</strong> Avoid entering sensitive personal identification numbers, bank details, or private case numbers.</span>
        </div>
    """, unsafe_allow_html=True)


def render_footer():
    """Render civic footer."""
    st.markdown("""
        <div class="np-footer">
            <div class="np-footer-brand">NYAYAPATH — Independent Civic Legal Education Platform</div>
            <div>Educational Information • AI-Assisted • Safety-Engine Protected</div>
            <div class="np-footer-notice">Not legal advice. Verify important procedures with official court portals (e.g. eCourts India). © 2026 NyayaPath</div>
        </div>
    """, unsafe_allow_html=True)
