#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete")

    @property
    def cities(self):
        from models import storage
        obj_list = []
        for value in storage.all(City).values():
            if self.id == value.id:
                obj_list.append(value)
        return obj_list


