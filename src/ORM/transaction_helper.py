from subtransaction import SubTransaction

from db.subtransactions import SubTransactions
from db.transactions import Transactions

def GetOrCreateSubtransactionSet(transaction):
    """ Get a Transaction's Subtransaction Set or create it if it doesn't exist """
    subtransaction_set = transaction.subtransaction_set
    if subtransaction_set is None:
        subtransaction_set = SubTransaction()
        SubTransactions.add(subtransaction_set)
        SubTransactions.save()
        transaction.subtransaction_set = subtransaction_set
        Transactions.add(transaction)
    
    return subtransaction_set