import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../web_server/listing_exec_app'))

from lib import *
from lib.plot import *
import matplotlib.pyplot as pyplot


def generatePyResultImages():
	listingLoc = "../../web_server/listing_exec_app/lib/default_code/ch_13/"
	imageLoc = "../../../../../regression_tests/Code_Listings/Ch13_PyImages/"
	imageFormat = ".png"
	os.chdir(listingLoc)

	# Listing 13.1
	execfile("Listing_13_1.py")
	pyplot.savefig(imageLoc + "Listing_13_1" + imageFormat)
	pyplot.clf()

generatePyResultImages()
