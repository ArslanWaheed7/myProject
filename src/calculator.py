def calculate_tax(income: float, tax_rate: float, currency: str = 'USD') -> float:
    return income * tax_rate


def calculate_sum_v2(a: float, b: float, operation: str = '+') -> float:
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
