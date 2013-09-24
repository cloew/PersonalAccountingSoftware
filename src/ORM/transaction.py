from account import Account
from category import Category
from subtransaction import SubTransaction
from orm_base import Base
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
#from transfers import association_table as transfers_table

class Transaction(Base):
    """ Represents a Financial Transaction. """
    __tablename__ = 'transactions'

    # Database Columns
    id = Column(Integer, primary_key = True)
    amount = Column(Integer) # In cents
    description = Column(String)
    income = Column(Boolean)
    cleared = Column(Boolean)
    reconciled = Column(Boolean)
    date = Column(Date)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    account = relationship("Account", backref=backref('transactions'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", backref=backref('transactions'))
    subtransaction_set_id = Column(Integer, ForeignKey('subtransactions.id'))
    subtransaction_set = relationship("SubTransaction", backref=backref('transactions'))
    # transferAccounts = relationship("Account",
                                    # secondary=transfers_table,
                                    # backref="transfers")
                                    
    def isIncome(self, account=None):
        """ Returns if the transaction is income for the given account """
        if self.account is account or account is None:
            return self.income is True
        else:
            return self.income is False or self.income is None
            
    def isTransfer(self):
        """ Returns if the transaction is a transfer """
        return not self.transfers == []
        
    def getValue(self, account=None):
        """ Return the value in cents of the transaction taking into account whether it is an Expense """
        amount = 0
        if self.isIncome(account):
            amount += self.amount
        else:
            amount -= self.amount
        return amount
        
    @property
    def dateString(self):
        """ Return the Transaction date string """
        return "{0:%m/%d/%Y}".format(self.date)
        
    @property
    def transfer(self):
        """ Return the Transfer the Transaction is associated with """
        if self.isTransfer():
            return self.transfers[0]
        
    @property
    def transferAccount(self):
        """ Return the Account the Transaction is transferrred to/from """
        if self.isTransfer():
            return self.transfer.account

    def __repr__(self):
        return "<Transaction('{0}', '${1}.{2}', '{3}', '{4}', '{5}')>".format(self.description, self.amount/100.0, self.amount%100, self.dateString, self.category, self.cleared)
