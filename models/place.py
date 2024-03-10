#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.review import Review

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id", ondelete='CASCADE'),
                     nullable=False) 
    user_id = Column(String(60), ForeignKey("users.id", ondelete='CASCADE'),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    cities = relationship("City", back_populates="places")
    user = relationship("User", back_populates="places")
    reviews = relationship("Review", cascade="all, delete", back_populates="place")
    amenity_ids = []

#    def reviews(self):
#        from models import storage
#        obj_list = []
#        for value in storage.all(Review).values():
#            if self.id == value.id:
#                obj_list.append(value)
#        return obj_list


