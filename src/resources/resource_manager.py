import os

def GetResourceFilePath(resource_file):
    """ Returns a valid path to a resource file """
    resourceDirectory = os.path.dirname(__file__)
    full_path = os.path.join(resourceDirectory, resource_file)
    rel_path = os.path.relpath(full_path, os.getcwd())
    return rel_path