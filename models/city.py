#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    The city class, contains state ID and name.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store cities
        name (sqlalchemy String): The name of the City.
        state_id (sqlalchemy String): The state id of the city.
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(Strin(120), nullable=False)
