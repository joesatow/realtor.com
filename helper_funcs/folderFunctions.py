import os
from . import constants

homePath = constants.HOME_PATH

def runFolderChecks():
    # Create folders if they don't exist
    if not os.path.exists(f"{homePath}/images"):
        os.makedirs(f"{homePath}/images")
    
    if not os.path.exists(f"{homePath}/images/results"):
        os.makedirs(f"{homePath}/images/results")

def makeResultFolder(folderName):
    os.makedirs(f"{homePath}/images/{folderName}")