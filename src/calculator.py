from utils import convert_pkr_to_usd
def calculate_tax(income: float, tax_rate: float, currency: str = 'USD') -> float:
    converted_income = convert_pkr_to_usd(income, 0.25) if currency.upper() == 'PKR' else income
    return converted_income * tax_rate