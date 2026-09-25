from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..schemas import RegisterRequest,LoginRequest
from ..auth import hash_password,verify_password,create_access_token
from ..dependencies import get_current_user
router=APIRouter(prefix="/api/auth",tags=["Authentication"])
def out(u): return {"id":u.id,"full_name":u.full_name,"email":u.email,"college":u.college,"department":u.department,"study_year":u.study_year,"career_goal":u.career_goal,"growth_score":u.growth_score}
@router.post("/register")
def register(d:RegisterRequest,db:Session=Depends(get_db)):
 if db.query(User).filter(User.email==d.email).first(): raise HTTPException(400,"Email already registered")
 u=User(full_name=d.full_name,email=d.email,password_hash=hash_password(d.password),college=d.college,department=d.department,study_year=d.study_year);db.add(u);db.commit();db.refresh(u);return {"access_token":create_access_token(u.id),"token_type":"bearer","user":out(u)}
@router.post("/login")
def login(d:LoginRequest,db:Session=Depends(get_db)):
 u=db.query(User).filter(User.email==d.email).first()
 if not u or not verify_password(d.password,u.password_hash): raise HTTPException(401,"Invalid email or password")
 return {"access_token":create_access_token(u.id),"token_type":"bearer","user":out(u)}
@router.get("/me")
def me(u=Depends(get_current_user)): return out(u)
