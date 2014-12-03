from sqlalchemy import Column, Integer, String
from base import Base


class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    score = Column(Integer)
