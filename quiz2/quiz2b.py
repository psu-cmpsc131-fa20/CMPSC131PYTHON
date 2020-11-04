# Author: Yanling Wang yuw17@psu.edu
# GitHub UserID: yanlingpsu

def fun_b(t, d):
  return 0 

def run():
  d = {"banana": 1.0, "orange":2.0, "toilet paper":3.0, "chips":4.0, "steak":10.0}

  t = [("banana", 2), ("steak", 1), ("toilet paper", 3), ("orange", 2.5), ("banana", 3)]

  print(f"{fun_b(t,d)}")

if __name__ == "__main__":
  run()
