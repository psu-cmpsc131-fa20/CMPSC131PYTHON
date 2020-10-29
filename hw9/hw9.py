from sys import argv
import pprint

def tile_value():
  """
  Returns a dictionary that maps lower case letter to its tile value
  """
  letters = 'abcdefghijklmnopqrstuvwxyz'
  values = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
  return dict(zip(letters, values))

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

def is_word_from_letters(word, letters):
  """
  Returns True if word is spelled by rearrange all or some of the letters
  Otherwise returns False
  Notes: this is different from uses_only function we wrote before, word
  not only can use only characters in letters, but the number of times it
  can use a letter is also limited by what is in letters. For example:
  is_word_from_letters("book", "bok") should be False because we do not have
  enough letter 'o'.
  """
  return True

def get_word_score(word, value_dict):
  """
  Given a word, and a dictionary matching each letter to an int score,
  calculates the word's score (adding up each letter's score)
  and return the score.
  """
  return 0

def get_legal_word_scores(letters, dictionary, value_dict):
  """
  Given a str of letters that we can use, and a dictionary
  that contains all legal words allowed in scrabble game,
  and a value_dict that maps each letter to a score,
  Returns a dictionary that contains all possible scores 
  earned by any legal word as the key, and for each score,
  the score/key maps to a list of words that are from the
  dictionary made from the given letters and computes to that
  score. The list should be in alphabetical order.
  """
  return {}

def run():
  # Getting list of words from the dictionary
  dictionary = get_words(argv[1])
  letters = input("Enter your letters: ")
  d = get_legal_word_scores(letters, dictionary, tile_value())
  pprint.PrettyPrinter().pprint(d)

if __name__ == "__main__":
  run()
