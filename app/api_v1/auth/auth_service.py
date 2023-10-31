from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends,  HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel, Field
from ..database import user_collection
from ..user.user_schema import User, UserInDB
from ..config import settings
from .auth_schema import OAuthTokenDeps
from ..user.user_schema import Role, Status
from bson import ObjectId

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY: str = settings.secret_key
ALGORITHM: str = settings.hashing_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(settings.token_expiration_minutes)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = Field(None)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    """Convert plain text to hash

    Args:
        password (str): Plain text

    Returns:
        str: Hash
    """
    return pwd_context.hash(password)


async def get_user(username: str):
    user_dict = await user_collection.find_one({'username': {
        "$regex": username,
        "$options": 'i',
    }})

    return UserInDB(**user_dict)


async def authenticate_user(username: str, password: str):
    user = await get_user(username)

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def mock_get_current_user(token: OAuthTokenDeps):
    return UserInDB(
        _id=ObjectId(),
        username="janedoe",
        firstName='Jane',
        lastName="Doe",
        email="janedoe@testmail.com",
        status=Status.ACTIVE,
        role=Role.STAFF,
        hashed_password=get_password_hash('secret')
    )


async def get_current_user(token: OAuthTokenDeps) -> UserInDB:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
