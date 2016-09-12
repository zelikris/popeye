import numpy as np
import math

def toString(a):
    return "".join([chr(item) for item in a])

def decrypt(itxt):
    global loch, hich, ch_range
    rn = np.random.randint(ch_range, size = len(itxt))
    change = np.logical_and((itxt>=loch), (itxt<=hich))
    idec = itxt[:];
    idec[change] = idec[change] - rn[change] + ch_range;
    idec[idec > hich] = idec[idec > hich] - ch_range;
    return toString(idec)
    
    
def Listing_01():
# Listing 06.01 Encryption exercise
    global loch, hich, ch_range
    txt = '''For example, consider the following:
    import numpy as np
    import math
    A = np.array([4.7, 1321454.47, 4.8]);
    index = 0;
    v = 'values';
    print('%8s of A(%d) are \t%8.3f' % (v, index, A[index]) 
    The first conversion, %8s', took the value
     of the first parameter, v, allowed 8 spaces. '''
    print('\noriginal text:\n' + txt)
#    % % encryption section
    np.random.seed(123456)
    loch = 33;
    hich = 126;
    ch_range = hich+1-loch;
#    rn = floor( ch_range * rand(1, length(txt) ) );
    itxt = np.fromstring(txt,dtype=np.uint8)
    rn = np.random.randint(ch_range, size = len(txt))
    change = np.logical_and((itxt>=loch), (itxt<=hich))
    ienc = itxt;
    ienc[change] = ienc[change] + rn[change];
    ienc[ienc > hich] = ienc[ienc > hich] - ch_range;
    enc = toString(ienc)
    print('\nencrypted text:\n' + enc)
#    % % good decryption
    np.random.seed(123456)
    dec = decrypt(ienc)
    print('\ngood decrypt:\n' + dec);
#    % % bad seed
    np.random.seed(123457)
    dec = decrypt(ienc)
    print('\nbad seed decrypt:\n' + dec);
    
    
print("\nListing_01\n")
A = Listing_01();
