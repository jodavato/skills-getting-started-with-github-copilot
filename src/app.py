"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": { ... },
    "Programming Class": { ... },
    "Gym Class": { ... },
    "Soccer Team": {
        "description": "Entrena tácticas y juega partidos amistosos",
        "schedule": "Martes y Jueves, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": []
    },
    "Swimming Club": {
        "description": "Mejora la técnica de natación y compite en relevos",
        "schedule": "Lunes y Miércoles, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": []
    },
    "Art Workshop": {
        "description": "Explora pintura y dibujo con proyectos creativos",
        "schedule": "Miércoles, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Drama Club": {
        "description": "Practica actuación y prepara presentaciones teatrales",
        "schedule": "Viernes, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": []
    },
    "Math Olympiad": {
        "description": "Resuelve problemas avanzados y participa en competencias",
        "schedule": "Lunes y Jueves, 3:30 PM - 4:30 PM",
        "max_participants": 12,
        "participants": []
    },
    "Science Club": {
        "description": "Realiza experimentos y aprende ciencias aplicadas",
        "schedule": "Martes, 4:00 PM - 5:30 PM",
        "max_participants": 14,
        "participants": []
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Check if student is already signed up    if email in activity["participants"]:
    raise HTTPException(status_code=400, detail="Student already signed up for this activity")


    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
