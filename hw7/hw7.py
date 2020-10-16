# Author: Yanling Wang yuw17@psu.edu
def num_to_digit_rec(num, base):
  """
  Return a list of digits for num with given base;
  Return an empty list [] if base < 2 or num <= 0
  """
  # Write your code here
  return []

def digit_sum(num, base):
  """
  Return the sum of all digits for a num with given base
  Your implementation should use num_to_digit_rec() function
  """
  # Write your code here
  return 0 

def digit_str(num, base):
  """
  Given a number and a base, for base between [2, 36] inclusive
  Converts the number to its string representation using digits
  0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
  to represent digits 0 to 35.
  Return the string representation of the number
  Return an empty string '' if base is not between [2, 36]
  Your implementation should use num_to_digit_rec() function
  """
  digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  # Can not find str representations for base not in [2, 36]
  if base > 36 or base < 2:
    return ""
  # Calculate and return the str representation for num for the given base
  # Write your code here
  return "" 

def uses_only(word, letters):
  """
  Return True if word only uses characters from letters;
  otherwise return False
  """
  # Write your code here
  return True

def digit_to_num(rep, base):
  """
  Return -1 if base is not between [2,36] inclusive;
  or if the string rep contains characters not a digit for the base;
  Return the number represented by the string for the given base otherwise.
  For example digit_to_num("1001", 2) is 9; digit_to_num("ABC", 16) is 2748. 
  """
  # Check if the base is valid
  if base > 36 or base < 2:
    return -1 
  digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  rep = rep.upper()
  # Check if the rep only uses proper digits
  # Write your code here
  return 0 

def run():
  num = int(input("Enter a num: "))
  base = int(input("Enter a base: "))
  print(f"Digit list is {num_to_digit_rec(num, base)}")
  print(f"Digit sum is {digit_sum(num, base)}")
  print(f"String Rep is {digit_str(num, base)}")
  rep = input(f"Enter a string rep of a num with base {base}: ")
  print(f"The number is {digit_to_num(rep, base)}")

if __name__ == "__main__":
  run()
