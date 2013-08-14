from db.accounts import Accounts
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
    
    startingBalalanceElement = SubElement(accountElement, "starting")
    startingBalalanceElement.text = str(account.starting_balance)
    
    return accountElement