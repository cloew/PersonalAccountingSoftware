from db.accounts import Accounts
from XML.account_element_factory import CreateAccountElement

from xml.etree.ElementTree import Element, ElementTree, SubElement

def Export():
    """ Export the PAS Database """
    pasElement = Element("pas")
    accountsElement = SubElement(pasElement, "accounts")
    
    for account in Accounts.all():
        accountElement = CreateAccountElement(account)
        accountsElement.append(accountElement)
        
    tree = ElementTree(pasElement)
    tree.write("export.xml")