from xml.etree.ElementTree import Element, SubElement

def CreateAccountElement(account):
    """ Create the Account XML ELement for the given account """
    accountElement = Element("account")
    
    nameElement = SubElement("name", accountElement)
    nameElement.text = account.name
    
    startingBalalanceElement = SubElement("starting", accountElement)
    startingBalalanceElement.text = str(account.startingBalance)
    
    return accountElement