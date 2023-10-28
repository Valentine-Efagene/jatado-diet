from fastapi import HTTPException, status
from ..database import *
from ..user.user_schema import User
from .auth_schema import OAuthTokenDeps
from bson import ObjectId


def fake_decode_token(token: str):
    return User(
        _id=str(ObjectId()),
        username=token + "fakedecoded",
        email="john@example.com", firstName="John"
    )


def fake_hash_password(password: str):
    return "fakehashed"+password


async def get_current_user(token: OAuthTokenDeps):
    user = fake_decode_token(token)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user
