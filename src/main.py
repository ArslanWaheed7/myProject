"""
Main entry point for the application.
"""

import logging
from .tax import calculate_tax
from .utils import calculate_discount, format_currency
from .config import CURRENCY

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:
    """
    Main application function.
    """
    amount = 100.0
    logger.info(f"Base amount: {format_currency(amount, CURRENCY)}")
    
    tax = calculate_tax(amount)
    discount = calculate_discount(amount)
    final_amount = amount + tax - discount
    
    logger.info(f"Tax: {format_currency(tax, CURRENCY)}")
    logger.info(f"Discount: {format_currency(discount, CURRENCY)}")
    logger.info(f"Final Amount: {format_currency(final_amount, CURRENCY)}")

if __name__ == "__main__":
    main()
