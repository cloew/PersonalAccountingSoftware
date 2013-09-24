from orm_base import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship, backref

class SubTransaction(Base):
    """ Represents a Financial Transaction. """
    __tablename__ = 'subtransactions'

    # Database Columns
    id = Column(Integer, primary_key = True)

    def __repr__(self):
        return "<SubTransaction()>"