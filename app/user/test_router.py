from sqlalchemy.exc import IntegrityError
from app.user.exceptions import UserNotFoundError
from fastapi.exceptions import HTTPException
from app.user.user_service import UserService
from unittest.mock import MagicMock
from app.user.router import create_user, delete_user, find_user, update_user
import pytest


async def create_coroutine(value):
    async def async_func():
        return value

    return async_func()


@pytest.fixture
def dto():
    dto = MagicMock()
    dto.dict.return_value = {}

    return dto


@pytest.fixture
def user_service():
    return MagicMock()


@pytest.mark.asyncio
async def test_create_user_succeed(dto, user_service: UserService):
    expected_result = 1
    user_service.create.return_value = await create_coroutine(expected_result)
    result = await create_user(dto, user_service)

    user_service.create.assert_called_once_with(dto)
    assert result == expected_result


@pytest.mark.asyncio
async def test_create_user_already_exists(dto, user_service: UserService):
    user_service.create.side_effect = IntegrityError('', '', '')

    with pytest.raises(HTTPException) as exc:
        await create_user(dto, user_service)

    user_service.create.assert_called_once_with(dto)
    assert exc.value.status_code == 409


@pytest.mark.asyncio
async def test_find_one_user_found(user_service: UserService):
    expected_value = 20
    id = 1
    user_service.find_one.return_value = await create_coroutine(expected_value)
    result = await find_user(id, user_service)

    user_service.find_one.assert_called_once_with(id)
    assert result == expected_value


@pytest.mark.asyncio
async def test_find_one_user_not_found(user_service: UserService):
    id = 1
    user_service.find_one.return_value = await create_coroutine(None)

    with pytest.raises(HTTPException) as exc:
        await find_user(id, user_service)

    user_service.find_one.assert_called_once_with(id)
    assert exc.value.status_code == 404


@pytest.mark.asyncio
async def test_update_user_succeed(dto, user_service: UserService):
    expected_result = 20
    id = 1
    user_service.update.return_value = await create_coroutine(expected_result)
    result = await update_user(id, dto, user_service)

    user_service.update.assert_called_once_with(id, dto)
    assert result == expected_result


@pytest.mark.asyncio
async def test_update_user_not_found(dto, user_service: UserService):
    id = 1
    user_service.update.side_effect = UserNotFoundError(id)

    with pytest.raises(HTTPException) as exc:
        await update_user(id, dto, user_service)

    user_service.update.assert_called_once_with(id, dto)
    assert exc.value.status_code == 404


@pytest.mark.asyncio
async def test_delete_user_succeed(user_service: UserService):
    expected_result = 10
    id = 1
    user_service.delete.return_value = await create_coroutine(expected_result)
    result = await delete_user(id, user_service)

    user_service.delete.assert_called_once_with(id)
    assert result == expected_result


@pytest.mark.asyncio
async def test_delete_user_not_found(user_service: UserService):
    id = 1
    user_service.delete.side_effect = UserNotFoundError(id)

    with pytest.raises(HTTPException) as exc:
        await delete_user(id, user_service)

    user_service.delete.assert_called_once_with(id)
    assert exc.value.status_code == 404
