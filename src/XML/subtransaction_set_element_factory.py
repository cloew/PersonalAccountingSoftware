from db.subtransaction_sets import SubtransactionSets
from db.transactions import Transactions
from ORM.subtransaction_set import SubtransactionSet

from xml.etree.ElementTree import Element, SubElement

def CreateSubtransactionSetElements():
    """ Create Subtransaction Set Elements to the parent element """
    subtransactionSetsElement = Element("subtransaction_sets")
    
    for subtransaction_set in SubTransactions.all():
        subtransactionSetElement = CreateSubtransactionSetElement(subtransaction_set)
        subtransactionSetsElement.append(subtransactionSetElement)
        
    return subtransactionSetsElement

def CreateSubtransactionSetElement(subtransaction_set):
    """ Create the Subtransaction Set XML Element for the given subtransaction set """
    subtransactionSetElement = Element("subtransaction_set")
    
    for transaction in subtransaction_set.transactions:
        transactionElement = SubElement(subtransactionSetElement, "transaction")
        transactionElement.text = str(transaction.id)
    
    return subtransactionSetElement
    
def LoadSubtransactionSets(parentElement):
    """ Load all subtransaction sets from the XML """
    subtransactionSetsElement = parentElement.find("subtransaction_sets")
    if subtransactionSetsElement is not None:
        for subtransactionSetElement in subtransactionSetsElement.findall("subtransaction_set"):
            LoadSubtransactionSet(subtransactionSetElement)
    
def LoadSubtransactionSet(subtransactionSetElement):
    """ Load a subtransaction set from XML """
    subtransaction_set = SubtransactionSet()
    SubtransactionSets.add(subtransaction_set)
    
    for transactionElement in subtransactionSetElement.findall("transaction"):
        id = int(transactionElement.text)
        transaction = Transactions.findById(id)
        if transaction:
            subtransaction_set.transactions.append(transaction)
            
    SubtransactionSets.save()
    Transactions.save()