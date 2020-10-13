# Author: Yanling Wang yuw17@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 1
# Breakout: 1

import time
import itertools

def get_letters_combinations(alphabet, length):
  """
  Given an alphabet such as 'abcde', and a int length n such as 2,
  returns all n letter combinations from the alphabet in alphabetical
  order, such as ['ab','ac','ad','ae','bc','bd','be','cd','ce','de']
  """
  return list(map(''.join, itertools.combinations(alphabet, length)))

def uses_all(word, letters):
  """
  Return True if every letter in letters appeared in word;
  return False otherwise.
  """
  return True

def count_words_letters(words, letters):
  """
  Return the number of words in the list that used all letters in letters.
  """
  return 0

def popular_letters(words, n):
  """
  Return the n letter combination from the alphabet such that
  all the letters in the combination appeared in the most number
  of words; if there are multiple combinations with the same
  popularity, return the combination that comes first in 
  alphabetic order.
  """
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  combinations = get_letters_combinations(alphabet, n)
  return combinations[0] 
  
def get_words(filename):
  """
  Given a filename (as a str), open the file and retrieve words from
  each line to create a list with whitespaces stripped.
  """
  ans = []
  with open(filename) as fin:
    for line in fin:
      ans.append(line.strip())
  return ans

def run():
  filename = input("Enter file name: ")
  words = get_words(filename)
  n = int(input("Enter an int: "))
  start = time.perf_counter()
  popular = popular_letters(words, n)
  end = time.perf_counter()
  print(f"{end-start} seconds to find popular {n}-letter combination:")
  print(f"Popular {n}-letter combination is: {popular}")

if __name__ == "__main__":
  run()
