from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..dependencies import get_current_user
from ..models import Project,UserProject
router=APIRouter(prefix="/api/projects",tags=["Projects"])
SEED=[("Student Management System","Manage student records and workflows.","Beginner"),("Personal Portfolio Website","Build a professional responsive portfolio.","Beginner"),("AI Skill Gap Analyzer","Analyze skills against industry roles.","Advanced"),("Placement Analytics Dashboard","Visualize placement and career readiness.","Intermediate"),("AI Resume Analyzer","Analyze and improve resumes.","Advanced"),("Smart Internship Matcher","Match students to internships using skills.","Advanced"),("Internship Application Tracker","Track internship applications and progress.","Beginner"),("Industry Learning Hub","Connect students to industry learning.","Intermediate"),("Industry-Academia Mentorship Hub","Coordinate mentorship between industry and students.","Intermediate")]
@router.post("/seed")
def seed(db:Session=Depends(get_db)):
 for t,d,l in SEED:
  if not db.query(Project).filter(Project.title==t).first():db.add(Project(title=t,description=d,level=l,required_skills="Python,SQL,Communication",milestones="Plan,Build,Test,Present"))
 db.commit();return {"message":"Project library ready"}
@router.get("/")
def all(db:Session=Depends(get_db)):return [{"id":p.id,"title":p.title,"description":p.description,"level":p.level} for p in db.query(Project).filter(Project.is_active==True).all()]
@router.get("/my")
def mine(u=Depends(get_current_user),db:Session=Depends(get_db)):return [{"id":r.id,"project_id":r.project_id,"progress":r.progress,"status":r.status} for r in db.query(UserProject).filter(UserProject.user_id==u.id).all()]
@router.post("/start")
def start(d:dict,u=Depends(get_current_user),db:Session=Depends(get_db)):
 r=UserProject(user_id=u.id,project_id=int(d["project_id"]));db.add(r);db.commit();return {"message":"Project started"}
