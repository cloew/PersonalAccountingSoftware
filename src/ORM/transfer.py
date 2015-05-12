from .transaction import Transaction
from .orm_base import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship, backref

class Transfer(Base):
    """ Represents a Transaction that is transferred to another account. """
    __tablename__ = 'transfers'

    # Database Columns
    id = Column(Integer, primary_key = True)
    transaction_id = Column(Integer, ForeignKey('transactions.id'))
    transaction = relationship("Transaction", backref=backref('transfers'))
    account_id = Column(Integer, ForeignKey('accounts.id'))
    account = relationship("Account", backref=backref('transfers'))

    def __repr__(self):
        return "<Transfer('{0}' transfered to/from '{1}')>".format(self.transaction, self.account)