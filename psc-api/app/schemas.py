# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date, datetime

# Base Schema for Team
class TeamBase(BaseModel):
    team_name: str

class TeamCreate(TeamBase):
    pass

class TeamResponse(TeamBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Base Schema for Player
class PlayerBase(BaseModel):
    username: str
    rank: Optional[int] = 0
    email: EmailStr

class PlayerCreate(PlayerBase):
    pass

class PlayerResponse(PlayerBase):
    id: int
    created_at: datetime
    team_id: Optional[int] = None

    class Config:
        from_attributes = True


# Base Schema for Match
class MatchBase(BaseModel):
    home_team_id: int
    away_team_id: int
    day_of_match: date
    status: Optional[str] = "scheduled"

class MatchCreate(MatchBase):
    pass

class MatchResponse(MatchBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Base Schema for MatchPlayer (Relationship Table)
class MatchPlayerBase(BaseModel):
    match_id: int
    player_id: int
    team_id: Optional[int] = None
    goals: Optional[int] = 0
    assists: Optional[int] = 0

class MatchPlayerCreate(MatchPlayerBase):
    pass

class MatchPlayerResponse(MatchPlayerBase):
    id: int

    class Config:
        from_attributes = True