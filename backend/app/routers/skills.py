from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..dependencies import get_current_user
from ..models import Skill,UserSkill
router=APIRouter(prefix="/api/skills",tags=["Skills"])
@router.get("/my")
def mine(u=Depends(get_current_user),db:Session=Depends(get_db)):
 return [{"id":r.id,"skill":{"id":r.skill.id,"name":r.skill.name},"level":r.level,"score":r.score} for r in db.query(UserSkill).filter(UserSkill.user_id==u.id).all()]
@router.post("/add")
def add(d:dict,u=Depends(get_current_user),db:Session=Depends(get_db)):
 n=str(d.get("skill_name","")).strip()
 if not n: raise HTTPException(400,"Skill name required")
 s=db.query(Skill).filter(Skill.name==n).first()
 if not s:s=Skill(name=n,category="General");db.add(s);db.commit();db.refresh(s)
 r=db.query(UserSkill).filter(UserSkill.user_id==u.id,UserSkill.skill_id==s.id).first()
 if not r:r=UserSkill(user_id=u.id,skill_id=s.id);db.add(r)
 r.level=d.get("level","Beginner");r.score=max(0,min(100,int(d.get("score",0))));db.commit();return {"message":"Skill saved"}
