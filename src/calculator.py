import logging

def wlecome_to_gotham(income: float, tax_rate: float, currency: str = 'USD') -> float:
    try:
        if income < 0 or tax_rate < 0:
            raise ValueError('Income and tax rate must be non-negative')
        result = income * tax_rate
        logging.info(f'Tax calculated: {result} {currency}')
        return result
    except Exception as e:
        logging.error(f'Error calculating tax: {e}')