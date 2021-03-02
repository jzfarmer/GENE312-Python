# File name: hw2pr4.py
# Name: Jessica Farmer
# PythonBat

def front3(str):
  front = str[:3]
  return front * 3

def sum_double(a, b):
  sum = a + b
  if a == b:
    sum = 2 * sum
  return sum

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

def diff21(n):
  if n < 21: 
    return abs(n-21)
  else:
    return 2*abs(n-21)

def hello_name(name):
  return 'Hello ' + name + '!'

def near_hundred(n):
  if (abs(100-n) <=10) or (abs(200-n) <= 10):
    return True
  else:
    return False

def not_string(str):
  if str[:3] == 'not':
    return str
  else:
   return 'not ' + str

def makes10(a, b):
  if a == 10:
    return True
  elif b == 10:
    return True
  elif a + b == 10:
    return True
  else:
    return False

def string_times(str, n):
  return str * n

def monkey_trouble(a_smile, b_smile):
  return a_smile and b_smile or not a_smile and not b_smile

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

def pos_neg(a, b, negative):
  if negative:
    return(a<0 and b<0)
  else:
    return ((a<0 and b >0) or (a>0 and b<0))

def missing_char(str, n):
  return str[:n] + str[n+1:]

def front_back(str):
  if len(str) == 0 or len(str) == 1:
    return str
  return str[-1] + str[1:-1] + str[0]

def make_abba(a, b):
  return a + b + b + a

def first_two(str):
  if len(str) <= 2:
    return str
  else:
    return str[0:2]

def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  else:
    return a + b + a

def without_end(str):
  return str[1:-1]

def first_half(str):
  return str[:len(str)/2]

def left2(str):
  return str[2:] + str[:2]

def extra_end(str):
  return str[-2:] * 3

def non_start(a, b):
  return a[1:] + b[1:]

def make_out_word(out, word):
  return out[:2] + word + out[2:]

def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"

def front_times(str, n):
  if len(str) < 3:
    return str * n
  else:
    return str[:3] * n