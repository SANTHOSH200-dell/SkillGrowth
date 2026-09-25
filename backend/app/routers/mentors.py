from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..dependencies import get_current_user
from ..models import Mentor,MentorRequest
router=APIRouter(prefix="/api/mentors",tags=["Mentors"])
@router.get("/")
def all(db:Session=Depends(get_db)):
 if db.query(Mentor).count()==0:
  db.add_all([Mentor(name="Arun Kumar",company="TechNova",role="Senior Software Engineer",bio="Backend and product engineering mentor.",expertise="Python,FastAPI,Cloud",experience=8,location="Chennai"),Mentor(name="Priya Menon",company="DataWorks",role="Data Scientist",bio="Data and AI career mentor.",expertise="Python,SQL,Machine Learning",experience=6,location="Bengaluru"),Mentor(name="Rahul Shah",company="InnovateLabs",role="Product Manager",bio="Product, startup and leadership mentor.",expertise="Product,Startups,Communication",experience=10,location="Mumbai")]);db.commit()
 return [{"id":m.id,"name":m.name,"company":m.company,"role":m.role,"bio":m.bio,"expertise":m.expertise,"experience":m.experience,"location":m.location,"mode":m.mode} for m in db.query(Mentor).filter(Mentor.is_active==True).all()]
@router.get("/my")
def mine(u=Depends(get_current_user),db:Session=Depends(get_db)):return [{"id":r.id,"mentor_id":r.mentor_id,"message":r.message,"status":r.status} for r in db.query(MentorRequest).filter(MentorRequest.user_id==u.id).all()]
@router.post("/request")
def req(d:dict,u=Depends(get_current_user),db:Session=Depends(get_db)):
 mid=int(d["mentor_id"])
 if not db.query(Mentor).filter(Mentor.id==mid).first():raise HTTPException(404,"Mentor not found")
 db.add(MentorRequest(user_id=u.id,mentor_id=mid,message=d.get("message","")));db.commit();return {"message":"Mentorship request sent"}
