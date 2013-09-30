from XML.pas_xml_generator import Import

from version import VERSION

from shutil import copy

import os
import sys

def GetBackupDirectory():
    """ Returns the backup directory and creates it if it does not exist already """
    directory = os.path.join(os.path.dirname(__file__), "../../PASBackups")
    if not os.path.exists(directory):
        os.mkdir(directory)
    return directory

def CopyImport(importFilename):
    """ Copies the Export XML of the Database """
    CopyFile(importFilename, "export.xml", "xml")
    Import()
    
def CopyFile(importFilename, destination, extension):
    """ Copies the file to the Backup Directory """
    directory = GetBackupDirectory()
    importPath = os.path.join(directory, "{0}.{1}".format(importFilename, extension))
    copy(importPath, destination)

def main(args):
    if len(args) > 0:
        backupName = args[0]
    else:
        backupName = "version{0}".format(str(VERSION).replace(".", ""))
    CopyImport(backupName)  
    
if __name__ ==  "__main__":
    main(sys.argv[1:])