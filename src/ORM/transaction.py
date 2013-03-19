from account import Account
from category import Category
from orm_base import Base
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
# from transaction_category_join_table import association_table as join_table

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
    # categories = relationship("Category",
    #                 secondary=join_table,
    #                 backref="transactions")

    def __repr__(self):
        return "<Transaction('{0}', '${1}.{2}', '{3}', '{4}', '{5}')>".format(self.description, self.amount/100.0, self.amount%100, self.date, self.category, self.cleared)