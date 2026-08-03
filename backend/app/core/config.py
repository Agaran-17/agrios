import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "AgriOS API"
    API_V1_PREFIX: str = "/api/v1"

    DATABASE_URL: str = os.getenv("DATABASE_URL")
    JWT_SECRET: str = os.getenv("JWT_SECRET")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day

    # CORS - frontend URLs allowed to call this API
    ALLOWED_ORIGINS: list = [
        "http://localhost:5173",  # Vite dev server default
        "http://localhost:3000",  # just in case
    ]


settings = Settings()