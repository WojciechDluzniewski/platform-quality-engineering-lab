from fastapi import FastAPI, HTTPException
from .models import User


app = FastAPI(title="User Service")

FAKE_USERS_DB = {
    1: User(id=1, name="Paula", email="paula@test.com"),
    2: User(id=2, name="Wojciech", email="wojciech@test.com")
}

@app.get("/users/{user_id}", response_model=User)
def ger_user(user_id: int):
    user = FAKE_USERS_DB.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail= "User not found")
    return user