#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    # amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.city_id = kwargs.get('city_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.name = kwargs.get('name', "")
        self.description = kwargs.get('description', "")
        self.number_rooms = kwargs.get('number_rooms', "")
        self.number_bathrooms = kwargs.get('number_bathrooms', "")
        self.max_guest = kwargs.get('max_guest', "")
        self.price_by_night = kwargs.get('price_by_night', "")
        self.latitude = kwargs.get('latitude', "")
        self.longitude = kwargs.get('longitude', "")
        #self.amenity_ids = kwargs.get('amenity_ids', "")