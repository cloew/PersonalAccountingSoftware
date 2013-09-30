from db.subtransactions import SubTransactions
from db.transactions import Transactions
from ORM.subtransaction import SubTransaction

from xml.etree.ElementTree import Element, SubElement

def CreateSubTransactionElements():
    """ Create SubTransaction Elements to the parent element """
    subtransactionsElement = Element("subtransaction_sets")
    
    for subtransaction_set in SubTransactions.all():
        subtransactionElement = CreateSubTransactionElement(subtransaction_set)
        subtransactionsElement.append(subtransactionElement)
        
    return subtransactionsElement

def CreateSubTransactionElement(subtransaction_set):
    """ Create the SubTransaction XML Element for the given subtransaction set """
    subtransactionElement = Element("subtransaction_set")
    
    for transaction in subtransaction_set.transactions:
        transactionElement = SubElement(subtransactionElement, "transaction")
        transactionElement.text = str(transaction.id)
    
    return subtransactionElement
    
def LoadSubTransactions(parentElement):
    """ Load all subtransactions from the XML """
    subtransactionsElement = parentElement.find("subtransaction_sets")
    if subtransactionsElement is not None:
        for subtransactionElement in subtransactionsElement.findall("subtransaction_set"):
            LoadSubTransaction(subtransactionElement)
    
def LoadSubTransaction(subtransactionElement):
    """ Load a subtransaction from XML """
    subtransaction_set = SubTransaction()
    SubTransactions.add(subtransaction_set)
    
    for transactionElement in subtransactionElement.findall("transaction"):
        id = int(transactionElement.text)
        transaction = Transactions.findById(id)
        if transaction:
            subtransaction_set.transactions.append(transaction)
            
    SubTransactions.save()
    Transactions.save()