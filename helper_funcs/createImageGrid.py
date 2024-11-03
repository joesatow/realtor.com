from PIL import Image
from . import constants
import os

homePath = constants.HOME_PATH

def createImage(chartSaveFolder):
    fileList = absoluteFilePaths(f"{homePath}/images/{chartSaveFolder}")
    rearrangedList = rearrangeFileList(fileList) 
    
    img_01 = Image.open(rearrangedList[0])
    img_02 = Image.open(rearrangedList[1])
    img_03 = Image.open(rearrangedList[2])
    img_04 = Image.open(rearrangedList[3])

    img_01_size = img_01.size

    pad = 1 # Thickness of divider line
    new_im = Image.new('RGB', (2*img_01_size[0]+pad,2*img_01_size[1]+pad), (0,0,0))
    
    new_im.paste(img_01, (0,0))
    new_im.paste(img_02, (img_01_size[0]+pad,0))
    new_im.paste(img_03, (0,img_01_size[1]+pad))
    new_im.paste(img_04, (img_01_size[0]+pad,img_01_size[1]+pad))
    
    new_im.save(f"{homePath}/images/results/grid-{chartSaveFolder}.png", "PNG")

def rearrangeFileList(fileList):
    newList = [None] * 4
    for filename in fileList:
        if "1w" in filename:
            newList[0] = filename
        if "1d" in filename:
            newList[1] = filename
        if "4h" in filename:
            newList[2] = filename
        if "1h" in filename:
            newList[3] = filename
    return newList

def absoluteFilePaths(directory):
    files = []
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            files.append(os.path.abspath(os.path.join(dirpath, f)))
    return files