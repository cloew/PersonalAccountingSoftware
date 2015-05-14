from .orm_base import Base
from Utilities.date_helper import DateToString
from Utilities.dollar_amount_helper import GetDollarString

from sqlalchemy import Column, Date, Integer, String

class Account(Base):
    """ Represents a Financial Account. """
    __tablename__ = 'accounts'

    # Database Columns
    id = Column(Integer, primary_key = True)
    name = Column(String)
    initial_balance = Column(Integer) # In cents
    initial_balance_date = Column(Date)
    
    @property
    def initialBalanceInDollars(self):
        """ Return the initial balance in dollars """
        return GetDollarString(self.initial_balance)
    
    @property
    def initialBalanceDateString(self):
        """ Return the initial balance in dollars """
        return DateToString(self.initial_balance_date)

    def __repr__(self):
        return "<Account('{0}', '{1}' as of {2})>".format(self.name, self.initialBalanceInDollars, self.initialBalanceDateString)