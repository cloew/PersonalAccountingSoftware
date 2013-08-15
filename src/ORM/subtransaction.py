from transaction import Transaction
from orm_base import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship, backref

class SubTransaction(Base):
    """ Represents a Financial Transaction. """
    __tablename__ = 'subtransactions'

    # Database Columns
    id = Column(Integer, primary_key = True)
    transaction_id = Column(Integer, ForeignKey('transactions.id'))
    transaction = relationship("Transaction", foreign_keys=[transaction_id], backref=backref('subtransaction'))
    parent_transaction_id = Column(Integer, ForeignKey('transactions.id'))
    parent_transaction = relationship("Transaction", foreign_keys=[parent_transaction_id], backref=backref('childTransactions'))

    def __repr__(self):
        return "<SubTransaction('{0}' is related to '{1}')>".format(self.transaction, self.parent_transaction)