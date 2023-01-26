# Model class
from sqlalchemy import Boolean, Column, Integer, String

from db_handler import Base


class Movies(Base):
    # Setting constraints on the table structure
    __tablename__ = "movie"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    movie_id = Column(String)
    movie_name = Column(String(255))
    director = Column(String(100))
    geners = Column(String)
    membership_required = Column(Boolean)
    cast = Column(String(255))
    streaming_platform = Column(String)


