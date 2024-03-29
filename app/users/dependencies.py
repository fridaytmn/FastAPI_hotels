
from datetime import datetime
from fastapi import Depends, Request
from jose import JWTError, jwt
from app.config import settings
from app.exceptions import IncorrentTokenFormatException, TokenAbsentException, TokenExpiredException, UserInNotPresentException
from app.users.dao import UserDAO
from app.users.models import Users


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM )
    except JWTError:
        raise IncorrentTokenFormatException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserInNotPresentException
    user = await UserDAO.find_by_id(int(user_id))
    if not user:
        raise UserInNotPresentException
    return user

async def get_current_admin_user(current_user: Users = Depends(get_current_user)):
    # if current_user.role != 'admin':
    #     raise HTTPException(status.HTTP_404_NOT_FOUND)
    return current_user