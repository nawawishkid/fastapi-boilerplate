class UserNotFoundError(Exception):
    def __init__(self, id: int) -> None:
        super().__init__(f"User with ID {id} could not be found.")
