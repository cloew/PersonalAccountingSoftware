from orm_base import Base
from sqlalchemy import Column, Integer, String

class Transaction(Base):
    """ Represents a Financial Transaction. """
    __tablename__ = 'transactions'

    # Database Columns
    id = Column(Integer, primary_key = True)
    name = Column(String)

    def __init__(self, name):
        """ Initialize the Transaction """
        self.name = name

    def __repr__(self):
        return "<Transaction('{0}')>".format(self.name)