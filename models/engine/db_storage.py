#!/usr/bin/python
'''New engine DBStorage'''

import os
import sqlalchemy
from sqlalchemy import create_engine, text
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    '''new engine class'''
    __engine = None
    __session = None

    def __init__(self):
        '''instantiate the engine'''
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', default='localhost')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == "test":
            Base.metatdata.drop_all(self.__engine)

    def all(self, cls=None):
        '''gets objects depending on the class name (argument cls)
        if cls=None, query all types of objects
        returns a dictionary of objects
        '''
        _cls = ["User", "State", "City", "Amenity", "Place", "Review"]
        dictionary = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            result = self.__session.query(cls)
            for obj in result:
                k = "{}.{}".format(type(obj).__name__, obj.id)
                dictionary[k] = obj
        else:
            for each in _cls:
                result = self.__session.query(eval(each))
                for obj in result:
                    k = "{}.{}".format(type(obj).__name__, obj.id)
                    dictionary[k] = obj
        return dictionary

    def new(self, obj):
        ''' add the object to the current database session'''
        self.__session.add(obj)

    def save(self):
        '''commit all changes of the current database session '''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete from the current database session obj if not None'''
        if obj:
            sefl.__session.delete()

    def reload(self):
        '''create all tables in the database '''
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
