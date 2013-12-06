from subtransaction import SubTransaction
from transaction import Transaction

from db.subtransactions import SubTransactions
from db.transactions import Transactions

import datetime

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
    
def CreateSubtransactionFromRelative(relative):
    """ Creates a Subtransaction From its Relative Transaction """
    transaction = Transaction(date=datetime.date.today())
    transaction.subtransaction_set = GetOrCreateSubtransactionSet(relative)
    transaction.account = relative.account
    
    Transactions.add(transaction)
    Transactions.save()
    return transaction