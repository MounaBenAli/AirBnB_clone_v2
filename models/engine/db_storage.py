#!/usr/bin/python3
"""
DataBase Storage Module
"""
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from ..base_model import Base


class DBStorage:
    """
    DataBase Storage Class
    """
    __engine = None
    __session = None
    classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']

    def __init__(self):
        """
        Init method
        """
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv('HBNB_ENV')

        engine = 'mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER,
                                                      HBNB_MYSQL_PWD,
                                                      HBNB_MYSQL_HOST,
                                                      HBNB_MYSQL_DB)
        self.__engine = create_engine(engine, pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current session
        """
        dictionary = {}
        if cls is None:
            for c in self.classes:
                c = eval(c)
                for instance in self.__session.query(c).all():
                    key = instance.__class__.__name__ + '.' + instance.id
                    dictionary[key] = instance
        else:
            for instance in self.__session.query(cls).all():
                key = instance.__class__.__name__ + '.' + instance.id
                dictionary[key] = instance
        return dictionary

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create table in database
        """
        Base.metadata.create_all(self.__engine)
        db_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(db_session)
        self.__session = Session()
