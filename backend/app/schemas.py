from pydantic import BaseModel,EmailStr
from typing import Optional
class RegisterRequest(BaseModel):
 full_name:str;email:EmailStr;password:str;college:Optional[str]=None;department:Optional[str]=None;study_year:Optional[str]=None
class LoginRequest(BaseModel):
 email:EmailStr;password:str
