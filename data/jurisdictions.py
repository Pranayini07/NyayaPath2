"""
Canonical data structure for supported countries, states/UTs, court levels, and legal domains in NyayaPath.
"""

from typing import Dict, List, Any

# Canonical list of Indian States and Union Territories
INDIA_STATES_AND_UTS: List[str] = [
    "Andaman and Nicobar Islands",
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chandigarh",
    "Chhattisgarh",
    "Dadra and Nagar Haveli and Daman and Diu",
    "Delhi (NCT)",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jammu and Kashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Ladakh",
    "Lakshadweep",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Puducherry",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]

# Canonical court levels in Indian judicial hierarchy
INDIA_COURT_LEVELS: List[str] = [
    "Supreme Court of India",
    "High Court",
    "District & Subordinate Courts",
    "Tribunals & Specialized Fora (e.g. NCLT, DRT, NGT, Consumer Forum)"
]

# Canonical legal domains supported for educational explanations
SUPPORTED_LEGAL_DOMAINS: List[str] = [
    "Civil Procedure",
    "Criminal Procedure",
    "Family & Matrimonial",
    "Property & Revenue",
    "Consumer Disputes",
    "Labour & Employment",
    "Cyber & Technology",
    "Constitutional Law",
    "Administrative & Service Law",
    "General Court Procedure"
]

# Extensible country registry
JURISDICTIONS: Dict[str, Dict[str, Any]] = {
    "India": {
        "regions": INDIA_STATES_AND_UTS,
        "court_levels": INDIA_COURT_LEVELS,
        "domains": SUPPORTED_LEGAL_DOMAINS
    }
}


def get_supported_countries() -> List[str]:
    return list(JURISDICTIONS.keys())


def get_regions_for_country(country: str) -> List[str]:
    return JURISDICTIONS.get(country, {}).get("regions", [])


def get_court_levels_for_country(country: str) -> List[str]:
    return JURISDICTIONS.get(country, {}).get("court_levels", [])


def get_legal_domains() -> List[str]:
    return SUPPORTED_LEGAL_DOMAINS
