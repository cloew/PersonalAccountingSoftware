from db.accounts import Accounts
from db.categories import Categories
from db.transactions import Transactions
from XML.account_element_factory import CreateAccountElement
from XML.category_element_factory import CreateCategoryElement
from XML.transaction_element_factory import CreateTransactionElement

from xml.dom.minidom import parseString
from xml.etree.ElementTree import Element, tostring, SubElement

def Export():
    """ Export the PAS Database """
    pasElement = Element("pas")
    
    AddAccountElements(pasElement)
    AddCategoryElements(pasElement)
    AddTransactionElements(pasElement)
      
    SaveXMLFile(pasElement)
    
def AddAccountElements(pasElement):
    """ Add Account Elements to the parent element """
    accountsElement = SubElement(pasElement, "accounts")
    
    for account in Accounts.all():
        accountElement = CreateAccountElement(account)
        accountsElement.append(accountElement)
        
def AddCategoryElements(pasElement):
    """ Add Category Elements to the parent element """
    categoriesElement = SubElement(pasElement, "categories")
    
    for category in Categories.all():
        categoryElement = CreateCategoryElement(category)
        categoriesElement.append(categoryElement)
        
def AddTransactionElements(pasElement):
    """ Add Transaction Elements to the parent element """
    transactionsElement = SubElement(pasElement, "transactions")
    
    for transaction in Transactions.all():
        transactionElement = CreateTransactionElement(transaction)
        transactionsElement.append(transactionElement)
        
def SaveXMLFile(root):
    """ Save the XML from the given root into a file """ 
    xmlString = tostring(root)
    domXML = parseString(xmlString)
    prettyXMLString = domXML.toprettyxml()
    
    with open("export.xml", 'w') as exportFile:
        exportFile.write(prettyXMLString)