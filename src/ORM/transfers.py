from orm_base import Base
from sqlalchemy import Table, Column, ForeignKey, Integer

association_table = Table('transfers', Base.metadata,
    Column('transcation_id', Integer, ForeignKey('transactions.id')),
    Column('account_id', Integer, ForeignKey('accounts.id'))
)