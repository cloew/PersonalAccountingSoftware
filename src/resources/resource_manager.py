import os

def GetResourceFilePath(resource_file):
    """ Returns a valid path to a resource file """
    resourceDirectory = os.path.dirname(__file__)
    return os.path.join(resourceDirectory, resource_file)