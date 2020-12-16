# from datetime import datetime, timedelta
# from typing import Optional

# from jose import jwt

# from app.core import config
# from app.core import security



# def send_email() -> None:
#     pass


# def generate_password_reset_token(email: str) -> str:
#     delta = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
#     now = datetime.utcnow()
#     expires = now + delta
#     exp = expires.timestamp()
#     encoded_jwt = jwt.encode({"exp": exp, "nbf": now, "sub": email},
#                              config.SECRET_KEY, algorithm=security.ALGORITHM)
#     return encoded_jwt


# def verify_password_reset_token(token: str) -> Optional[str]:
#     try:
#         decoded_token = jwt.decode(token, config.SECRET_KEY,
#                                    algorithms=[security.ALGORITHM])
#         return decoded_token["email"]
#     except jwt.JWTError:
#         return None
