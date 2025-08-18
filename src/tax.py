"""
Tax calculation module.
"""

from typing import Optional
from .config import TAX_RATE
import logging

logger = logging.getLogger(__name__)

def calculate_tax(amount: Optional[float]) -> float:
    """
    Calculate the tax for a given amount.
    
    Args:
        amount (float): The base amount before tax.
        
    Returns:
        float: The calculated tax value.
    """
    if amount is None:
        logger.warning("Received None as amount. Returning 0.0.")
        return 0.0
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    
    return amount * TAX_RATE
