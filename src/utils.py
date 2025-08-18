"""
Utility functions for the application.
"""

from typing import Optional
from .config import DISCOUNT_RATE


def format_currency(value: float, currency: str = "USD") -> str:
    """
    Format a float as a currency string.
    
    Args:
        value (float): Numeric value to format.
        currency (str): Currency symbol or code.
        
    Returns:
        str: Formatted currency string.
    """
    return f"{currency} {value:,.2f}"





def generate_random_numbers() -> List[int]:
    return [random.randint(100, 1000) for _ in range(10)]