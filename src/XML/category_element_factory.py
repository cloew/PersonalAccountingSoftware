from db.categories import Categories
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