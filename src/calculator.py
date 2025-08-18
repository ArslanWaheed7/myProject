def calculator(a: float, b: float, operation: str) -> float:
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            raise ValueError('Division by zero')
    else:
        raise ValueError('Invalid operation')