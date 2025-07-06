# FastAPI CRUD MVC Project

This project is a basic CRUD web app built using **FastAPI** with a clean **MVC architecture**, a **service layer**, and an HTML frontend using **Jinja2 templates**.

---

## 📁 Project Structure

```
fastapi_crud_mvc/
├── main.py                       # Entry point for FastAPI app
├── database.py                   # DB configuration (SQLAlchemy + SQLite)
├── models/
│   └── user.py                   # SQLAlchemy user model
├── services/
│   └── user_service.py           # Business logic
├── controllers/
│   ├── user_controller.py        # CRUD routes for User
│   └── test.py                   # Example test controller
├── templates/
│   ├── user_list.html            # User list view
│   └── test.html                 # Example test page
├── static/
│   └── style.css                 # CSS for frontend
├── requirements.txt              # Python dependencies
└── .gitignore                    # Files and folders to ignore in git
```

---

## 🚀 Features

- ✅ Add, List, Update, Delete Users
- ✅ Clean MVC + Service Layer separation
- ✅ SQLite database using SQLAlchemy
- ✅ HTML interface using Jinja2 templates
- ✅ Static files support (CSS, JS)

---

## 🧰 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Jinja2](https://jinja.palletsprojects.com/)
- SQLite (file-based database)

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-crud-mvc.git
cd fastapi-crud-mvc
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

---

## 🌐 Access the Web App

Open your browser at:

```
http://127.0.0.1:8000/
```

---

## 🧪 Available Routes

| Route             | Method | Description                     |
|------------------|--------|---------------------------------|
| `/`              | GET    | Display user list               |
| `/add`           | POST   | Add a new user                  |
| `/delete/{id}`   | POST   | Delete a user                   |
| `/update/{id}`   | POST   | Update a user                   |
| `/test`          | GET    | Test view from another router   |

---

## 📄 Example `.env` (if needed)

```ini
DATABASE_URL=sqlite:///./test.db
```

---

## 🧼 Clean Architecture Flow

1. `Router` → Receives HTTP Request
2. `Service` → Handles business logic
3. `Model` → Communicates with DB
4. Response rendered with Jinja2 HTML templates

---

## ✅ TODO (Future Improvements)

- Add user input validation (Pydantic)
- Add flash messages for form results
- Support pagination
- Add login system with OAuth2/JWT

---

##  Please do ⭐ this repo, if you liked my work.
##  Made with ❤️ using FastAPI and Python

## Feel free to fork, contribute, or reach out with suggestions!
