from fastapi import FastAPI  # external-lib: fastapi
from fastapi.middleware.cors import CORSMiddleware  # external-lib: fastapi
from app.api.auth import router as auth_router  # internal-file: api/auth

app = FastAPI()

# Setup CORS to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Replace with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include authentication routes
app.include_router(auth_router)

@app.get("/")
async def root():  # type: ignore
    return {"message": "Welcome to the User Authentication API"}
