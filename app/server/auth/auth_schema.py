
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
OAuthTokenDeps = Annotated[str, Depends(oauth2_scheme)]
