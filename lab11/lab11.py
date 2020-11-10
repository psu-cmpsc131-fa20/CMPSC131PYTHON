# Author: Yanling Wang yuw17@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 1
# Breakout: 1

from sys import argv
import csv

def run():
  """
  This program should be run with the following command line arguments:

  python3 lab11.py originalFile newFile minRating minVotes
          argv[0]  argv[1]      argv[2] argv[3]   argv[4]

  originalfilename will be a tsv (tab-separated-values) file with three
  columns

  tconst  averageRating   numVotes 

  The first column tconst will be a string unique id for a title
  The second column averageRating will be a floating point number between 0.0 ~ 10.0
  The third column numVotes will be an integer number >= 0
  Your goal is to:
  1. Read in tsv file: originalFile
  2. Filter and only keep rows whose averageRating >= minRating and whose
  numVotes >= minVotes
  3. Sort the rows by the averageRating from largest to smallest
  4. Write the filtered and sorted file as a tsv file to newFile with the same header
  """
  if len(argv) < 5:
    print(f"Usage: python3 {argv[0]} originalFile newFile minRating minVotes")
    return
  
  return

if __name__ == "__main__":
  run()
