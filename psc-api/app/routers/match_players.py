from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/match_players", tags=["Match Players"])

@router.post("/", response_model=schemas.MatchPlayerResponse)
def create_match_player(match_player: schemas.MatchPlayerCreate, db: Session = Depends(database.get_db)):
    return crud.create_match_player(db, match_player)

@router.get("/", response_model=list[schemas.MatchPlayerResponse])
def get_match_players(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_match_players(db, skip, limit)

@router.get("/{match_player_id}", response_model=schemas.MatchPlayerResponse)
def get_match_player(match_player_id: int, db: Session = Depends(database.get_db)):
    match_player = crud.get_match_player(db, match_player_id)
    if not match_player:
        raise HTTPException(status_code=404, detail="MatchPlayer not found")
    return match_player