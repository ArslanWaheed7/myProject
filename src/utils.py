"""
Utility functions for the application.
"""

from typing import Optional
from .config import DISCOUNT_RATE

def calculate_discount(amount: Optional[float], rate: Optional[float] = None) -> float:
    """
    Calculate the discount for a given amount.
    
    Args:
        amount (float): The original price.
        rate (float): The discount rate. Defaults to DISCOUNT_RATE.
        
    Returns:
        float: Discounted amount.
    """
    if amount is None:
        return 0.0
    
    rate = rate if rate is not None else DISCOUNT_RATE
    return amount * rate

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

