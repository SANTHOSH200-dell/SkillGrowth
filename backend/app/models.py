from datetime import datetime
from sqlalchemy import Boolean,Column,DateTime,ForeignKey,Integer,String,Text
from sqlalchemy.orm import relationship
from .database import Base
class User(Base):
 __tablename__="users";id=Column(Integer,primary_key=True);full_name=Column(String(100),nullable=False);email=Column(String(150),unique=True,index=True,nullable=False);password_hash=Column(String(255),nullable=False);college=Column(String(200));department=Column(String(150));study_year=Column(String(50));career_goal=Column(String(200));growth_score=Column(Integer,default=0);is_active=Column(Boolean,default=True);created_at=Column(DateTime,default=datetime.utcnow)
class Skill(Base):
 __tablename__="skills";id=Column(Integer,primary_key=True);name=Column(String(100),unique=True,nullable=False);category=Column(String(100),nullable=False)
class UserSkill(Base):
 __tablename__="user_skills";id=Column(Integer,primary_key=True);user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"));skill_id=Column(Integer,ForeignKey("skills.id",ondelete="CASCADE"));level=Column(String(50),default="Beginner");score=Column(Integer,default=0);skill=relationship("Skill")
class Project(Base):
 __tablename__="projects";id=Column(Integer,primary_key=True);title=Column(String(200),nullable=False);description=Column(Text,nullable=False);level=Column(String(50),nullable=False);duration=Column(String(100));category=Column(String(100));required_skills=Column(Text,nullable=False);milestones=Column(Text,nullable=False);is_active=Column(Boolean,default=True)
class UserProject(Base):
 __tablename__="user_projects";id=Column(Integer,primary_key=True);user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"));project_id=Column(Integer,ForeignKey("projects.id",ondelete="CASCADE"));progress=Column(Integer,default=0);status=Column(String(50),default="Started")
class Internship(Base):
 __tablename__="internships";id=Column(Integer,primary_key=True);title=Column(String(200),nullable=False);company=Column(String(200),nullable=False);description=Column(Text,nullable=False);location=Column(String(150));mode=Column(String(50));duration=Column(String(100));stipend=Column(String(100));required_skills=Column(Text,nullable=False);category=Column(String(100));openings=Column(Integer,default=1);is_active=Column(Boolean,default=True);created_at=Column(DateTime,default=datetime.utcnow)
class UserInternship(Base):
 __tablename__="user_internships";id=Column(Integer,primary_key=True);user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"));internship_id=Column(Integer,ForeignKey("internships.id",ondelete="CASCADE"));status=Column(String(50),default="Applied");progress=Column(Integer,default=0);match_score=Column(Integer,default=0);applied_at=Column(DateTime,default=datetime.utcnow);internship=relationship("Internship")
class Mentor(Base):
 __tablename__="mentors";id=Column(Integer,primary_key=True);name=Column(String(150),nullable=False);email=Column(String(150));company=Column(String(200));role=Column(String(150));bio=Column(Text);expertise=Column(Text,nullable=False);experience=Column(Integer,default=0);location=Column(String(150));mode=Column(String(50),default="Online");availability=Column(String(100),default="Available");rating=Column(Integer,default=5);is_active=Column(Boolean,default=True)
class MentorRequest(Base):
 __tablename__="mentor_requests";id=Column(Integer,primary_key=True);user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"));mentor_id=Column(Integer,ForeignKey("mentors.id",ondelete="CASCADE"));message=Column(Text);status=Column(String(50),default="Pending");created_at=Column(DateTime,default=datetime.utcnow)
class StartupIdea(Base):
 __tablename__="startup_ideas";id=Column(Integer,primary_key=True);user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"));title=Column(String(200),nullable=False);description=Column(Text,nullable=False);problem=Column(Text);solution=Column(Text);category=Column(String(100));stage=Column(String(100),default="Idea");progress=Column(Integer,default=0);status=Column(String(50),default="Active");created_at=Column(DateTime,default=datetime.utcnow)
