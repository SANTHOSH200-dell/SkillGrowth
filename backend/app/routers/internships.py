import json
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..dependencies import get_current_user
from ..models import Internship,UserInternship
router=APIRouter(prefix="/api/internships",tags=["Internships"])
def norm(v):
 try:
  x=json.loads(v);return x if isinstance(x,list) else [str(v)]
 except:return [s.strip() for s in str(v).split(",") if s.strip()]
def out(i):return {"id":i.id,"title":i.title,"company":i.company,"description":i.description,"location":i.location or "","mode":i.mode or "Online","duration":i.duration or "","stipend":i.stipend or "","required_skills":norm(i.required_skills),"category":i.category or "","openings":i.openings}
@router.get("/")
def all(db:Session=Depends(get_db)):
 if db.query(Internship).count()==0:
  db.add_all([Internship(title="Software Engineering Intern",company="SkillTech",description="Build web applications and APIs.",location="Chennai",mode="Hybrid",duration="3 Months",stipend="₹15,000/month",required_skills="Python,JavaScript,SQL",category="Software",openings=3),Internship(title="Data Analytics Intern",company="DataWorks",description="Analyze datasets and dashboards.",location="Remote",mode="Remote",duration="2 Months",stipend="₹12,000/month",required_skills="Python,SQL,Excel",category="Data",openings=2),Internship(title="AI/ML Intern",company="InnovateAI",description="Work on applied machine learning projects.",location="Bengaluru",mode="Hybrid",duration="6 Months",stipend="₹20,000/month",required_skills="Python,Machine Learning,SQL",category="AI",openings=2)]);db.commit()
 return [out(i) for i in db.query(Internship).filter(Internship.is_active==True).all()]
@router.get("/my")
def mine(u=Depends(get_current_user),db:Session=Depends(get_db)):return [{"id":a.id,"internship_id":a.internship_id,"status":a.status,"progress":a.progress,"match_score":a.match_score,"internship":out(a.internship)} for a in db.query(UserInternship).filter(UserInternship.user_id==u.id).all()]
@router.post("/apply")
def apply(d:dict,u=Depends(get_current_user),db:Session=Depends(get_db)):
 iid=int(d["internship_id"]);i=db.query(Internship).filter(Internship.id==iid).first()
 if not i:raise HTTPException(404,"Internship not found")
 if db.query(UserInternship).filter(UserInternship.user_id==u.id,UserInternship.internship_id==iid).first():return {"message":"Already applied"}
 db.add(UserInternship(user_id=u.id,internship_id=iid));db.commit();return {"message":"Application submitted successfully"}
