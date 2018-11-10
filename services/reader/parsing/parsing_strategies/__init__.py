"""
Parsing strategies
"""

import re

def comma_to_dot(text: str) -> str:
    """
    Replace commas with dots
    """
    return re.sub(",", ".", text)