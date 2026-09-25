import os
from dotenv import load_dotenv
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError,jwt
from sqlalchemy.orm import Session
from .database import get_db
from .models import User
load_dotenv();SECRET_KEY=os.getenv("SECRET_KEY","development-secret-key");ALGORITHM=os.getenv("ALGORITHM","HS256")
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/api/auth/token")
def get_current_user(token=Depends(oauth2_scheme),db:Session=Depends(get_db)):
 try: uid=int(jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM]).get("sub"))
 except (JWTError,ValueError,TypeError): raise HTTPException(status_code=401,detail="Invalid or expired token")
 u=db.query(User).filter(User.id==uid).first()
 if not u: raise HTTPException(status_code=401,detail="User not found")
 return u
