from orm_base import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship, backref

class SubTransaction(Base):
    """ Represents a Financial Transaction. """
    __tablename__ = 'subtransactions'

    # Database Columns
    id = Column(Integer, primary_key = True)

    def getValue(self, account=None):
        """ Return the net value of the subtransaction """
        amount = 0
        for subtransaction in self.transactions:
            amount += subtransaction.getValue()
        return amount
    
    def __repr__(self):
        return "<SubTransaction()>"