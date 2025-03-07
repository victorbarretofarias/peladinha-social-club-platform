# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

# 🚀 CRUD for Teams
def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def get_teams(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Team).offset(skip).limit(limit).all()

def get_team(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()


# 🚀 CRUD for Players
def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def get_players(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Player).offset(skip).limit(limit).all()

def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()


# 🚀 CRUD for Matches
def create_match(db: Session, match: schemas.MatchCreate):
    db_match = models.Match(**match.dict())
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match

def get_matches(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Match).offset(skip).limit(limit).all()

def get_match(db: Session, match_id: int):
    return db.query(models.Match).filter(models.Match.id == match_id).first()


# 🚀 CRUD for MatchPlayers (Relationships)
def create_match_player(db: Session, match_player: schemas.MatchPlayerCreate):
    db_match_player = models.MatchPlayer(**match_player.dict())
    db.add(db_match_player)
    db.commit()
    db.refresh(db_match_player)
    return db_match_player

def get_match_players(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.MatchPlayer).offset(skip).limit(limit).all()

def get_match_player(db: Session, match_player_id: int):
    return db.query(models.MatchPlayer).filter(models.MatchPlayer.id == match_player_id).first()
