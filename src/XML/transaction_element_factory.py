from db.accounts import Accounts
from db.categories import Categories
from db.transactions import Transactions
from ORM.transaction import Transaction
from xml.etree.ElementTree import Element, SubElement

from dateutil import parser

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
    
    if transaction.account:
        accountElement = SubElement(transactionElement, "account")
        accountElement.text = transaction.account.name
    
    if transaction.category:
        categoryElement = SubElement(transactionElement, "category")
        categoryElement.text = transaction.category.name
    
    if transaction.isTransfer():
        transferElement = SubElement(transactionElement, "transfer")
        transferElement.text = str(transaction.transferAccount.name)
    
    return transactionElement
    
def LoadTransactions(parentElement):
    """ Load all transactions from the XML """
    transactionsElement = parentElement.find("transactions")
    for transactionElement in transactionsElement.findall("transaction"):
        LoadTransaction(transactionElement)
    
def LoadTransaction(transactionElement):
    """ Load a transaction from XML """
    amount = int(transactionElement.findtext("amount"))
    description = transactionElement.findtext("description")
    income = StringToBoolean(transactionElement.findtext("income"))
    date = parser.parse(transactionElement.findtext("date"))
    cleared = StringToBoolean(transactionElement.findtext("cleared"))
    reconciled = StringToBoolean(transactionElement.findtext("reconciled"))
    accountName = transactionElement.findtext("account")
    categoryName = transactionElement.findtext("category")
    transferAccountName = transactionElement.findtext("transfer")
    
    transaction = Transaction(amount=amount, description=description, date=date, income=income, cleared=cleared, reconciled=reconciled)
    
    if accountName:
        account = Accounts.accountWithName(accountName)
        transaction.account = account
    
    if categoryName:
        category = Categories.findByName(categoryName)
        transaction.category = category
        
    if transferAccountName:
        transferAccount = Accounts.accountWithName(transferAccountName)
        transaction.transferAccounts = [transferAccount]
    
    Transactions.add(transaction)
    
def StringToBoolean(someString):
    """ Convert a String to a Boolean """
    return someString == "True"