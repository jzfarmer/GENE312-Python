#
# hw8pr1.py - Intro to loops!
#
# Name: Jessica Farmer
#
def fac(n):
    """Loop-based factorial function
       Argument: a nonnegative integer, n
       Return value: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1,n+1):     # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

#
# Tests for looping factorial
#
print( "fac(0)   should be   1 :",  fac(0) )   
print( "fac(5)   should be 120 :",  fac(5) ) 


def power(b,p):
    result = 1                 # starting value - like a base case
    for x in range(1,p+1):     # loop from 1 to n, inclusive
        result = result * b    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

print("power(2, 5): should be 32 ==", power(2, 5))
print("power(5, 2): should be 25 ==", power(5, 2))
print("power(42, 0): should be 1 ==", power(42, 0))
print("power(0, 42): should be 0 ==", power(0, 42))
print("power(0, 0): should be 1 ==", power(0, 0))


def summed(L):
    """Loop-based function to return a numeric list.
       ("sum" is built-in, so we're using a different name.)
       Argument: L, a list of integers.
       Result: the sum of the list L.
    """
    result = 0
    for e in L:
        result = result + e    # or result += e
    return result

# tests!
print( "summed([4, 5, 6])      should be 15 :",  summed([4, 5, 6]) )   
print( "summed(range(3, 10))   should be 42 :",  summed(range(3, 10)) ) 


def summedOdds(L):
    """Loop-based function to return a numeric list.
       ("sum" is built-in, so we're using a different name.)
       Argument: L, a list of integers.
       Result: the sum of the odds in list L.
    """
    result = 0
    for e in L:
        if e % 2 == 1:
            result = result + e
    return result  

# tests!
print( "summedOdds([4, 5, 6])      should be 5 :",  summedOdds([4, 5, 6]) )   
print( "summedOdds(range(3, 10))   should be 24 :",  summedOdds(range(3, 10)) ) 


import random

def countGuesses(hidden):
    """Uses a while loop to guess "hidden", from 0 to 99.
       Argument: hidden, a "hidden" integer from 0 to 99.
       Result: the number of guesses needed to guess hidden.
    """
    guess = random.choice(range(0, 100))     # 0 to 99, inclusive
    numguesses = 1                           # we just made one guess, above
    while guess != hidden:
        guess = random.choice(range(0, 100)) # guess again!
        numguesses += 1                      # add one to our number of guesses
    return numguesses


def unique(L):
  """Returns whether all elements in L are unique.
     Argument: L, a list of any elements.
     Return value: True, if all elements in L are unique,
                or False, if there is any repeated element
  """
  if len(L) == 0:
    return True
  elif L[0] in L[1:]:
    return False
  else:
    return unique(L[1:])  # recursion is OK in this function!



def untilARepeat(high):
    """Uses a while loop to guess "hidden", from 0 to 99.
       Argument: hidden, a "hidden" integer from 0 to 99.
       Result: the number of guesses needed to guess hidden.
    """
    L = []
    count = 0
    while unique(L):
        L += [random.choice(range(0, high))]     
        count += 1                   
    return count

"""In [65]: sum(L)/len(L)                                                               
Out[65]: 24.3696

In [66]: max(L)                                                                      
Out[66]: 84

In [67]: min(L)                                                                      
Out[67]: 2

In [68]: 42 in L                                                                     
Out[68]: True

In [69]: L.count(2)                                                                  
Out[69]: 29

In [70]: 1 in L                                                                      
Out[70]: False

In [71]: 142 in L                                                                    
Out[71]: False"""

import random

def rs():
    """ one random step """
    return random.choice( [-1, 1] )

def rwalk(radius):
    """ random walk between -radius and +radius  (starting at 0 by deafult)  """
    totalsteps = 0              # starting value of totalsteps (_not_ final value!)
    start = 0                   # start location (_not_ the total # of steps)

    while True:                 # run "forever"  (really, until a return or break)
        if start == -radius or start == radius:   
            return totalsteps   # phew!  return totalsteps  (stops the while loop)

        start = start + rs()
        totalsteps += 1         # addn totalsteps 1    (for all who miss Hmmm :-)

        #print("start:", start)  # to see what's happening / debugging

    # it can never get here!

""" How long does it take to run rwalk(5)
    10,000 times: 200 ms ± 0 ns per loop (mean ± std. dev. of 1 run, 10 loops each)
    100,000 times: 1.73 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)
    1,000,000 times: 18.5 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

    First, an LC with 10,000 random-walk trials was created (with LC = [ rwalk(5) for x in range(10000) ])
    Of those 10,000 trials, the average number of steps to reach radius 5:
    In [91]: sum(LC)/len(LC)                                                             
    Out[91]: 24.8104 

    To reach radius 6:
    In [93]: sum(LC)/len(LC)                                                             
    Out[93]: 36.1384 

    To reach radius 7:
    In [95]: sum(LC)/len(LC)                                                             
    Out[95]: 48.9528   

    To reach radius 10:
    In [97]: sum(LC)/len(LC)                                                             
    Out[97]: 99.4724

    Next level challenge! 
    From above, the pattern is on average it takes radius^2 steps to reach the radius.
    """

