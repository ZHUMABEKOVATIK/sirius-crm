from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from src.core.jwt import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = await verify_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is invalid or expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload