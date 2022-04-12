#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models import City


class State(BaseModel):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        """inherited init"""
        super.__init__(*args, **kwargs)

    if models.storage_type != "db":
        @property
        def cities(self):
            """
            Cities' getter that return
            a list of city instances
            """
            city_list = []
            instances = models.storage.all()
            for value in instances.values():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list
