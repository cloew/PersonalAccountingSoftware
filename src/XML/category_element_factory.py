from db.categories import Categories
from ORM.category import Category
from xml.etree.ElementTree import Element, SubElement

def CreateCategoryElements():
    """ Create Category Elements to the parent element """
    categoriesElement = Element("categories")
    
    for category in Categories.all():
        categoryElement = CreateCategoryElement(category)
        categoriesElement.append(categoryElement)
        
    return categoriesElement

def CreateCategoryElement(category):
    """ Create the Category XML Element for the given account """
    categoryElement = Element("category")
    
    nameElement = SubElement(categoryElement, "name")
    nameElement.text = category.name
    
    return categoryElement
    
def LoadCategories(parentElement):
    """ Load all categories from the XML """
    categoriesElement = parentElement.find("categories")
    for categoryElement in categoriesElement.findall("category"):
        LoadCategory(categoryElement)
    
def LoadCategory(categoryElement):
    """ Load a category from XML """
    name = categoryElement.findtext("name")
    
    category = Category(name=name) 
    Categories.add(category)