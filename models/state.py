#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """
    Represents a state in the MySQL database

    Attributes:
        __tablename__ (str): The name of the MySQL table to store states.
        name (sqlalchemy String): The name of the state.
        cities (sqlalchemy relationship): The State-City relationship
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
