# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Date, TIMESTAMP, func
from sqlalchemy.orm import relationship
from .database import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String(50), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    players = relationship("Player", back_populates="team", cascade="all, delete")
    home_matches = relationship("Match", foreign_keys="[Match.home_team_id]", back_populates="home_team", cascade="all, delete")
    away_matches = relationship("Match", foreign_keys="[Match.away_team_id]", back_populates="away_team", cascade="all, delete")


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    rank = Column(Integer, default=0)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    team_id = Column(Integer, ForeignKey("teams.id", ondelete="SET NULL"), nullable=True)
    team = relationship("Team", back_populates="players")


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    home_team_id = Column(Integer, ForeignKey("teams.id", ondelete="CASCADE"), nullable=False)
    away_team_id = Column(Integer, ForeignKey("teams.id", ondelete="CASCADE"), nullable=False)
    day_of_match = Column(Date, nullable=False)
    status = Column(String(20), default="scheduled")
    created_at = Column(TIMESTAMP, server_default=func.now())

    home_team = relationship("Team", foreign_keys=[home_team_id], back_populates="home_matches")
    away_team = relationship("Team", foreign_keys=[away_team_id], back_populates="away_matches")
    match_players = relationship("MatchPlayer", back_populates="match", cascade="all, delete")


class MatchPlayer(Base):
    __tablename__ = "match_players"

    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id", ondelete="CASCADE"), nullable=False)
    player_id = Column(Integer, ForeignKey("players.id", ondelete="CASCADE"), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id", ondelete="SET NULL"), nullable=True)
    goals = Column(Integer, default=0)
    assists = Column(Integer, default=0)

    match = relationship("Match", back_populates="match_players")
    player = relationship("Player")
    team = relationship("Team")
