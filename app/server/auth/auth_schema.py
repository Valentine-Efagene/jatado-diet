
from typing import Annotated
from pydantic import BaseModel
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
OAuthTokenDeps = Annotated[str, Depends(oauth2_scheme)]
