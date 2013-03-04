from contextlib import contextmanager
from database import Database

class TransactionsWrapper:
    """ Class to wrap interaction to the Transactions table in the database """

    def __init__(self):
        """ Initialize the Transactions Wrapper """

    def add(self, transaction):
        """ Add Transaction to the database """
        with self.session() as session:
            session.add(transaction)

    def update(self, transaction):
        """ Update the given transaction """


    def allTransactions(self):
        """ Returns all transactions from the database """

    @contextmanager
    def session(self):
        """ Returns the session """ # Need to add Exception handling
        session = Database.getSession()
        yield session
        session.commit()
        session.close()

Transactions = TransactionsWrapper()