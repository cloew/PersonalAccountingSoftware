from .table_wrapper import TableWrapper
from ORM.transfer import Transfer

class TransfersWrapper(TableWrapper):
    """ Class to wrap interaction to the Transfers table in the database """
    table_class = Transfer

Transfers = TransfersWrapper()