from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base,engine
from . import models
from .routers import auth,skills,projects,internships,mentors,startups
Base.metadata.create_all(bind=engine)
app=FastAPI(title="SkillGrowth API",version="1.0.0")
app.add_middleware(CORSMiddleware,allow_origins=["http://127.0.0.1:5500","http://localhost:5500","http://127.0.0.1:5501","http://localhost:5501"],allow_methods=["*"],allow_headers=["*"])
app.include_router(auth.router);app.include_router(skills.router);app.include_router(projects.router);app.include_router(internships.router);app.include_router(mentors.router);app.include_router(startups.router)
@app.get("/")
def root():return {"message":"SkillGrowth Backend is running 🚀","status":"success"}
@app.get("/api/health")
def health():return {"status":"healthy","database":"connected"}
