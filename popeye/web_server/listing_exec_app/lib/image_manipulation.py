import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

imagewritten = False

def image(pic):
    """Displays an image in a figure of fixed dimensions with axes
    
    Args:
        pic: A numpy.array. For grayscale images, the array is MxN. 
            For RGB images, the value is MxNx3. 
            For RGBA images the value is MxNx4.
    """
    plt.imshow(pic)
    plt.show()

def imread(*args, **kwargs):
    """Read an image from a file into an array.
    
    Args:
        'fname' may be a string path or a Python file-like object. 
        If using a file object, it must be opened in binary mode.
        
        If 'format' is provided, will try to read file of that type, 
        otherwise the format is deduced from the filename. If nothing can 
        be deduced, PNG is tried.
        
    Returns:
        Return value is a numpy.array. For grayscale images, the return array 
        is MxN. For RGB images, the return value is MxNx3. For RGBA images the 
        return value is MxNx4.
    """
    return mpimg.imread(*args, **kwargs)
    
def imwrite(data, fname, imformat):
    """Writes an image file
    
    Args:
        data: An MxN (luminance), MxNx3 (RGB) or MxNx4 (RGBA) array.
        fname: A string containing a path to a filename, or a Python file-like
            object. If format is None and fname is a string, the output
            format is deduced from the extension of the filename.
        imformat: One of the file extensions supported by the active backend. 
            Most backends support png, pdf, ps, eps and svg.
    """
    global imagewritten
    mpimg.imsave(fname, data, vmin=None, vmax=None, cmap=None, \
                 format=imformat, origin=None, dpi=100)
    imagewritten = True
    
def isimagewritten():
    return imagewritten
                 
def rgb2gray(pic):
    return np.dot(pic[...,:3], [0.299, 0.587, 0.114])

def imshow(*args, **kwargs):
    """Displays an image in a figure of variable dimensions without axes
    
    Args:
        pic: A numpy.array. For grayscale images, the array is MxN. 
            For RGB images, the value is MxNx3. 
            For RGBA images the value is MxNx4.
    """
    plt.axis("off")
    plt.imshow(*args, **kwargs)
    plt.show()
  
# Listing 13.04 Mirroring on a diagonal
def diagMirror(A, code):
    """ mirror this square image diagonally
        the parameter code represents the number of
        90 deg left rotations
    """
    sq = np.empty((A.shape[0], A.shape[1], A.shape[2]))
    for c in range(0,3): # tacky to do a layer at a time, but
        # tril must see a 2-D array
        layer = A[:,:,c]
        trin = np.tril(np.rot90(layer, code))
        # rotate the image back after mirroring
        sq[:,:,c] = np.rot90(trin + np.transpose(trin), 4 - code)
    return sq          

        
def shape(pic, index):
    return pic.shape[index]