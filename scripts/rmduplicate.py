import os
import hashlib
from organizephotos import getpath

def rmduplicate(indir):

    while os.path.isdir(indir) == False:
        indir = getpath(True)
    
    print("Finding Duplicates")

    checksums = set()

    for i in os.listdir(indir):
        infile = indir + "/" + i
        #ignores non-files
        if os.path.isfile(infile) == False:
            continue
        #ignores non-image files
        if ((i.lower().endswith("jpg") == False) and (i.lower().endswith("jpeg") == False) and (i.lower().endswith("tif") == False) and (i.lower().endswith("tiff") == False) and (i.lower().endswith("cr2") == False) and (i.lower().endswith("nef") == False)):
            continue
        
        print("Checking " + infile)
        openfile = open(infile, "rb")
        readfile = openfile.read()

        sha1Hash = hashlib.sha1(readfile)
        sha1Hashed = sha1Hash.hexdigest()

        if (sha1Hashed in checksums):
            print("Deleting " + infile)
            print(sha1Hashed)
            os.remove(infile)
        else:
            checksums.add(sha1Hashed)


    print("Done")