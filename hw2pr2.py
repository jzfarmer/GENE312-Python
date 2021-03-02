# CS5 Gold, hw2pr2
# Filename: hw2pr2.py
# Name: Jessica Farmer
# Problem description: Sleepwalking student

import random  

def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return random.choice([-1, 1])

import time

def rwpos( start, nsteps ):
    """ rwpos models a random walker that
        * starts at the int input, start
        * takes the int # of steps, nsteps

        rwpos returns the final position of the walker
    """
    time.sleep(0.1)
    print('location is', start)
    if nsteps == 0:
        return start
    else:
        newpos = start + rs()  # take one step
        return rwpos( newpos, nsteps-1 )
import time

def rwsteps( start, low, hi ):
    """ rwsteps models a random walker that
        * starts at the int input, start  
        * goes UNTIL reaching low or hi
          low will always be less than hi

        rwsteps returns the number of steps the
        walker needed to reach the lower or upper bound
    """
    print("|"+"_"*(start-low) +'❤' +"_"*(hi-start)+ "|" )    # here is the beginning of a "terminal-graphics" wandering...
    time.sleep(0.05)

    if start <= low or start >= hi:
        return 0

    else:
        newpos = start + rs()   # take one step, from start to newpos!
        return 1 + rwsteps( newpos, low, hi )

def pokemon_chase(C, PT, P):
        """
            This simulator observes two Pokemon, Charmander (C) and Pikachu (P), racing to reach 
            their Pokemon Trainer, PT, in a field. 

            C:  the location of Charmander (who wanders). Since it is a fire type Pokemon, it is 
            denoted with a 🔥 emoji.
            PT:  the location of the Pokemon Trainer (it does not move). Denoted with a 🧍 emoji.
            P:  the location of Pikachu (who wanders). Since it is an electric type Pokemon, it is 
            denoted with a ⚡ emoji. 
         
            The endpoints are always at 0 and 30. To start,  0 < sA < PT < sB < 30
   
            Good values to run:  pokemon_chase( 5, 10, 15 )  # evenly spaced
                                 pokemon_chase( 5, 20, 30 )  # uneven spacing: sB is closer...
        """ 
        print("|"+"_"*(C) +'🔥' + "_"*(PT-C)+ '🧍' + "_"*(P-PT)+ '⚡' + "_"*(30-P)+"|")
        time.sleep(0.05)

        if PT <= C or PT >= P:
            return 0

        else:
            newposC = C + rs()
            newposP = P + rs()    # take one step, from start to newpos!
            return 1 + pokemon_chase( newposC, PT, newposP)


"""Example run:
In [58]: pokemon_chase(5,10,15)                                                      
|_____🔥_____🧍_____⚡_______________|
|____🔥______🧍______⚡______________|
|___🔥_______🧍_______⚡_____________|
|__🔥________🧍______⚡______________|
|___🔥_______🧍_______⚡_____________|
|____🔥______🧍______⚡______________|
|___🔥_______🧍_______⚡_____________|
|__🔥________🧍______⚡______________|
|_🔥_________🧍_____⚡_______________|
|🔥__________🧍______⚡______________|
|_🔥_________🧍_______⚡_____________|
|__🔥________🧍______⚡______________|
|___🔥_______🧍_____⚡_______________|
|__🔥________🧍______⚡______________|
|___🔥_______🧍_______⚡_____________|
|__🔥________🧍______⚡______________|
|___🔥_______🧍_____⚡_______________|
|____🔥______🧍______⚡______________|
|_____🔥_____🧍_______⚡_____________|
|______🔥____🧍________⚡____________|
|_____🔥_____🧍_______⚡_____________|
|____🔥______🧍______⚡______________|
|___🔥_______🧍_______⚡_____________|
|____🔥______🧍________⚡____________|
|___🔥_______🧍_______⚡_____________|
|____🔥______🧍______⚡______________|
|_____🔥_____🧍_______⚡_____________|
|______🔥____🧍________⚡____________|
|_______🔥___🧍_______⚡_____________|
|______🔥____🧍________⚡____________|
|_______🔥___🧍_________⚡___________|
|________🔥__🧍__________⚡__________|
|_________🔥_🧍_________⚡___________|
|__________🔥🧍________⚡____________|
Out[58]: 33
"""

