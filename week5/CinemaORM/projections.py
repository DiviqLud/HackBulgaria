from base import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Projection(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    movie_type = Column(String)
    date_time = Column(DateTime)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    movies = relationship("Movie", backref="projections")

    def __str__(self):
        return "{} - {} -({})".format(self.id, self.date_time, self.movie_type)

    def __repr__(self):
        return self.__str__()
