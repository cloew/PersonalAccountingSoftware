from db.accounts import Accounts
from db.categories import Categories
from db.transactions import Transactions
from db.transfers import Transfers
from ORM.transaction import Transaction
from ORM.transfer import Transfer
from Utilities.date_helper import DateToString, StringToDate

from xml.etree.ElementTree import Element, SubElement

def CreateTransactionElements():
    """ Create Transaction Elements to the parent element """
    transactionsElement = Element("transactions")
    
    for transaction in Transactions.all():
        transactionElement = CreateTransactionElement(transaction)
        transactionsElement.append(transactionElement)
        
    return transactionsElement

def CreateTransactionElement(transaction):
    """ Create the Transaction XML Element for the given transaction """
    transactionElement = Element("transaction")
    
    idElement = SubElement(transactionElement, "id")
    idElement.text = str(transaction.id)
    
    amountElement = SubElement(transactionElement, "amount")
    amountElement.text = str(transaction.amount)
    
    descriptionElement = SubElement(transactionElement, "description")
    descriptionElement.text = transaction.description
    
    incomeElement = SubElement(transactionElement, "income")
    incomeElement.text = str(transaction.income)
    
    dateElement = SubElement(transactionElement, "date")
    dateElement.text = DateToString(transaction.date)
    
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
    idText = transactionElement.findtext("id")
    amount = int(transactionElement.findtext("amount"))
    description = transactionElement.findtext("description")
    income = StringToBoolean(transactionElement.findtext("income"))
    date = StringToDate(transactionElement.findtext("date"))
    cleared = StringToBoolean(transactionElement.findtext("cleared"))
    reconciled = StringToBoolean(transactionElement.findtext("reconciled"))
    accountName = transactionElement.findtext("account")
    categoryName = transactionElement.findtext("category")
    transferAccountName = transactionElement.findtext("transfer")
    
    if idText is not None:
        transaction = Transaction(id=int(idText), amount=amount, description=description, date=date, income=income, cleared=cleared, reconciled=reconciled)
    else:
        transaction = Transaction(amount=amount, description=description, date=date, income=income, cleared=cleared, reconciled=reconciled)
    
    if accountName:
        account = Accounts.accountWithName(accountName)
        transaction.account = account
    
    if categoryName:
        category = Categories.findByName(categoryName)
        transaction.category = category
        
    Transactions.add(transaction)
        
    if transferAccountName:
        transferAccount = Accounts.accountWithName(transferAccountName)
        transfer = Transfer(transaction=transaction, account=transferAccount)
        transaction.transferAccounts = [transferAccount]
        Transfers.add(transfer)
    
def StringToBoolean(someString):
    """ Convert a String to a Boolean """
    return someString == "True"