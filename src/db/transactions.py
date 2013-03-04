from database import Database

class TransactionsWrapper:
    """ Class to wrap interaction to the Transactions table in the database """

    def __init__(self):
        """ Initialize the Transactions Wrapper """

    def add(self, transaction):
        """ Add Transaction to the database """
        session = Database.getSession()
        session.add(transaction)
        session.commit()

    def update(self, transaction):
        """ Update the given transaction """


    def allTransactions(self):
        """ Returns all transactions from the database """

Transactions = TransactionsWrapper()