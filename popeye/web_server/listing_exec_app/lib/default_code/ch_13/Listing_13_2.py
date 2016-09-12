import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

# Imports
from lib.image_manipulation import *
from lib.plot import *
from lib.librarywrappers import *
# Endports

# Listing 13.02 Replacing the gray sky
# Begin
input_path = 'input_images/'
v = imread(input_path + 'Vienna.jpg');
w = imread(input_path + 'Witney.jpg');
imshow(v)
imshow(w)

# thres = 160;
# array thres has size of image and all elements are value of threshold
thres = nparray(160);
thres = repmat(thres, v.shape[0], v.shape[1])
layer = logical_and(logical_and(greater(v[:,:,0], thres), \
            greater(v[:,:,1], thres)), greater(v[:,:,2], thres))
            # R channel > thres & G channel > thres & B channel > thres
            
# Create mask
mask = empty((size(v, 0), size(v, 1), size(v, 2)));
mask = astype(mask, bool)
# copy layer(places to mask) to each RGB channel of mask, in this case all
# channels are identical
npcopyto(mask[:,:,0],layer)
npcopyto(mask[:,:,1],layer)
npcopyto(mask[:,:,2],layer)
mask[699:size(v, 0)-1,:,:] = False;
# mask array to boolean type

# Comine image, masked part only
nv = v;
nv[mask] = w[mask];

imshow(nv);
imwrite(nv, 'newVienna.jpg', 'jpg')
# End
