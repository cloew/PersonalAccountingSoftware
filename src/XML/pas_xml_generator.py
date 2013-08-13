from db.accounts import Accounts
from XML.account_element_factory import CreateAccountElement

from xml.dom.minidom import parseString
from xml.etree.ElementTree import Element, tostring, SubElement

def Export():
    """ Export the PAS Database """
    pasElement = Element("pas")
    accountsElement = SubElement(pasElement, "accounts")
    
    for account in Accounts.all():
        accountElement = CreateAccountElement(account)
        accountsElement.append(accountElement)
      
    SaveXMLFile(pasElement)
        
def SaveXMLFile(root):
    """ Save the XML from the given root into a file """ 
    xmlString = tostring(root)
    domXML = parseString(xmlString)
    prettyXMLString = domXML.toprettyxml()
    
    with open("export.xml", 'w') as exportFile:
        exportFile.write(prettyXMLString)