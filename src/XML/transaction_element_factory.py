from db.transactions import Transactions
from xml.etree.ElementTree import Element, SubElement

def CreateTransactionElements():
    """ Create Transaction Elements to the parent element """
    transactionsElement = Element("transactions")
    
    for transaction in Transactions.all():
        transactionElement = CreateTransactionElement(transaction)
        transactionsElement.append(transactionElement)
        
    return transactionsElement

def CreateTransactionElement(transaction):
    """ Create the Transaction XML Element for the given account """
    transactionElement = Element("transaction")
    
    amountElement = SubElement(transactionElement, "amount")
    amountElement.text = str(transaction.amount)
    
    descriptionElement = SubElement(transactionElement, "description")
    descriptionElement.text = transaction.description
    
    incomeElement = SubElement(transactionElement, "income")
    incomeElement.text = str(transaction.income)
    
    dateElement = SubElement(transactionElement, "date")
    dateElement.text = transaction.dateString
    
    clearedElement = SubElement(transactionElement, "cleared")
    clearedElement.text = str(transaction.cleared)
    
    reconciledElement = SubElement(transactionElement, "reconciled")
    reconciledElement.text = str(transaction.reconciled)
    
    if transaction.category:
        categoryElement = SubElement(transactionElement, "category")
        categoryElement.text = transaction.category.name
    
    if transaction.isTransfer():
        transferElement = SubElement(transactionElement, "transfer")
        transferElement.text = str(transaction.transferAccount.name)
    
    return transactionElement