from .orm_base import Base
from Utilities.date_helper import DateToString
from Utilities.dollar_amount_helper import GetDollarString


from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String

class Account(Base):
    """ Represents a Financial Account. """
    __tablename__ = 'accounts'

    # Database Columns
    id = Column(Integer, primary_key = True)
    name = Column(String)
    initial_balance = Column(Integer) # In cents
    initial_balance_date = Column(Date)

    def __repr__(self):
        return "<Account('{0}', '{1}' as of {2})>".format(self.name, GetDollarString(self.initial_balance), DateToString(initial_balance_date))