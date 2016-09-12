import numpy as np
import copy

# Listing 09_01 simple fact
def simple_fact(N):
    if N == 0:
        result = 1
    else:
        result = N * simple_fact(N-1)
    return result
    
# Listing 09_03 fact with wrapper
def fact(N):
    if (N < 0) or (N%1 > 0):
        raise RuntimeError('Bad input number: ' + str(N))
    return r_fact(N)
    
def r_fact(N):
    if N == 0:
        result = 1
    else:
        result = N * r_fact(N-1)
    return result

# Listing 09.05 The Fibonacci function
def fib(N):
# recursive computation the Nth Fibonacci number
    if N == 1 or N == 2:
        result = 1
    else:
        result = fib(N-1) + fib(N-2)
    return result

def f(x):
    return ((((((0.0333*x - 0.3)*x) - 1.3333)*x + 16)*x + 0)*x - 187.2)*x + 172.9
    
def Listing_04():
# Testing fact and fib
    print('test factorial')
    print('simple 5! = ' + str(simple_fact(5))) 
# fact protected by a wrapper
    print('5! = ' + str(fact(5)))  
    try:
        it = fact(-5)
        print("shouldn't print" + str(it))  
    except:
        print('negative input error')
    try:
        it = fact(5.1)
        print("shouldn't print" + str(it))  
    except:
        print('fractional input error')
    print('test fibonacci', flush = True)
    print('5th fibonacci num is ' + str(fib(5)), flush = True) 
    for N in range(25,36):
        print(str(N) + 'th fibonacci num is ' + str(fib(N)), flush = True)  
             
def Listing_06():
# Listing 09.06 testing find zeros
    px = np.linspace(-6.3, 8.4, 19)
    vf = np.vectorize(f)  
    py = vf(px) 
    left = py[np.arange(0,len(px)-1)]
    right = py[np.arange(1,len(px))]
    zeros = (left * right) <= 0
    print('zeros occur just after' + str(px[zeros]))
    root = findZero([px(zeros(3)) px(zeros(3)+1)])
    
#print("\nListing_04\n")
#A = Listing_04();
print("\nListing_06\n")
A = Listing_06();
