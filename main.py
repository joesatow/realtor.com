from helper_funcs.folderFunctions import runFolderChecks, makeResultFolder
from helper_funcs.downloadSCfile import get_chart
from helper_funcs.createImageGrid import createImage
import time

chartSaveFolder = int(time.time())

runFolderChecks()
makeResultFolder(chartSaveFolder)

get_chart('AAPL', '1h', chartSaveFolder)
get_chart('AAPL', '4h', chartSaveFolder)
get_chart('AAPL', '1d', chartSaveFolder)
get_chart('AAPL', '1w', chartSaveFolder)

createImage(chartSaveFolder)