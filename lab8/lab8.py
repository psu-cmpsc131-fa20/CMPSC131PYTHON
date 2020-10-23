# Author: Yanling Wang yuw17@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 1
# Breakout: 1

import time

def binary_search_rec(x, t, start, end):
  """
  Return the left most index of x if x is in t indexed between [start, end] inclusive
  Otherwise return -1
  You may assume that both start and end are valid index for t.
  Use Recursion, Do Not Use loops
  Your algorithm should be logarithmic to number of elements between [start, end]
  regardless of how many duplicates of x is.
  """
  return 0

def binary_search_loop(x, t, start, end):
  """
  Return the left most index of x if x is in t indexed between [start, end] inclusive
  Otherwise return -1
  You may assume that both start and end are valid index for t.
  Use loop, Do Not Use Recursion 
  Your algorithm should be logarithmic to number of elements between [start, end]
  regardless of how many duplicates of x is.
  """
  return 0

def run():
  t1 = [10, 20, 30, 30, 30, 40, 50]
  t2 = list(set(t1))
  t2.sort()
  t3 = [5, 15, 25, 35, 45, 55]
  for x in t2:
    ans = t1.index(x)
    print(f"searching for {x} in {t1} and index should be {ans}")
    ans_rec = binary_search_rec(x, t1, 0, len(t1)-1)
    ans_loop = binary_search_loop(x, t1, 0, len(t1)-1)
    print(f"rec: {ans_rec}, loop: {ans_loop}")
    assert(ans_rec == ans)
    assert(ans_loop == ans)

  for x in t3:
    ans = -1
    print(f"searching for {x} in {t1} and index should be -1")
    ans_rec = binary_search_rec(x, t1, 0, len(t1)-1)
    ans_loop = binary_search_loop(x, t1, 0, len(t1)-1)
    print(f"rec: {ans_rec}, loop: {ans_loop}")
    assert(ans_rec == ans)
    assert(ans_loop == ans)

  # Some performance checking with large lists
  t1 =[131]*1000000
  start = time.perf_counter()
  for i in range(1000):
    ans = binary_search_rec(131, t1, i, len(t1)-i)
    assert(ans == i)
  end = time.perf_counter()
  print(f"{end-start} seconds to do binary_search_rec")
  
  start = time.perf_counter()
  for i in range(1000):
    ans = binary_search_loop(131, t1, i, len(t1)-i)
    assert(ans == i)
  end = time.perf_counter()
  print(f"{end-start} seconds to do binary_search_loop")

  t1 = list(range(1000000))
  start = time.perf_counter()
  for i in range(0,1000000,1000):
    ans = binary_search_rec(i, t1, 0, len(t1)-1)
    assert(ans == i)
    ans = binary_search_rec(i, t1, i, i+999)
    assert(ans == i)
  end = time.perf_counter()
  print(f"{end-start} seconds to do binary_search_rec")

  start = time.perf_counter()
  for i in range(0,1000000,1000):
    ans = binary_search_loop(i, t1, 0, len(t1)-1)
    assert(ans == i)
    ans = binary_search_loop(i, t1, i, i+999)
    assert(ans == i)
  end = time.perf_counter()
  print(f"{end-start} seconds to do binary_search_loop")

  print("Success")
  
if __name__ == "__main__":
  run()
