from XML.pas_xml_generator import Export

from shutil import copy

import os
import sys

def GetBackupDirectory():
    """ Returns the backup directory and creates it if it does not exist already """
    directory = os.path.join(os.path.dirname(__file__), "../../PASBackups")
    if not os.path.exists(directory):
        os.mkdir(directory)
    return directory
    
def CopyDatabase(destinationName):
    """ Copies the Database """
    CopyFile(os.path.join(os.path.dirname(__file__), "resources/pas.db"), destinationName, "db")
    
def CopyExport(destinationName):
    """ Copies the Export XML of the Database """
    Export()
    CopyFile("export.xml", destinationName, "xml")
    
def CopyFile(someFile, destinationName, extension):
    """ Copies the file to the Backup Directory """
    directory = GetBackupDirectory()
    destinationPath = os.path.join(directory, "{0}.{1}".format(destinationName, extension))
    copy(someFile, destinationPath)

def main(args):
    backupName = args[0]
    CopyDatabase(backupName)
    CopyExport(backupName)    

if __name__ ==  "__main__":
    main(sys.argv[1:])