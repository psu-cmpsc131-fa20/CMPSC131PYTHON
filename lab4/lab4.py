# Author: Yanling Wang yuw17@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 1
# Breakout: 12

def num_of_divisors(n):
  """
  given a positive int n, return number of divisors for n between 1-n inclusive
  You must use a while cond: style loop for this function.
  """

  return 0

def sum_n(n):
  """
  given a non-negative int n, return the sum 0+1+2+...+n
  You must use a while cond: style loop for this function.
  """
  return 0

def print_n(s, n):
  """
  given a string s and a non-negative int n, print s n times
  you must use for ... in range(...): style loop for this function
  """
  return

def run():
  num = int(input("Enter an int: "))
  print(f"sum is {sum_n(num)}.")
  line = input("Enter a string: ")
  print_n(line, num)
  print(f"{num} has {num_of_divisors(num)} divisors.")

if __name__ == "__main__":
  run()
