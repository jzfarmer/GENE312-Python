# hw9pr2.py
# Name: Jessica Farmer

def rot(c,n):
    """ rotates c by n characters, 'wrapping' as needed. non letters
        do not change.
        """
    if 'a' <= c <= 'z': # checks for lowercase
        if ord(c) + n <= ord('z'):
            return chr(ord(c) + n)
        else:
            return chr(ord(c)+n-26)
    elif 'A' <= c <= 'Z':
        if ord(c) + n <= ord('Z'):
            return chr(ord(c) + n)
        else:
            return chr(ord(c)+n-26)
    else:
        return c

def encipher(S,n):
    """ S is a string and n is a non negative integer between 0 
        and 25. Returns new string in which S letters have been
        rotated by n characters.
        """
    result = ''
    for c in S:
        result = result + rot(c,n)
    return result

def letScore(let):
    """ given a letter, returns a score
    """
    if let in "AEILNORSTUaeilnorstu": return 1
    elif let in 'DGdg': return 2
    elif let in 'BCMPbcmp': return 3
    elif let in 'FHVWYfhvwy': return 4
    elif let in 'Kk': return 5
    elif let in 'JXjx': return 8
    elif let in 'QZqz': return 10
    else: return 0

def sScores(s):
    LC = [ letScore(c) for c in s]
    return sum(LC)

def decipher(S):
    """ Given a string of English text already shifted by some amount
        then decipher returns the original English string to 
        the best of its ability
        """
    L = [ encipher(S, n)  for n in range(26) ]
    #print(L)
    LoL = [ [sScores(x), x] for x in L ]
    #print(LoL)
    bestpr = min(LoL)
    return bestpr

def jscore(S, T): 
    score = 0
    for c in range(len(S)):
        for i in range(len(T)):
            if S[c] == T[i]:
                score += 1
                T = T[0:i] + T[i+1:]
                break
            else:
                score = score
    return score

"""
In [65]: decipher('Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.')                           
Out[65]: [47, 'Caesar cipher? I prefer Caesar salad.']

In [66]: decipher('Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla '\ 
    ...:               'lclyfaopun dl ohcl slhyulk.')                                
Out[66]: 
[101,
 'An education is what remains after we forget everything we have learned.']

In [67]: decipher('Onyx balks')                                                      
Out[67]: [20, 'Ihsr vufem']
In [38]: jscore('diner', 'syrup')                                                    
Out[38]: 1

In [39]: jscore('geese', 'elate')                                                    
Out[39]: 2

In [40]: jscore('gattaca', 'aggtccaggcgc')                                           
Out[40]: 5

In [41]: jscore('gattaca', '')                                                       
Out[41]: 0
"""