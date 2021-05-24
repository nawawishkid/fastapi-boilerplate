from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session
from .dtos import CreateUserDto, UpdateUserDto
from .models import User
from .exceptions import UserAlreadyExistsError, UserNotFoundError


class UserService():
    def __init__(self, session: Session) -> None:
        self.session = session

    async def create(self, dto: CreateUserDto):
        user = User(**dto.dict())

        try:
            self.session.add(user)
            self.session.commit()

            return user
        except IntegrityError as exc:
            raise UserAlreadyExistsError(exc.params["email"])

    async def find_one(self, id: int):
        return self.session.query(User).filter_by(id=id).first()

    async def update(self, id: int, dto: UpdateUserDto):
        result = self.session.query(User).filter_by(
            id=id).update(dto, synchronize_session='fetch')

        if result.rowcount == 0:
            raise UserNotFoundError(id)

        return result

    async def delete(self, id: int):
        result = self.session.query(User).filter_by(id=id).delete()

        if result.rowcount == 0:
            raise UserNotFoundError(id)

        return result
