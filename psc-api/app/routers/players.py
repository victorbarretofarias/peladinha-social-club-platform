from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/players", tags=["Players"])

@router.post("/", response_model=schemas.PlayerResponse)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(database.get_db)):
    return crud.create_player(db, player)

@router.get("/", response_model=list[schemas.PlayerResponse])
def get_players(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_players(db, skip, limit)

@router.get("/{player_id}", response_model=schemas.PlayerResponse)
def get_player(player_id: int, db: Session = Depends(database.get_db)):
    player = crud.get_player(db, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player
