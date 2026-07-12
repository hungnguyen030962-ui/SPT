from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import engine, Base, SessionLocal
from app.routers import questions, literature, flashcards
from app.models.question import Question

# Create tables if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Backend API for SPT HNUE exam preparation website.",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers under /api
app.include_router(questions.router, prefix=settings.API_V1_STR)
app.include_router(literature.router, prefix=settings.API_V1_STR)
app.include_router(flashcards.router, prefix=settings.API_V1_STR)

@app.on_event("startup")
def startup_event():
    # Automatically seed the database if it contains no questions
    db = SessionLocal()
    try:
        q_count = db.query(Question).count()
        if q_count < 90:
            print(f"Database has only {q_count} questions. Auto-seeding full data...")
            from app.seed import seed_db
            seed_db()
        else:
            print(f"Database contains {q_count} questions. Skipping auto-seed.")
    except Exception as e:
        print(f"Error checking database during startup: {e}")
    finally:
        db.close()

@app.get("/")
def read_root():
    return {
        "status": "online",
        "project": settings.PROJECT_NAME,
        "docs": "/docs"
    }
