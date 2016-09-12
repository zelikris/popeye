import sys
import os
import getopt
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../web_server/listing_exec_app'))
from lib import *
from lib.plot import *
import matplotlib.pyplot as pyplot

# Import chapter modules here
import Code_Listings.Ch3 as Ch3
import Code_Listings.Ch4 as Ch4
import Code_Listings.Ch5 as Ch5
import Code_Listings.Ch11Plots as Ch11Plots
#import Ch11
import Code_Listings.Ch11 as Ch11
# import Code_Listings.Ch13 as Ch13
import RegressionGUI

import unittest

# Delta is used to define the acceptable amount of error when calculating
# floating point numbers
global DELTA
DELTA = 0.0001

# Message for negative/unsuccessful test
global NEG_RESULT
NEG_RESULT = " was unsuccessful."

global LOG_NAME
LOG_NAME = 'regression_test_results.txt'

# if -gui flag is entered, run RegressionGUI at the end.
#global runRegressionGUI
#runRegressionGUI = False
#opts, args = getopt.getopt(sys.argv[1:], "gui")
#if opts and "-gui" in opts[0]:
#    runRegressionGUI = True

# class Chapter2Listings(unittest.TestCase):
#     ''' This class will define all of the test cases for the Chapter 2 listings
#     '''

#     def test_listing_01(self):
#         self.assertEqual(Ch2.listing_01(), 5, msg = Ch2.listing_01.__name__ + NEG_RESULT)

#     def test_listing_02_03(self):
#         # Floating point aproximations might have a certain degree of error
#         self.assertAlmostEqual(Ch2.listing_02_03(), 1400.7141,
#                                 msg = Ch2.listing_02_03.__name__ + NEG_RESULT,
#                                delta=DELTA)

# class Chapter3Listings(unittest.TestCase):
# #     ''' This class will define all of the test cases for the Chapter 3 listings
# #     '''
#     def test_listing_01(self):
#          self.assertEqual(Ch3.listing_01(), vector([99, 5, 99, 1, 99, 4]), msg = Ch3.listing_01.__name__ + NEG_RESULT)

#     def test_listing_02(self):
#          self.assertEqual(Ch3.listing_02(), vector([1, 2, -5]), msg = Ch3.listing_02.__name__ + NEG_RESULT)

#     def test_listing_03(self):
#          self.assertEqual(Ch3.listing_03(), [vector([112, 5, 7, 113]), vector([111, 113, 14, 112])], msg = Ch3.listing_03.__name__ + NEG_RESULT)

#     def test_listing_04(self):
#          self.assertEqual(Ch3.listing_04(), 1117.5, msg = Ch3.listing_03.__name__ + NEG_RESULT)

class Chapter4Listings(unittest.TestCase):
    ''' This class will define all of the test cases for the Chapter 4 listings
    '''
    def test_listing_01(self):
        self.assertEqual(Ch4.Listing_01(1), "Weekend", msg = Ch4.Listing_01.__name__ + NEG_RESULT)
        self.assertEqual(Ch4.Listing_01(7), "Weekend", msg = Ch4.Listing_01.__name__ + NEG_RESULT)
        self.assertEqual(Ch4.Listing_01(3), "Weekday", msg = Ch4.Listing_01.__name__ + NEG_RESULT)
        self.assertEqual(Ch4.Listing_01(6), "Weekday", msg = Ch4.Listing_01.__name__ + NEG_RESULT)
    
    def test_listing_02(self):
        self.assertEqual(Ch4.Listing_02(100), 'A', msg = Ch4.Listing_02.__name__ + NEG_RESULT)
        self.assertEqual(Ch4.Listing_02(90), 'A', msg = Ch4.Listing_02.__name__ + NEG_RESULT)
        self.assertEqual(Ch4.Listing_02(85), 'B', msg = Ch4.Listing_02.__name__ + NEG_RESULT)
        self.assertEqual(Ch4.Listing_02(80), 'B', msg = Ch4.Listing_02.__name__ + NEG_RESULT)
        self.assertEqual(Ch4.Listing_02(75), 'C', msg = Ch4.Listing_02.__name__ + NEG_RESULT)
        self.assertEqual(Ch4.Listing_02(70), 'C', msg = Ch4.Listing_02.__name__ + NEG_RESULT)
        self.assertEqual(Ch4.Listing_02(65), 'D', msg = Ch4.Listing_02.__name__ + NEG_RESULT)
        self.assertEqual(Ch4.Listing_02(60), 'D', msg = Ch4.Listing_02.__name__ + NEG_RESULT)
        self.assertEqual(Ch4.Listing_02(55), 'F', msg = Ch4.Listing_02.__name__ + NEG_RESULT)

    def test_listing_03(self):
        self.assertEqual(Ch4.Listing_03([False, False, False]), [False, False, True], msg = Ch4.Listing_03.__name__ + NEG_RESULT)
        self.assertEqual(Ch4.Listing_03([False, False, True]), [False, False, True], msg = Ch4.Listing_03.__name__ + NEG_RESULT)
        self.assertEqual(Ch4.Listing_03([True, False, False]), [True, False, True], msg = Ch4.Listing_03.__name__ + NEG_RESULT)
        self.assertEqual(Ch4.Listing_03([False, True, False]), [False, True, True], msg = Ch4.Listing_03.__name__ + NEG_RESULT)
        self.assertEqual(Ch4.Listing_03([True, True, False]), [True, True, True], msg = Ch4.Listing_03.__name__ + NEG_RESULT)

    def test_listing_04(self):
        month = 2
        year = 2012        
        self.assertEqual(Ch4.Listing_04(month, year), 29)
        year = 2015
        self.assertEqual(Ch4.Listing_04(month, year), 28)
        month = 4
        self.assertEqual(Ch4.Listing_04(month, year), 30)
        month = 5
        self.assertEqual(Ch4.Listing_04(month, year), 31)
    def test_listing_05(self):
        a = (12, 43, 23, 52, 32, 12, 53, 24, 123, 4321, 52, 1412, 412, 1252)
        self.assertEquals(Ch4.Listing_05(a), 4321)        
    def test_listing_06(self):
        a = (12, 43, 23, 52, 32, 12, 53, 24, 123, 4321, 52, 1412, 412, 1252)
        self.assertEqual(Ch4.Listing_06(a), 9)
        
    def test_listing_07a(self):
        A = [61, 38, 45, 65, 27, 66, 88, 97, 11, 23]
        self.assertEqual(Ch4.Listing_07(A), 7, msg = Ch4.Listing_07.__name__ + NEG_RESULT)
    def test_listing_07b(self):
        A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(Ch4.Listing_07(A), 0, msg = Ch4.Listing_07.__name__ + NEG_RESULT)
    def test_listing_07c(self):
        A = [10, 10, 10, 10, 10, 10, 10, 10, 10, 11]
        self.assertEqual(Ch4.Listing_07(A), 9, msg = Ch4.Listing_07.__name__ + NEG_RESULT)
    def test_listing_07d(self):
        A = [10, 10, 10, 10, 11, 10, 10, 10, 10, 10]
        self.assertEqual(Ch4.Listing_07(A), 4, msg = Ch4.Listing_07.__name__ + NEG_RESULT)
        print('----------------------------------------------------------------------')
    def test_listing_08a(self):
        self.assertEqual(Ch4.Listing_08(1), 'radius = 1; area = 3.14; circum = 6.28', msg = Ch4.Listing_08.__name__ + NEG_RESULT)
    def test_listing_08b(self):
        self.assertEqual(Ch4.Listing_08(30), 'radius = 30; area = 2827.43; circum = 188.50', msg = Ch4.Listing_08.__name__ + NEG_RESULT)
    def test_listing_08c(self):
        self.assertEqual(Ch4.Listing_08(100), 'radius = 100; area = 31415.93; circum = 628.32', msg = Ch4.Listing_08.__name__ + NEG_RESULT)
        print('----------------------------------------------------------------------')
    def test_listing_09a(self):
        self.assertEqual(Ch4.Listing_09(10, 5, 3), 'rad 5.00 ht 10.00 level 3.00 vol 113.10', msg = Ch4.Listing_09.__name__ + NEG_RESULT)
    def test_listing_09b(self):
        self.assertEqual(Ch4.Listing_09(0, 0, 0), 'rad 0.00 ht 0.00 level 0.00 vol 0.00', msg = Ch4.Listing_09.__name__ + NEG_RESULT)
    def test_listing_09c(self):
        self.assertEqual(Ch4.Listing_09(100, 5, 10), 'rad 5.00 ht 100.00 level 10.00 vol 654.50', msg = Ch4.Listing_09.__name__ + NEG_RESULT)
    def test_listing_09d(self):
        self.assertEqual(Ch4.Listing_09(5, 5, 10), 'liquid level too high', msg = Ch4.Listing_09.__name__ + NEG_RESULT)
        print('----------------------------------------------------------------------')

class Chapter5Listings(unittest.TestCase):
    ''' This class will define all of the test cases for the Chapter 4 listings
    '''
    def test_listing_01(self):
        self.assertEqual(Ch5.Listing_01(12,6), 1357.1680263507906)

    def test_listing_02(self):
        self.assertEqual(Ch5.Listing_02(12,6), {'volume': 1357.1680263507906, 'area': 2940.5307237600464})

class Chapter11Listings(unittest.TestCase):
    ''' This class will define all of the test cases for the Chapter 11 listings
    '''
    def test_listing_5(self):
        self.assertEqual(Ch11Plots.Listing_5(), True, msg = Ch11Plots.Listing_5.__name__ + NEG_RESULT)
    def test_listing_9(self):
        self.assertEqual(Ch11Plots.Listing_9(), True, msg = Ch11Plots.Listing_9.__name__ + NEG_RESULT)
    def test_listing_10(self):
        self.assertEqual(Ch11Plots.Listing_10(), True, msg = Ch11Plots.Listing_10.__name__ + NEG_RESULT)
    def test_listing_12(self):
        self.assertEqual(Ch11Plots.Listing_12(), True, msg = Ch11Plots.Listing_12.__name__ + NEG_RESULT)
    def test_listing_13(self):
        self.assertEqual(Ch11Plots.Listing_13(), True, msg = Ch11Plots.Listing_13.__name__ + NEG_RESULT)
    def test_listing_16(self):
        self.assertEqual(Ch11Plots.Listing_16(), True, msg = Ch11Plots.Listing_16.__name__ + NEG_RESULT)

    #def test_listing_02(self):
    #    if runRegressionGUI:
    #        execfile("RegressionGUI.py")

if __name__ == "__main__": # If this module is the staring program...
   # ... then execute the following:
   log_file = open(LOG_NAME, "w")
   runner = unittest.TextTestRunner(log_file) # Output unit test info to file
   unittest.main(testRunner=runner)
   log_file.close()
   print "Done running regression tests."
