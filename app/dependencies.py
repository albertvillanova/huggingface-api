from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


# credentials.scheme "Bearer", credentials.credentials = "MY-TOKEN"
security = HTTPBearer(auto_error=False)  # `auto_error=False` allows optional credentials = None


async def build_authorization_headers(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]):
    headers = {"Authorization": f"{credentials.scheme} {credentials.credentials}"} if credentials else {}
    return headers
