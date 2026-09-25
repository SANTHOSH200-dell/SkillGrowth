from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..dependencies import get_current_user
from ..models import StartupIdea
router=APIRouter(prefix="/api/startups",tags=["Startups"])
def out(x):return {"id":x.id,"user_id":x.user_id,"title":x.title,"description":x.description,"problem":x.problem,"solution":x.solution,"category":x.category,"stage":x.stage,"progress":x.progress,"status":x.status,"created_at":x.created_at}
@router.get("/my")
def mine(u=Depends(get_current_user),db:Session=Depends(get_db)):return [out(x) for x in db.query(StartupIdea).filter(StartupIdea.user_id==u.id).all()]
@router.get("/")
def all(db:Session=Depends(get_db)):return [out(x) for x in db.query(StartupIdea).all()]
@router.post("/")
def create(d:dict,u=Depends(get_current_user),db:Session=Depends(get_db)):
 t=str(d.get("title","")).strip();desc=str(d.get("description","")).strip()
 if not t or not desc:raise HTTPException(400,"Title and description are required")
 x=StartupIdea(user_id=u.id,title=t,description=desc,problem=d.get("problem"),solution=d.get("solution"),category=d.get("category"),stage=d.get("stage","Idea"));db.add(x);db.commit();db.refresh(x);return {"message":"Startup idea created successfully","idea":out(x)}
