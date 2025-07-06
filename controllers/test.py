from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from services.user_service import UserService


Base.metadata.create_all(bind=engine)
router = APIRouter()
templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/allusers")
def read_users(request: Request, db: Session = Depends(get_db)):
    users = UserService.get_all_users(db)
    return templates.TemplateResponse("test_users.html", {"request": request, "users": users})
