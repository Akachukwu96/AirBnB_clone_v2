#!/usr/bin/python3
""" This script defines Place Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
import os

cascade_values = 'all, delete, delete-orphan'


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', cascade=cascade_values,
                               backref='place')
    else:
        @property
        def reviews(self):
            '''returns the list of Review instances with
            place_id equals to the current Place.id'''
            from models import storage
            objects = storage.all(Review)
            obj_list = []
            for obj in objects.keys():
                if objects[obj].place_id == self.id:
                    obj_list.append(objects[obj])
            return obj_list
