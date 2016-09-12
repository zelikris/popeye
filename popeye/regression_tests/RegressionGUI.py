#!/usr/bin/env python

# ------------------------------ 
# The GUI is used for regression tests which involve comparing image data.  We
# simply display the images in a 2 column format such that the output code is
# in one column and the expected image from matlab is in the other
#
# USAGE:
#
#   # first create an instance of the regression testing application
#   app = RegTestApp()
#   # initialize the test data.  You can look to init_tests() for how this
#   # should be formatted. Don't be lazy.
#   app.init_tests(test_data)
#   # start the application
#   app.init_gui()
#
#   At this point, you can manually inspect and pass/fail each image test.  The
#   two images will be displayed side-by-side in a two column layout.  At the
#   end of the tests, a results screen will be shown.
#
# author: Brendan McGarry
# team:   Test Code Team
# ------------------------------ 

# TODO(Brendan):
#   [ ] Call script to autogenerate the images for the book
#   [ ] Call my script inside the regression test python file
#   [x] Update GUI on pass/fail
#   [x] Add params for regression class functions
#   [x] Dynamically update top label with the name of the test being run
#   [x] Display results of regression tests after all tests have been evaluated

import os
import sys

import PIL.ImageTk
import PIL.Image

#sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../web_server/listing_exec_app'))
#from lib import *
#from matplotlib import *

#import Code_Listings.Ch11 as Ch11

# GUI implemented with TK.  May need to install this on your system
#   sudo apt-get install python-tk
from Tkinter import *

# ------------------------------ 
#   CONSTANTS
# ------------------------------ 

# Default font size for the column labels:
# font size styling
DEFAULT_LABEL_FONT = "Helvetica 14 bold"

# Default title for the label at the top of the GUI.  The current regression
# test that is being evaluated will be displayed up here.
#
# NOTE(ALL): This is NOT the title that is displayed in the window decoration.
#            Refer to DEFAULT_TITLE for that.
DEFAULT_TEST = "default_test_1.py"
DEFAULT_TEST_FONT = "Helvetica 16 bold"

# Default title for the GUI- displayed in the window decoration
DEFAULT_TITLE = "Regression Testing Ch 11,13"

# Desired dimensions to display the photo in.  We either upscale or downscale
# each image so all the images look universal on the screen
IMAGE_HEIGHT = 400
IMAGE_WIDTH = 400

MINIMUM_HEIGHT = 400
MINIMUM_WIDTH  = 400

# ------------------------------ 
#   CLASS 
# ------------------------------ 

class RegTestApp:

    # ------------------------------ 
    #   VARIABLES
    # ------------------------------ 

    # Buttons for pass/fail.  When one of these buttons are pressed, the result
    # of the test is recorded and the next test is loaded into the GUI.
    btn_pass = None
    btn_fail = None

    # Canvases for displaying the images
    can_matlab = None
    can_python = None

    # Images to display in the canvases
    img_matlab = None
    img_pytho = None

    # Label which displays the current test.  To make the text of the label
    # dynamic, we use python-tk's StringVar() class and the textvariable
    # property of the label
    label_test = None
    label_test_text = None

    # Labels for the two column layout to demonstrate which image corresponds
    # to which output
    label_matlab = None
    label_python = None

    # Counters for passing and failing of the tests.  These are used to
    # calculate the pass/fail ratio of all the regression tests
    num_failed = 0
    num_passed = 0

    # Top-level container for the GUI application.  You can conceptualize this
    # as the window
    root = None

    # The current test being evaluated.  This is an integer that corresponds to
    # an index in the list test_data
    test_current = 0

    # A list of comprising of the data used to generate/display the regression
    # tests.  This variable is initialized via the init_tests() function in
    # this class
    #
    # NOTE(ALL): See init_tests() for the correct format of this variable
    test_data = None

    # ------------------------------ 
    #   PUBLIC FUNCTIONS
    # ------------------------------ 

    def init_gui(self, title = DEFAULT_TITLE):
        """
        Initializes the GUI for use

        NOTE: init_tests() must be called before init_gui()

        Args:
            title: [string] A string to display on the top of the window
        """

        # get an instance of the TK root widget (ordinary window with title bar and
        # decoration provided by the window manager)
        self.root = Tk()
        self.root.title(title)

        # uncomment these out to put in full-screen windowed mode
        """
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (width, height))
        """

        # label to display the current test we are evaluating.  We have to use
        # StringVar() and textvariable for the text to be dynamic
        self.label_test_text = StringVar()
        self.label_test_text.set(DEFAULT_TEST)
        self.label_test = Label(self.root, textvariable=self.label_test_text,
            font=DEFAULT_TEST_FONT)
        self.label_test.grid(row=0, column=0, columnspan=2)

        # Titles for the 2 columns
        self.label_python = Label(self.root, text="PYTHON", font=DEFAULT_LABEL_FONT)
        self.label_python.grid(row = 1, column = 0)

        self.label_matlab = Label(self.root, text="MATLAB", font=DEFAULT_LABEL_FONT)
        self.label_matlab.grid(row = 1, column = 1)

        # Canvases for the 2 images
        #self.img_python = PhotoImage(file="red_250x250.gif")
        self.can_python = Canvas(self.root, width=IMAGE_WIDTH,
            height=IMAGE_HEIGHT)
        #self.can_python['scrollregion'] = (0, 0, IMAGE_WIDTH, IMAGE_HEIGHT)
        #self.can_python = Canvas(self.root, width=(width/2),
        #    height=(height/2))
        #self.can_python = Canvas(self.root, width=(width/2))
        #self.can_python.create_image(0, 0, image=self.img_python)
        self.can_python.grid(row=2, column=0)

        #self.img_matlab = PhotoImage(file="blue_250x250.gif")
        self.can_matlab = Canvas(self.root, width=IMAGE_WIDTH, 
            height=IMAGE_HEIGHT)
        #self.can_matlab['scrollregion'] = (0, 0, IMAGE_WIDTH, IMAGE_HEIGHT)
        #self.can_matlab = Canvas(self.root, width=(width/2), 
        #    height=(height/2))
        #self.can_matlab = Canvas(self.root, width=(width/2))
        #self.can_matlab.create_image(0, 0, image=self.img_matlab)
        self.can_matlab.grid(row=2, column=1)

        # Buttons for pass/fail
        self.btn_pass = Button(self.root, text="PASS", command=self.test_passed,
            activebackground="green")
        self.btn_pass.grid(row=3, column=0)
        
        self.btn_fail = Button(self.root, text="FAIL", command=self.test_failed,
            activebackground="red")
        self.btn_fail.grid(row=3, column=1)

        # set the minimum size of the GUI
        self.root.minsize(width=MINIMUM_WIDTH, height=MINIMUM_HEIGHT)

        # load the first regression test.  test_current should start at index 0
        # and increment on each decision
        self.load_test(
            self.test_data[self.test_current]['title'],
            self.test_data[self.test_current]['img_matlab'],
            self.test_data[self.test_current]['img_python']
        )

        # start running the GUI
        self.root.mainloop()

    def init_tests(self, test_data):
        """
        Initialize the test data for the regression testing application.  The
        test data must be in the format specified in the argument section.

        NOTE(ALL): Images MUST be in .gif format!

        NOTE(ALL): init_tests() must be called before init_gui()

        Args:
            test_data: [list] The list of test data.  Each index of the
                       test_data must be a dictionary with the following keys:

                       'title' => The name of the test to display at the top of
                                  the GUI
                       'img_matlab' => The path to the expected matlab image
                                       output
                       'img_python' => The path to the generated image from the
                                       python code listings

        Ex:
            test_data = [
                            {
                                'title': 'listing_11_1.py', 
                                'img_matlab': 'matlab/listing_11_1.gif', 
                                'img_python': 'python/listing_11_1.gif'
                            },
                            {
                                'title': 'listing_11_2.py', 
                                'img_matlab': 'matlab/listing_11_2.gif', 
                                'img_python': 'python/listing_11_2.gif'
                            },
                            ...
                        ]
        """
        # save the test data and start at the 0th test
        self.test_data = test_data
        self.test_current = 0

    # ------------------------------ 
    #   PRIVATE FUNCTIONS
    # ------------------------------ 

    def display_stats(self):
        """
        This function is invoked once all regression tests have been completed.
        The main purpose of this function is to display the results of the
        tests, such as how many passed, how many failed, the total number of
        tests, and the pass/fail ratios.
        """
        num_tests = len(self.test_data)
        pass_ratio = (float(self.num_passed) / num_tests) * 100
        fail_ratio = (float(self.num_failed) / num_tests) * 100

        # CLI results
        print("RESULTS:")
        print("  PASSED: [" + str(self.num_passed) + "/" + str(num_tests) + "]")
        print("  FAILED: [" + str(self.num_failed) + "/" + str(num_tests) + "]")
        print("")
        print("  PASSED PERCENTAGE: [%.2f]" % pass_ratio)
        print("  FAILED PERCENTAGE: [%.2f]" % fail_ratio)

        # remove all the widgets from root
        self.btn_pass.grid_remove()
        self.btn_fail.grid_remove()

        self.can_matlab.grid_remove()
        self.can_python.grid_remove()

        self.label_matlab.grid_remove()
        self.label_python.grid_remove()

        # update the text displayed at the top of the window. I had to break
        # this into multiple lines because python is so fun.
        self.label_test_text.set("RESULTS:")

        passed_str = "PASSED: " + "[" + str(self.num_passed) + "/" + str(num_tests) + "] = "
        passed_str = passed_str + ("%.2f" % pass_ratio) + "%"

        failed_str = "FAILED: " + "[" + str(self.num_failed) + "/" + str(num_tests) + "] = "
        failed_str = failed_str + ("%.2f" % fail_ratio) + "%"

        label_passed = Label(self.root, text=passed_str, font=DEFAULT_LABEL_FONT)
        label_passed.grid(row=1, column=0)

        label_failed = Label(self.root, text=failed_str, font=DEFAULT_LABEL_FONT)
        label_failed.grid(row=2, column=0)

    def load_next_test(self):
        """
        Wrapper function for load_test to help minimize code duplication
        """
        # we're done with regression testing, show the stat screen
        if self.test_current >= len(self.test_data) - 1:
            self.display_stats()
        else:
            # load the next test
            self.test_current = self.test_current + 1
            self.load_test(
                self.test_data[self.test_current]['title'],
                self.test_data[self.test_current]['img_matlab'],
                self.test_data[self.test_current]['img_python']
            )

    def load_test(self, test_title, img_matlab, img_python):
        """
        Loads the next test for the regression tester to approve

        NOTE(ALL): Images MUST be in .gif format!

        Args:
            test_title: [string] The name of the test (for example,
                        listing_11_1.py).  This will be displayed at the top of
                        the GUI to show which test is being evaluated
            img_matlab: [string] The path to the expected matlab image output
            img_python: [string] The path to the auto-generated python image
                        output
        """
        # update the GUI widgets

        self.label_test_text.set(test_title)

        #self.img_matlab = PhotoImage(file=img_matlab)
        #self.img_python = PhotoImage(file=img_python)

        # we need to scale the images.  they are unpredictable and probably
        # really big.
        py_orig = PIL.Image.open(img_python)
        py_resize = py_orig.resize((IMAGE_WIDTH, IMAGE_HEIGHT), PIL.Image.ANTIALIAS)
        self.img_python = PIL.ImageTk.PhotoImage(py_resize)

        ml_orig = PIL.Image.open(img_matlab)
        ml_resize = ml_orig.resize((IMAGE_WIDTH, IMAGE_HEIGHT), PIL.Image.ANTIALIAS)
        self.img_matlab = PIL.ImageTk.PhotoImage(ml_resize)

        """
        ml_scale_width = float(IMAGE_WIDTH) / self.img_matlab.width()
        ml_scale_height = float(IMAGE_HEIGHT) / self.img_matlab.height()
        print("%dx%d" % (ml_scale_width, ml_scale_height))
        self.img_matlab.zoom(ml_scale_width, ml_scale_height)

        py_scale_width = float(IMAGE_WIDTH) / self.img_python.width()
        py_scale_height = float(IMAGE_HEIGHT) / self.img_python.height()
        print("%dx%d" % (py_scale_width, py_scale_height))
        self.img_python.zoom(py_scale_width, py_scale_height)
        """
        # update the UI

        self.can_matlab.create_image(0, 0, image=self.img_matlab)
        self.can_python.create_image(0, 0, image=self.img_python)

    def test_failed(self):
        """
        Invoked when the regression test failed for the image comparison
        """
        self.num_failed = self.num_failed + 1
        print("FAILED: testno: [" + str(self.test_current) + "]")
        self.load_next_test()

    def test_passed(self):
        """
        Invoked when the regression test passed for the image comparison
        """
        self.num_passed = self.num_passed + 1
        print("PASSED: testno: [" + str(self.test_current) + "]")
        self.load_next_test()

    # ------------------------------ 
    #   CONSTRUCTORS, DECONSTRUCTORS, ETC
    # ------------------------------ 

    def __init__(self):
        # call the chapter 11 regression test script to automatically generate
        # the python listing images.  We will compare these to the expected,
        # static images from the matlab listings.
        #print("LOADING...\n  Generating ch11 listings")
        #Ch11.generatePyResultImages()
        #print("DONE.")
        pass

# ------------------------------ 
#   MAIN
# ------------------------------ 

def main():

    py_dir = "Code_Listings/Ch11_PyImages/"
    ml_dir = "Code_Listings/Ch11_MatlabImages/"

    # some dummy data for the purposes of testing
    test_data = [
        {
            "title" : "listing_11_1.py",
            "img_python" : py_dir + "Listing_11_1.gif",
            "img_matlab" : ml_dir + "Figure_11_1.gif"
        },
        {
            "title" : "listing_11_2.py",
            "img_python" : py_dir + "Listing_11_2.gif",
            "img_matlab" : ml_dir + "Figure_11_2.gif"
        },
        {
            "title" : "listing_11_3.py",
            "img_python" : py_dir + "Listing_11_3.gif",
            "img_matlab" : ml_dir + "Figure_11_3.gif"
        },
        {
            "title" : "listing_11_5.py",
            "img_python" : py_dir + "Listing_11_5.gif",
            "img_matlab" : ml_dir + "Figure_11_5.gif"
        },
        {
            "title" : "listing_11_6.py",
            "img_python" : py_dir + "Listing_11_6.gif",
            "img_matlab" : ml_dir + "Figure_11_6.gif"
        },
        {
            "title" : "listing_11_8.py",
            "img_python" : py_dir + "Listing_11_8.gif",
            "img_matlab" : ml_dir + "Figure_11_8.gif"
        },
        {
            "title" : "listing_11_9.py",
            "img_python" : py_dir + "Listing_11_9.gif",
            "img_matlab" : ml_dir + "Figure_11_9.gif"
        },
        {
            "title" : "listing_11_10.py",
            "img_python" : py_dir + "Listing_11_10.gif",
            "img_matlab" : ml_dir + "Figure_11_10.gif"
        },
        {
            "title" : "listing_11_12.py",
            "img_python" : py_dir + "Listing_11_12.gif",
            "img_matlab" : ml_dir + "Figure_11_12.gif"
        },
        {
            "title" : "listing_11_13.py",
            "img_python" : py_dir + "Listing_11_13.gif",
            "img_matlab" : ml_dir + "Figure_11_13.gif"
        },
        {
            "title" : "listing_11_16.py",
            "img_python" : py_dir + "Listing_11_16.gif",
            "img_matlab" : ml_dir + "Figure_11_16.gif"
        }
    ]

    # create an instance of the regression application, load the test data, and
    # then begin running
    app = RegTestApp()
    app.init_tests(test_data)
    app.init_gui()

if __name__ == "__main__":
    main()
