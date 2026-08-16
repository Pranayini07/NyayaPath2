"""
Unit test suite for Jurisdiction-Aware Legal Navigator service and data structures.
"""

import unittest
from data.jurisdictions import (
    get_supported_countries,
    get_regions_for_country,
    get_court_levels_for_country,
    get_legal_domains,
    INDIA_STATES_AND_UTS
)
from services.jurisdiction_service import (
    JurisdictionContext,
    get_jurisdiction_response
)
from prompts import build_jurisdiction_prompt


class TestJurisdictionNavigator(unittest.TestCase):

    def test_jurisdiction_data_integrity(self):
        countries = get_supported_countries()
        self.assertIn("India", countries)
        
        regions = get_regions_for_country("India")
        self.assertEqual(len(regions), 36)
        self.assertIn("Andhra Pradesh", regions)
        self.assertIn("Delhi (NCT)", regions)
        self.assertIn("Maharashtra", regions)
        self.assertIn("Tamil Nadu", regions)

        court_levels = get_court_levels_for_country("India")
        self.assertIn("High Court", court_levels)
        self.assertIn("District & Subordinate Courts", court_levels)

        domains = get_legal_domains()
        self.assertIn("Civil Procedure", domains)
        self.assertIn("Criminal Procedure", domains)

    def test_jurisdiction_context_creation(self):
        context = JurisdictionContext(
            country="India",
            state="Andhra Pradesh",
            court_level="District & Subordinate Courts",
            legal_domain="Civil Procedure"
        )
        self.assertEqual(context.country, "India")
        self.assertEqual(context.state, "Andhra Pradesh")

    def test_build_jurisdiction_prompt(self):
        context = JurisdictionContext(
            country="India",
            state="Andhra Pradesh",
            court_level="High Court",
            legal_domain="Constitutional Law"
        )
        question = "What is the procedure for filing a writ petition?"
        prompt = build_jurisdiction_prompt(question, context)
        self.assertIn("India", prompt)
        self.assertIn("Andhra Pradesh", prompt)
        self.assertIn("High Court", prompt)
        self.assertIn("writ petition", prompt.lower())

    def test_jurisdiction_safety_blocking(self):
        context = JurisdictionContext(
            country="India",
            state="Andhra Pradesh",
            court_level="District & Subordinate Courts",
            legal_domain="Civil Procedure"
        )
        unsafe_question = "What should I do to win my lawsuit in Andhra Pradesh?"
        decision, ai_resp = get_jurisdiction_response(unsafe_question, context)
        
        self.assertFalse(decision.allowed)
        self.assertEqual(ai_resp.error_code, "SAFETY_BLOCK")
        self.assertIsNotNone(decision.refusal_message)

    def test_jurisdiction_safety_allowing_educational(self):
        context = JurisdictionContext(
            country="India",
            state="Andhra Pradesh",
            court_level="District & Subordinate Courts",
            legal_domain="Civil Procedure"
        )
        safe_question = "What generally happens after a civil case is filed?"
        decision, ai_resp = get_jurisdiction_response(safe_question, context)
        
        self.assertTrue(decision.allowed)


if __name__ == "__main__":
    unittest.main()
