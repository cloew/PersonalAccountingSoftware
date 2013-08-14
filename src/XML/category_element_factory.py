from xml.etree.ElementTree import Element, SubElement

def CreateCategoryElement(category):
    """ Create the Category XML Element for the given account """
    categoryElement = Element("category")
    
    nameElement = SubElement(categoryElement, "name")
    nameElement.text = category.name
    
    return categoryElement