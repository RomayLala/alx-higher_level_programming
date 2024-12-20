#!/usr/bin/python3
"""
This module contains the class definition for City, inheriting from Base.
It links to the `cities` table in the MySQL database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

class City(Base):
    """
    City class that links to the `cities` table in MySQL database.
    Inherits from `Base` and uses SQLAlchemy to map the table.
    """

    __tablename__ = 'cities'  # Table name in MySQL

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Relationship with the State class (optional)
    state = relationship("State")
