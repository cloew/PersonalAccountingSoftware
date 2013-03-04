from contextlib import contextmanager
from database import Database

from ORM.transaction import Transaction

class TransactionsWrapper:
    """ Class to wrap interaction to the Transactions table in the database """

    def __init__(self):
        """ Initialize the Transactions Wrapper """

    def add(self, transaction):
        """ Add Transaction to the database """
        with self.session() as session:
            session.add(transaction)

    def save(self):
        """ Update the given transaction """
        with self.session() as session:
            pass

    def find(self, transaction):
        """ Returns the matching entry in the database """
        db_transaction_record = None
        with self.session() as session:
            db_transaction_record = session.query(Transaction).filter_by(id=transaction.id).first()
        return db_transaction_record

    def allTransactions(self):
        """ Returns all transactions from the database """

    @contextmanager
    def session(self):
        """ Returns the session """ # Need to add Exception handling
        session = Database.getSession()
        yield session
        session.commit()

Transactions = TransactionsWrapper()