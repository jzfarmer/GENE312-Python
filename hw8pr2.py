# hw8pr2.py
# Name: Jessica Farmer
# Python bat loop practice


def double_char(str):
  result = ''
  for c in str:
    result += c*2
  return result


def count_code(str):
  count_code = 0
  for i in range(0, len(str)-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      count_code += 1
  return count_code

def count_hi(str):
  count_hi = 0
  for i in range(len(str)-1):
    if str[i:i+2] == 'hi':
      count_hi += 1
  return count_hi

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))

def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(len(str)-2):
    if str[i:i+3] == 'cat':
      cat += 1
    if str[i:i+3] == 'dog':
      dog += 1
  return cat == dog

def xyz_there(str):
  for i in range(len(str)):
    if str[i] != '.' and str[i+1:i+4] == 'xyz':
      return True
  if str[0:3] == 'xyz':
    return True
  return False

def count_evens(nums):
  count = 0
  for c in nums:
    if c % 2 == 0:
      count += 1
  return count

def sum13(nums):
  if len(nums) == 0:
    return 0
  for i in range(0, len(nums)):
    if nums[i] == 13:
      nums[i] = 0
      if i+1 < len(nums): 
        nums[i+1] = 0
  return sum(nums)

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  sum = 0
  for c in nums:
    sum += c
  return (sum - min(nums) - max(nums)) / (len(nums)-2) 

def has22(nums):
  for i in range(0, len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True    
  return False

def string_bits(str):
  result = ''
  for n in range(0, len(str)):
    if n%2 == 0:
      result += str[n]
  return result
