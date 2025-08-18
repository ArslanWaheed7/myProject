"""
Main entry point for the application.
"""

import logging
from .tax import calculate_tax
from .utils import calculate_discount, format_currency
from .config import CURRENCY

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    main()
