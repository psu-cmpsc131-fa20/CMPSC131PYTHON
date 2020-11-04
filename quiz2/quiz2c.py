# Author: Yanling Wang yuw17@psu.edu
# GitHub UserID: yanlingpsu

# The only requirement for this file is that:
# Your code must print out the 2 answers to the quiz question 
# in two separate lines when run directly without any user input
# $python3 quiz2c.py words.txt
# answer1
# answer2

from sys import argv

def get_words(filename):
  """
  Given a dictionary filename of a file that contains one word at a line,
  returns the list of words from the dictionary.
  """
  words = []
  with open(filename) as fin:
    for line in fin:
      words.append(line.strip())
  return words

def get_word_score(word, value_dict):
  """
  Given a word, and a dictionary matching each letter to an int score,
  calculates the word's score (adding up each letter's score)
  and return the score.
  """
  return 0 

def get_answer(words, value_dict):
  return 


if __name__ == "__main__":
  # Getting list of words from the dictionary
  words = get_words(argv[1])
