from table_wrapper import TableWrapper
from ORM.subtransaction import SubTransaction

class SubTransactionsWrapper(TableWrapper):
    """ Class to wrap interaction to the Subtransactions table in the database """
    table_class = SubTransaction

SubTransactions = SubTransactionsWrapper()