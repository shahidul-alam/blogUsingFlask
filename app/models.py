from typing import Optional
import sqlalchemy as sqlalchemy
import sqlalchemy.orm as so
from app import db

class User(db.model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(128), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String[256])

    def __ref__(self):
        return '<User {}>'.format(self.username)
