#!/usr/bin/python3
"""simple app to return profile information"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import requests
from datetime import datetime, timezone


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/me", status_code=200)
async def get_profile():
    """Return profile informationas json"""
    try:
        cat_fact_response = requests.get("https://catfact.ninja/fact", timeout=5)
        cat_fact_response.raise_for_status()
        fact = cat_fact_response.json().get("fact", "Could not fetch cat fact.")
    except requests.exceptions.RequestException:
        fact = "Could not fetch cat fact."

    user_info = {
        "status": "success",
        "user": {
            "email": "naddulidaniel94@gmail.com",
            "name": "Nadduli Daniel",
            "stack": "Python/FastAPI"
        },
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "fact": fact
    }

    return JSONResponse(content=user_info)