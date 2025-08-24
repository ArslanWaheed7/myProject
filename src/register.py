from .User import User
def create_user(username: str, email: str, password: str) -> User:
    return User(username, email, password)