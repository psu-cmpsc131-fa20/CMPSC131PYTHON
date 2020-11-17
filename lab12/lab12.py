# Author: Yanling Wang yuw17@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 1
# Breakout: 1

from sys import argv

def run():
  """
  This program should be run with the following command line arguments:

  python3 lab12.py input.pickle output.csv
  
  input.pickle file will be a binary file that contains pickle-dump'ed 
  data of a python list of dictionaries. Each dictionary will share
  the same key and corresponds to the csv file's header row. And each
  dictionary corresponds to a row in the csv file.

  Your program shall read in the data from input.pickle file; and then
  write to the output csv file including the header row.
  """
  if len(argv) < 3:
    print(f"Usage: python3 {argv[0]} input.pickle output.csv")
    return

if __name__ == "__main__":
  run()
