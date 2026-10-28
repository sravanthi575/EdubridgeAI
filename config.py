import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


def _database_url():
    url = os.environ.get("DATABASE_URL")
    if url:
        # Some hosts still give "postgres://", SQLAlchemy needs "postgresql://"
        return url.replace("postgres://", "postgresql://", 1)
    return "sqlite:///" + os.path.join(BASE_DIR, "instance", "edubridge.db")


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-only-secret-change-me"
    SQLALCHEMY_DATABASE_URI = _database_url()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = os.environ.get("SESSION_COOKIE_SECURE") == "1"
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024
    AI_API_KEY = os.environ.get("AI_API_KEY", "")
    AI_MODEL = os.environ.get("AI_MODEL", "claude-sonnet-5-5")
    AUTO_SEED = True


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
    SECRET_KEY = "test-secret"
    AI_API_KEY = ""
