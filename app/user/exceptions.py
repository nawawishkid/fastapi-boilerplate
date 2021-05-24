class UserNotFoundError(Exception):
    def __init__(self, id: int) -> None:
        super().__init__(f"User with ID {id} could not be found.")


class UserAlreadyExistsError(Exception):
    def __init__(self, email: str) -> None:
        super().__init__(f"User with email '{email}' already exists.")
