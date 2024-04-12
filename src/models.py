import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(60), nullable=False)
    phone = Column(Integer)
    password = Column(String(40), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    diameter = Column(Integer)
    temperature = Column(Integer, nullable=False)
    description = Column(String(250))

class Characters(Base):
    __tablename__ = 'characters'
    character_id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)
    weight = Column(Integer)
    height = Column(Integer)

class Favorites(Base):
    __tablename__ = 'favorites'
    favorite_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.planet_id'))
    character_id = Column(Integer, ForeignKey('characters.character_id'))
    users = relationship("User", foreign_keys=[user_id])
    planets = relationship("Planets", foreign_keys=[planet_id])
    characters = relationship("Characters", foreign_keys=[character_id])

    def to_dict(self):
        return {}

render_er(Base, 'diagram.png')