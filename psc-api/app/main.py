from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import teams, players, matches, match_players
from .database import engine, Base

# ✅ Initialize DB Tables (Only for local development)
Base.metadata.create_all(bind=engine)

# ✅ FastAPI App Instance
app = FastAPI(title="Match Management API", version="1.0")

# ✅ CORS Middleware (Adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include Routers
app.include_router(teams.router)
app.include_router(players.router)
app.include_router(matches.router)
app.include_router(match_players.router)

# ✅ Root Endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Match Management API!"}