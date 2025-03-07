from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/matches", tags=["Matches"])

@router.post("/", response_model=schemas.MatchResponse)
def create_match(match: schemas.MatchCreate, db: Session = Depends(database.get_db)):
    return crud.create_match(db, match)

@router.get("/", response_model=list[schemas.MatchResponse])
def get_matches(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_matches(db, skip, limit)

@router.get("/{match_id}", response_model=schemas.MatchResponse)
def get_match(match_id: int, db: Session = Depends(database.get_db)):
    match = crud.get_match(db, match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return match
