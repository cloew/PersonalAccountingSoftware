from .orm_base import Base
from sqlalchemy import Column, Integer, String

class Category(Base):
    """ Represents a Financial Transaction. """
    __tablename__ = 'categories'

    # Database Columns
    id = Column(Integer, primary_key = True)
    name = Column(String)

    def __repr__(self):
        return "<Category('{0}')>".format(self.name)