#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all, delete", backref="state")

    def cities(self):
        '''returns the list of City instances
        with state_id equals to the current State.id'''
        return [city for city in self.cities if city.state_id == self.id]
