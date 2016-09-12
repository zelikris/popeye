import numpy as np
import math
import copy

def makeStruct(tup):
    ln = 0
    for ndx in np.arange(0,len(tup),2):
        it = tup[ndx+1]
        print('at ' + str(ndx+1) + ' is ' + str(it))
        itl = len(it)
        if isinstance(it, tuple) and (itl > ln):
            ln = itl
    strct = [dict() for x in range(ln)]
    for ndx in np.arange(0,len(tup),2):
        key = tup[ndx]
        value = tup[ndx+1]
        for row in np.arange(0,ln):
            dct = strct[row]
            if isinstance(value, tuple):
                dct[key] = value[row]
            else: 
                dct[key] = value  
            strct[row] = dct
    return strct  

fred = {}
fred['last'] = 'Jones'        
fred['first'] = 'Fred'        
fred['grad'] = False 
date = {}
date['day'] = 30
date['month'] = 'Feb'
date['year'] = 1984
fred['birth'] = copy.deepcopy(date) 
sally = copy.deepcopy(fred)  
sally['first'] = 'Sally'
sally['birth']['day'] = 31
print('\nFred is ' + str(fred))   
print('\nSally is ' + str(sally))   
jones = [fred, sally]  
print('\njones ' + str(jones))  
print('\njones[1] ' + str(jones[1]))  
date['year'] = 1994
triplets = makeStruct(('first', ('A','B','C'),
                      'last', 'Jones',
                      'grad', [False, True,False],
                        'birth', date))
print('\ntriplets ' + str(triplets)) 
for trip in triplets: 
    jones.append( trip ) 
print('\ncomplete jones family' + str(jones))  


