from db.transactions import Transactions
from XML.account_element_factory import CreateAccountElements, LoadAccounts
from XML.category_element_factory import CreateCategoryElements
from XML.transaction_element_factory import CreateTransactionElements

from xml.dom.minidom import parseString
from xml.etree.ElementTree import Element, tostring, SubElement, parse

def Export():
    """ Export the PAS Database """
    pasElement = Element("pas")
    
    elementGenerators = [CreateAccountElements, CreateCategoryElements, CreateTransactionElements]
    
    for elementGenerator in elementGenerators:
        element = elementGenerator()
        pasElement.append(element)
      
    SaveXMLFile(pasElement)
    
def Import():
    """ Load the PAS XML """
    xmlTree = parse("export.xml")
    root = xmlTree.getroot()
    
    dataLoaders = [LoadAccounts]#, LoadCategorys, LoadTransactions]
    
    for dataLoader in dataLoaders:
        dataLoader(root)
        
def SaveXMLFile(root):
    """ Save the XML from the given root into a file """ 
    xmlString = tostring(root)
    domXML = parseString(xmlString)
    prettyXMLString = domXML.toprettyxml()
    
    with open("export.xml", 'w') as exportFile:
        exportFile.write(prettyXMLString)