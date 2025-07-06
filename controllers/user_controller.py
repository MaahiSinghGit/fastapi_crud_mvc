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


@router.get("/")
def read_users(request: Request, db: Session = Depends(get_db)):
    users = UserService.get_all_users(db)
    return templates.TemplateResponse("user_list.html", {"request": request, "users": users})


@router.post("/add")
def add_user(name: str = Form(...), email: str = Form(...), db: Session = Depends(get_db)):
    UserService.create_user(name, email, db)
    return RedirectResponse("/", status_code=302)


@router.post("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    UserService.delete_user(user_id, db)
    return RedirectResponse("/", status_code=302)


@router.post("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    UserService.delete_user(user_id, db)
    return RedirectResponse("/", status_code=302)


@router.post("/update/{user_id}")
def update_user(user_id: int, name: str = Form(...), email: str = Form(...), db: Session = Depends(get_db)):
    UserService.update_user(user_id, name, email, db)
    return RedirectResponse("/", status_code=302)
