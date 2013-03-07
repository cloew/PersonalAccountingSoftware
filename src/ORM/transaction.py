from orm_base import Base
from sqlalchemy import Boolean, Column, Date, Integer, String

class Transaction(Base):
    """ Represents a Financial Transaction. """
    __tablename__ = 'transactions'

    # Database Columns
    id = Column(Integer, primary_key = True)
    amount = Column(Integer) # In cents
    description = Column(String)
    income = Column(Boolean)
    date = Column(Date)

    def __repr__(self):
        return "<Transaction('{0}', '${1}.{2}', '{3}')>".format(self.description, self.amount/100.0, self.amount%100, self.date)