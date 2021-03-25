import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    fullName = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    hair_color = Column(String(250))
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250))
    photoUrl = Column(String(500))

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(250))
    terrain = Column(String(250), nullable=False)
    weather = Column(String(250))
    photoUrl = Column(String(500))


class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_characters = Column(Integer, ForeignKey(Planets.id,Characters.id))
    id_planets = Column(String(50))
    users = relationship(Users)
    characters = relationship(Characters)


   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')