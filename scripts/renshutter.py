import os
import time
import exifread
from organizephotos import getpath

def renshutter(indir):
    
    while os.path.isdir(indir) == False:
        indir = getpath(True)

    print("Please specify a prefix (i.e. \"DSC_\")")
    prefix = input()

    for i in os.listdir(indir):
        
        infile = indir + "/" + i
        #ignores non-files
        if os.path.isfile(infile) == False:
            continue
        #ignores non-image files
        if ((i.lower().endswith("jpg") == False) and (i.lower().endswith("jpeg") == False) and (i.lower().endswith("tif") == False) and (i.lower().endswith("tiff") == False) and (i.lower().endswith("cr2") == False) and (i.lower().endswith("nef") == False)):
            continue
        
        file = open(infile, "rb")
        try:
            tags = exifread.process_file(file)
            shuttercount = str(tags["MakerNote TotalShutterReleases"])
        except:
            print("READ ERROR on file " + i + ": Cannot read EXIF - File is probably corrupt OR exif-py not installed")
            print("Please type <pip install exifread> to install exif-py")
        try:
            print("Renaming " + i + " to " + prefix + shuttercount + "." + i.split(".")[-1])
            os.rename(infile, indir + "/" + prefix + shuttercount + "." + i.split(".")[-1])
        except:
            print("WRITE ERROR ON " + i + ": Insufficient privileges?")

    print("Done")
    print("Press ENTER to exit")
    input()
