# CS5, Lab1 part 2
# Filename: hw1pr2.py
# Name: Jessica Farmer
# Problem description: First few functions!


def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
       Spam is great, and dbl("spam") is better!
    """
    return 2*x

def tpl(x):
    """Return value: tpl returns thrice its argument
       Argument x: a number (int or float)
    """
    return 3*x

def sq(x):
      """Return value: the square of the argument
      Argument x: a number (int or float)
      """
      return x ** 2

def interp(low, hi, fraction):
      """Return value: the floating point value that is the 
      fraction of the way between low and hi.
      Arguments: numbers (int or float)
      """
      d = hi - low
      return (d*fraction) + low
   
def checkends(s):
      """Return value: checks to see if the first and last character
         of a string are the same
         input s: a string
      """
      if s[0] == s[-1]:
         return True
      else:
         return False

def flipside(s):
      """Return value: swaps the first and second half of a string
         input s: a string
      """
      x = len(s)//2
      return s[x:] + s[:x]

def convertFromSeconds(s):
      """Return value: Converts an integer number of seconds into
         a list of days, hours, minutes, and seconds
         Input s: an int
       """
      days = s // (24*60*60)  
      s = s % (24*60*60)      
      hours = s // (60*60)
      s = s % (60*60)
      minutes = s // 60
      s = s % 60
      return [days, hours, minutes, s]