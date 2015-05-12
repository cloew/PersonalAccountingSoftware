from .table_wrapper import TableWrapper
from ORM.subtransaction_set import SubtransactionSet

class SubtransactionSetsWrapper(TableWrapper):
    """ Class to wrap interaction to the Subtransaction Set's table in the database """
    table_class = SubtransactionSet

SubtransactionSets = SubtransactionSetsWrapper()