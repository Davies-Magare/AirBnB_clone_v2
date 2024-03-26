#!/usr/bin/python3
"""This module defines a class for a database engine"""
from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
import os

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        usr = os.environ.get('HBNB_MYSQL_USER')
        pwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')
        test_val = os.environ.get('HBNB_ENV')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(usr, pwd, host, db),
                                       pool_pre_ping=True)
        if test_val == 'test':
            metadata = MetaData()
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Return database objects."""
        self.reload()
        obj_dict = {}
        if cls != None:
            results = self.__session.query(cls).all()
            for result in results:
                try:
                    delattr(result, "_sa_instance_state")
                except Exception:
                    pass
                key = "{}.{}".format(result.__class__.__name__, result.id)
                obj_dict[key] = result
        else:
            tables = [City, State, User, Place, Review]
            for table in tables:
                results = self.__session.query(table).all()
                for result in results:
                    try:
                        delattr(result, "_sa_instance_state")
                    except Exception:
                        pass
                    key = "{}.{}".format(result.__class__.__name__, result.id)
                    obj_dict[key] = result
        return obj_dict

    def new(self, obj):
        """Add object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to database."""
        self.__session.commit()

    def delete(self, obj):
        """Delete object from database session."""
        if obj != None:
            self.__session.delete(obj)
   
    def reload(self):
        """Create connection to database and create tables."""
        from models.city import City
        from models.state import State
        from models.base_model import Base
        from models.user import User
        from models.place import Place
        from models.review import Review
        from sqlalchemy.orm import sessionmaker, scoped_session

        session_factory = sessionmaker(bind=self.__engine)
        self.Session = scoped_session(session_factory)
        self.__session = self.Session()

        Base.metadata.create_all(bind=self.__engine)
    def close(self):
        """Destroy the session"""
        self.Session.close()

