import numpy as np
import math

def nextconn( fnd, cl ):
# find a connection name among
# those found not already connected
# usage: nm = nextconn( fnd, cl )
    for item in fnd:
        cn = item['connect'];
        for nm in cn:
            if not ison(nm, cl):
                return nm

def ison( nm, cl ):
# is this beam on the connection list,
# a list of beam names
# usage: res = ison( beam, cl )
    res = False
    for item in cl:
        if item == nm:
            res = True
            break
    return res

def beam( nm, xp, yp, conn ):
# construct a beam structure with fields:
# name - beam name
# xp, yp - coordinates of its centroid
# conn - cell array - names of adjacent beams
# useage: ans = beam( nm, xp, yp, conn )
    ans = {}
    ans['name'] = nm
    ans['pos'] = (xp, yp)
    ans['connect'] = conn
    return ans

def touches(bm, conn):
# does the beam touch this connecting point?
# usage: res = touches(beam, conn)
    res = False
    b_c = bm['connect'] 
    for item in b_c:
        if item == conn:
            res = True
            break
    return res
        
# Listing 07.03 Constructor for a CD structure
def makeCD(gn, ar, ti, yr, st, pr):
# integrate CD data into a structure
    ans = {}
    ans['genre'] = gn
    ans['artist'] = ar
    ans['title'] = ti
    ans['year'] = yr
    ans['stars'] = st
    ans['price'] = pr
    return ans

def makeStruct(tup):
    ln = 0
    for ndx in range(0,len(tup),2):
        it = tup[ndx+1]
        print('at ' + str(ndx+1) + ' is ' + str(it))
        itl = len(it)
        if isinstance(it, tuple) and (itl > ln):
            ln = itl
    strct = [dict() for x in range(ln)]
    for ndx in np.arange(0,len(tup),2):
        key = tup[ndx]
        value = tup[ndx+1]
        for row in range(0,ln):
            dct = strct[row]
            if isinstance(value, tuple):
                dct[key] = value[row]
            else: 
                dct[key] = value  
            strct[row] = dct
    return strct  
        
        
# Listing 07.02 Tuple processing example
def totalNums(it):
## count the numbers in a tuple
    n = 0;
    print('in totalNums type of ' + str(it) + ' is ' + str(type(it)))
    if isinstance(it, bool):  # trap bool - it registers as an int!
        pass
    elif isinstance(it, (float, int, np.int32)):
        n = n + 1
    elif isinstance(it, (list, np.ndarray, tuple)):
        for dat in it:
            n = n + totalNums(dat)
    return n
    
def Listing_02():
# Listing 07.0 tuples
    tup =  'abc', False, 42, [1, 2, 3], 'defg', math.pi, np.arange(1,4)
    print('tup = ' + str(tup))
    for it in tup:
        print('type of ' + str(it) + ' is ' + str(type(it)))
    n = totalNums(tup)
    print('There are %d numbers in %s' % (n, str(tup)))
    
def Listing_04():
# Listing 07.04 Building a structure array using struct(...)
    pass
    genres = ('Blues', 'Classical', 'Country' )
    artists = ('Clapton, Eric', 'Bocelli, Andrea', 'Twain, Shania' )
    years = ( 2004, 2008, 2010 )
    stars = ( 2, 4.6, 3.9 )
    prices = ( 18.95, 14.89, 13.49 )
    cds = makeStruct( ('genre', genres, 
                  'artist', artists, 
                  'year', years, 
                  'stars', stars, 
                  'price',  prices))
    print('cds  = ' + str(cds))

def Listing_05():
# Listing 07.05 Building a structure array using a custom constructor
# extracts from http://www.cduniverse.com/ 12/30/04
    cds = []
    cds.append(makeCD('Blues', 'Clapton, Eric',
    'Sessions For Robert J', 2004, 2, 18.95 ))
    cds.append(makeCD('Classical', 
    'Bocelli, Andrea', 'Andrea', 2004, 4.6, 14.89 ))
    cds.append(makeCD( 'Country', 'Twain, Shania',
    'Greatest Hits', 2004, 3.9, 13.49 ))
    cds.append(makeCD( 'Latin', 'Trevi, Gloria',
    'Como Nace El Universo', 2004, 5, 12.15 ))
    cds.append(makeCD( 'Rock/Pop', 'Ludacris', 
    'The Red Light District', 2004, 4, 13.49 ))
    cds.append(makeCD( 'R & B', '2Pac', 
    'Loyal To The Game', 2004, 3.9, 13.49 ))
    cds.append(makeCD( 'Rap', 'Eminem', 
    'Encore', 2004, 3.5, 15.75 ))
    cds.append(makeCD( 'Heavy Metal', 'Rammstein', 
    'Reise, Reise', 2004, 4.2, 12.65 ))
    print('cds  = ' + str(cds))
    
def Listing_06():
# Listing 07.06 Connectivity of a structure
    data = []
    data.append(beam('A-1', 0.866, 0.5, 
               ('A','A-2','A-3','D-1') ))
    data.append(beam('A-2', 0, 1, 
               ('A','A-3','B-1','B-2') ))
    data.append(beam('A-3', 0.866, 1.5, 
               ('A-1','A-2','B-1','D-1') ))
    data.append(beam('B-1', 0.866, 2.5, 
               ('A-2','A-3','B-2','B-3','D-1','D-2') ))
    data.append(beam('B-2', 0, 3, 
               ('A-2','A-3','B-1','B-3','C-1','C-2') ))
    data.append(beam('B-3', 0.866, 3.5, 
               ('B-1','B-2','C-1','C-2','D-1','D-2') ))
    data.append(beam('C-1', 0.866, 4.5, 
               ('B-2','B-3','C-2','C-3','D-2') ))
    data.append(beam('C-2', 0, 5, 
               ('B-2','B-3','C-1','C-3','C') ))
    data.append(beam('C-3', 0.866, 5.5, 
               ('C-1','C-2','D-2','C') ))
    data.append(beam('D-1', 1.732, 2, 
               ('A-1','A-3','B-1','B-3','D-2') ))
    data.append(beam('D-2', 1.732, 4, 
               ('B-1','B-3','C-1','C-3','D-1') ))
    conn = 'A';
    clist = list()
    clist.append(conn)
    while True:
        found = list()
        # find all the beams connected to conn
        for bm in data:
            if touches(bm, conn):
                found.append(bm)
        # eliminate those already connected
        for jn in range((len(found)-1),-1,-1):
            if ison(found[jn]['name'], clist):
                del found[jn]
            else:
                clist.append(found[jn]['name'])
        if len(found) > 0:
            conn = nextconn( found, clist )
            clist.append(conn)
        else:
            break
    print('the order of assembly is:' + str(clist))

#print("\nREMOVE Listing_01\n")
#print("\nListing_02\n")
#A = Listing_02()
#print("\nListing_04\n")
#A = Listing_04()
#print("\nListing_05\n")
#A = Listing_05()
print("\nListing_06\n")
A = Listing_06()
