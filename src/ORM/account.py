from orm_base import Base
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String

class Account(Base):
    """ Represents a Financial Account. """
    __tablename__ = 'accounts'

    # Database Columns
    id = Column(Integer, primary_key = True)
    name = Column(String)
    starting_balance = Column(Integer) # In cents

    def __repr__(self):
        return "<Account('{0}', '${1}.{2}')>".format(self.name, self.starting_balance/100.0, self.starting_balance%100)