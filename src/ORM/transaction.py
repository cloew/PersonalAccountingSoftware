from category import Category
from orm_base import Base
from sqlalchemy import Boolean, Column, Date, Integer, String
from sqlalchemy.orm import relationship, backref
from transaction_category_join_table import association_table as join_table

class Transaction(Base):
    """ Represents a Financial Transaction. """
    __tablename__ = 'transactions'

    # Database Columns
    id = Column(Integer, primary_key = True)
    amount = Column(Integer) # In cents
    description = Column(String)
    income = Column(Boolean)
    date = Column(Date)
    categories = relationship("Category",
                    secondary=join_table,
                    backref="transactions")

    def __repr__(self):
        return "<Transaction('{0}', '${1}.{2}', '{3}')>".format(self.description, self.amount/100.0, self.amount%100, self.date)