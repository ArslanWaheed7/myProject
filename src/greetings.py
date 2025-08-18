def greet_user(username: str) -> str:
    """Greet a user by their username."""
    from datetime import datetime
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"Hello, {username}! Current time is {current_time}"