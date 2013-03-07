# from orm_base import Base
# from sqlalchemy import Table, Column, ForeignKey, Integer

# association_table = Table('transaction_category_join', Base.metadata,
#     Column('transcation_id', Integer, ForeignKey('transactions.id')),
#     Column('category_id', Integer, ForeignKey('categories.id'))
# )