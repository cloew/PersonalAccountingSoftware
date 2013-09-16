from db.accounts import Accounts
from ORM.account import Account
from Utilities.date_helper import DateToString, StringToDate

from xml.etree.ElementTree import Element, SubElement

def CreateAccountElements():
    """ Create Account Elements to the parent element """
    accountsElement = Element("accounts")
    
    for account in Accounts.all():
        accountElement = CreateAccountElement(account)
        accountsElement.append(accountElement)
        
    return accountsElement

def CreateAccountElement(account):
    """ Create the Account XML Element for the given account """
    accountElement = Element("account")
    
    nameElement = SubElement(accountElement, "name")
    nameElement.text = account.name
    
    initialBalalanceElement = SubElement(accountElement, "initial_balance")
    initialBalalanceElement.text = str(account.initial_balance)
    
    dateElement = SubElement(accountElement, "date")
    dateElement.text = DateToString(account.initial_balance_date)
    
    return accountElement

def LoadAccounts(parentElement):
    """ Load all accounts from the XML """
    accountsElement = parentElement.find("accounts")
    for accountElement in accountsElement.findall("account"):
        LoadAccount(accountElement)
    
def LoadAccount(accountElement):
    """ Load an account from XML """
    name = accountElement.findtext("name")
    initialBalance = int(accountElement.findtext("initial_balance"))
    date = StringToDate(accountElement.findtext("date"))
    
    account = Account(name=name, initial_balance=initialBalance, initial_balance_date=date) 
    Accounts.add(account)