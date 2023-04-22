#!/usr/bin/python3
""" This script defines State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

cascade_values = "all, delete, delete-orphan"


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade=cascade_values, backref="state")

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            '''returns the list of City instances
            with state_id equals to the current State.id'''
            from models import storage
            list_of_cities = []
            dict_cities = storage.all(City)
            for city in dict_cities.values():
                if city.state_id == self.id:
                    list_of_cities.append(city)
            return list_of_cities
