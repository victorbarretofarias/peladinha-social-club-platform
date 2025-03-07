# FastAPI Match Management API

## 🚀 Project Overview
This FastAPI-based project manages teams, players, and matches with a PostgreSQL database hosted on Neon.
It includes CRUD operations and follows best practices for API development.

## 📌 Features
- FastAPI framework with Pydantic models for validation
- PostgreSQL database integration (Neon-hosted)
- CRUD operations for **Teams, Players, Matches, and Match Players**
- Automatic JSON responses using Pydantic schemas
- CORS enabled for API access

---

## 📂 Project Structure
```
.
├── app/
│   ├── main.py          # Main FastAPI app
│   ├── database.py      # Database connection setup
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # Database operations
│   ├── routers/         # API route handlers
│   │   ├── teams.py
│   │   ├── players.py
│   │   ├── matches.py
│   │   ├── match_players.py
│   ├── __init__.py
├── .env                 # Environment variables
├── requirements.txt      # Dependencies
├── README.md            # Project documentation
```

---

## 🛠 Setup & Installation
### 1️⃣ **Clone the repository**
```sh
git clone <repository_url>
cd <repository_folder>
```

### 2️⃣ **Create a virtual environment**
```sh
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ **Install dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Set up the `.env` file**
Create a `.env` file in the root directory:
```
DATABASE_URL=postgresql://<user>:<password>@<neon_host>:<port>/<db_name>
```

### 5️⃣ **Run database migrations (if needed)**
```sh
alembic upgrade head
```

### 6️⃣ **Start the FastAPI server**
```sh
uvicorn app.main:app --reload
```

API will be running at: **`http://127.0.0.1:8000`**

---

## 🔍 API Testing
### **Swagger UI** (Interactive Docs)
Open in your browser:
```
http://127.0.0.1:8000/docs
```

### **cURL Example: Create a Team**
```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/teams/' \
  -H 'Content-Type: application/json' \
  -d '{"team_name": "Team Alpha"}'
```

### **Test with Python Requests**
```python
import requests

response = requests.get("http://127.0.0.1:8000/teams")
print(response.json())
```

---

## ✅ Running Tests
```sh
pytest
```

---