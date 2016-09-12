import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../web_server/listing_exec_app'))

from lib import *
from lib.plot import *
import matplotlib.pyplot as pyplot

# used for converting .jpg to .gif
#import Image
# import Image

def generatePyResultImages():
    listings = [1, 2, 3, 5, 6, 8, 9, 10, 12, 13, 16]
    listingLoc = "../web_server/listing_exec_app/lib/default_code/ch_11/"
    imageLoc = "../../../../../regression_tests/Code_Listings/Ch11_PyImages/"
    imageFormat = ".gif"
    os.chdir(listingLoc)

    for listing in listings:
        listingNum = str(listing)
        fileName = "Listing_11_" + listingNum + ".py"
        execfile(fileName)

        imageName = imageLoc + "Listing_11_" + listingNum + imageFormat
        pyplot.savefig(imageName)
        pyplot.clf()
        
        # convert from jpg to gif for regression GUI.  The regression GUI is
        # built on Tk.  Tk does not support a lot of formats.  It does support
        # .gif.  Rather than mess with another lib, convert it to something
        # that tk will understand.
        imageNameGif = imageName.replace(imageFormat, ".gif")

        #Image.open(imageName).save(imageNameGif)
        # Image.open(imageName).save(imageNameGif)
    os.chdir("../../../../../regression_tests/")
