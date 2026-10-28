from datetime import datetime, timezone

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()


def utcnow():
    """Naive UTC timestamp (works the same on SQLite and PostgreSQL)."""
    return datetime.now(timezone.utc).replace(tzinfo=None)
