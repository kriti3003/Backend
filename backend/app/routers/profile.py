from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas import Profile, ProfileCreate, ProfileUpdate, Project, ProjectCreate, ProjectUpdate, WorkExperience, WorkExperienceCreate, WorkExperienceUpdate
from app import crud
from app.auth import get_current_user

router = APIRouter()


@router.post("/profile", response_model=Profile)
async def create_profile(profile: ProfileCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    # Check if profile with email already exists
    db_profile = crud.get_profile_by_email(db, email=profile.email)
    if db_profile:
        raise HTTPException(status_code=400, detail="Profile with this email already exists")
    
    return crud.create_profile(db=db, profile=profile)


@router.get("/profile/{profile_id}", response_model=Profile)
def get_profile(profile_id: int, db: Session = Depends(get_db)):
    db_profile = crud.get_profile(db, profile_id=profile_id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile


@router.get("/profiles", response_model=List[Profile])
def get_profiles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    profiles = crud.get_profiles(db, skip=skip, limit=limit)
    return profiles


@router.put("/profile/{profile_id}", response_model=Profile)
async def update_profile(profile_id: int, profile_update: ProfileUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_profile = crud.update_profile(db, profile_id=profile_id, profile_update=profile_update)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile


@router.delete("/profile/{profile_id}")
async def delete_profile(profile_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    success = crud.delete_profile(db, profile_id=profile_id)
    if not success:
        raise HTTPException(status_code=404, detail="Profile not found")
    return {"message": "Profile deleted successfully"}


@router.post("/profile/{profile_id}/projects", response_model=Project)
async def create_project(profile_id: int, project: ProjectCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_project = crud.create_project(db=db, profile_id=profile_id, project=project)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_project


@router.put("/project/{project_id}", response_model=Project)
async def update_project(project_id: int, project_update: ProjectUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_project = crud.update_project(db, project_id=project_id, project_update=project_update)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project


@router.delete("/project/{project_id}")
async def delete_project(project_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    success = crud.delete_project(db, project_id=project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted successfully"}


@router.post("/profile/{profile_id}/work", response_model=WorkExperience)
async def create_work_experience(profile_id: int, work: WorkExperienceCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_work = crud.create_work_experience(db=db, profile_id=profile_id, work=work)
    if db_work is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_work


@router.put("/work/{work_id}", response_model=WorkExperience)
async def update_work_experience(work_id: int, work_update: WorkExperienceUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_work = crud.update_work_experience(db, work_id=work_id, work_update=work_update)
    if db_work is None:
        raise HTTPException(status_code=404, detail="Work experience not found")
    return db_work


@router.delete("/work/{work_id}")
async def delete_work_experience(work_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    success = crud.delete_work_experience(db, work_id=work_id)
    if not success:
        raise HTTPException(status_code=404, detail="Work experience not found")
    return {"message": "Work experience deleted successfully"}