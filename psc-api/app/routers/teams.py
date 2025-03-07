from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/teams", tags=["Teams"])

@router.post("/", response_model=schemas.TeamResponse)
def create_team(team: schemas.TeamCreate, db: Session = Depends(database.get_db)):
    return crud.create_team(db, team)

@router.get("/", response_model=list[schemas.TeamResponse])
def get_teams(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_teams(db, skip, limit)

@router.get("/{team_id}", response_model=schemas.TeamResponse)
def get_team(team_id: int, db: Session = Depends(database.get_db)):
    team = crud.get_team(db, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team
