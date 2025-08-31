from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.schemas import Profile, Project
from app import crud

router = APIRouter()


@router.get("/projects", response_model=List[Project])
def get_projects_by_skill(skill: str = Query(..., description="Filter projects by skill"), db: Session = Depends(get_db)):
    """Get projects filtered by skill"""
    projects = crud.get_projects_by_skill(db, skill=skill)
    return projects


@router.get("/skills/top")
def get_top_skills(limit: int = Query(10, ge=1, le=50, description="Number of top skills to return"), db: Session = Depends(get_db)):
    """Get top skills with usage count"""
    skills = crud.get_top_skills(db, limit=limit)
    return {"skills": skills}


@router.get("/search", response_model=List[Profile])
def search_profiles(
    q: str = Query(..., min_length=1, description="Search query for profiles"),
    skip: int = Query(0, ge=0, description="Number of profiles to skip"),
    limit: int = Query(10, ge=1, le=100, description="Number of profiles to return"),
    db: Session = Depends(get_db)
):
    """Search profiles by name, description, or skills"""
    profiles = crud.search_profiles(db, query=q, skip=skip, limit=limit)
    return profiles


@router.get("/profiles/summary")
def get_profiles_summary(db: Session = Depends(get_db)):
    """Get summary statistics of all profiles"""
    from sqlalchemy import func
    from app.models import Profile, Skill, Project, WorkExperience
    
    total_profiles = db.query(Profile).count()
    total_skills = db.query(Skill).count()
    total_projects = db.query(Project).count()
    total_work_experiences = db.query(WorkExperience).count()
    
    # Most common skills
    top_skills = crud.get_top_skills(db, limit=5)
    
    return {
        "total_profiles": total_profiles,
        "total_skills": total_skills,
        "total_projects": total_projects,
        "total_work_experiences": total_work_experiences,
        "top_skills": top_skills
    }