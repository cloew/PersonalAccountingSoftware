from xml.etree.ElementTree import Element, SubElement

def CreateAccountElement(account):
    """ Create the Account XML Element for the given account """
    accountElement = Element("account")
    
    nameElement = SubElement(accountElement, "name")
    nameElement.text = account.name
    
    startingBalalanceElement = SubElement(accountElement, "starting")
    startingBalalanceElement.text = str(account.starting_balance)
    
    return accountElement