from sqlalchemy import Column, Integer, String, Text
from app.db import Base

class Function(Base):
    """Model representing a registered Python function."""

    __tablename__ = 'functions'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    code = Column(Text)  # Use Text instead of String for larger code blocks
    dependencies = Column(Text, nullable=True)

    def __repr__(self):
        return f"<Function id={self.id}, name='{self.name}'>"
