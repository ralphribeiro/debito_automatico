from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException, status

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core import security
from app.core import config
from app.core.security import get_password_hash


router = APIRouter()


@router.post("/login/access-token", response_model=schemas.Token)
def login_access_token(db: Session = Depends(deps.get_db),
                       form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    """
    Get OAuth2 compatible token login for future requests.
    """
    user = crud.user.authenticate(db, email=form_data.username,
                                  password=form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect email or password")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Inactive user")

    access_token_expires = timedelta(
        minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }

