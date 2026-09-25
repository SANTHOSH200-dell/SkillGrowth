import os
from datetime import datetime,timedelta,timezone
from dotenv import load_dotenv
from jose import jwt
from passlib.context import CryptContext
load_dotenv()
SECRET_KEY=os.getenv("SECRET_KEY","development-secret-key");ALGORITHM=os.getenv("ALGORITHM","HS256");ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES","60"))
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
def hash_password(p): return pwd_context.hash(p)
def verify_password(p,h): return pwd_context.verify(p,h)
def create_access_token(uid):
 return jwt.encode({"sub":str(uid),"exp":datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)},SECRET_KEY,algorithm=ALGORITHM)
