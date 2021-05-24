from app.user.user_service import UserService
from app.user.exceptions import UserAlreadyExistsError, UserNotFoundError
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from app.dependencies import get_db_session
from app.user.dtos import CreateUserDto, UpdateUserDto, UserDto
from fastapi import APIRouter, HTTPException


def get_user_service(session: Session = Depends(get_db_session)):
    return UserService(session)


router = APIRouter()


@router.post('', status_code=201, response_model=UserDto)
async def create_user(dto: CreateUserDto, user_service: UserService = Depends(get_user_service)):
    try:
        return await user_service.create(dto)
    except UserAlreadyExistsError as exc:
        raise HTTPException(409, str(exc))


@router.get('/{id}', response_model=UserDto)
async def find_user(id: int, user_service: UserService = Depends(get_user_service)):
    user = await user_service.find_one(id)

    if not user:
        raise HTTPException(404, str(UserNotFoundError(id)))

    return user


@router.patch('/{id}', response_model=UserDto)
async def update_user(id: int, dto: UpdateUserDto, user_service: UserService = Depends(get_user_service)):
    try:
        return await user_service.update(id, dto)
    except UserNotFoundError as exc:
        raise HTTPException(404, str(exc))


@router.delete('/{id}', status_code=204)
async def delete_user(id: int, user_service: UserService = Depends(get_user_service)):
    try:
        return await user_service.delete(id)
    except UserNotFoundError as exc:
        raise HTTPException(404, str(exc))
