import os

def GetResourceFilePath(resource_file):
    """ Returns a valid path to a resource file """
    resourceDirectory = GetResourceDirectory()
    full_path = os.path.join(resourceDirectory, resource_file)
    rel_path = os.path.relpath(full_path, os.getcwd())
    return rel_path
    
def GetResourceDirectory():
    """ Returns the proper Resource Directory """
    resourceDirectory = os.path.dirname(__file__)
    print "Resource Directory", resourceDirectory
    if not os.path.isdir(resourceDirectory):
        print "Resource Directory does not exist"
        resourceDirectory = FindFirstRealDirectory(resourceDirectory)
    return resourceDirectory
    
def FindFirstRealDirectory(resourceDirectory):
    """ Finds the First Real Driectory in the resourceDirectory path """
    resourceParentDirectory = resourceDirectory
    while not os.path.isdir(resourceParentDirectory):
        resourceParentDirectory = os.path.split(resourceParentDirectory)[0]
    resourceDirectory = os.path.join(resourceParentDirectory, "resources")
    
    if not os.path.isdir(resourceDirectory):
        print resourceDirectory, "does not exist" 
        os.mkdir(resourceDirectory)
    return resourceDirectory