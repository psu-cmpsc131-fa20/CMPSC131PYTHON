import re
import time
from sys import argv

def avoids(word, letters):
  for c in letters:
    if c in word:
      return False
  return True

def get_words_from_text(filename):
  """
  Given a filename, open the file, split the file into words that contains only
  alphanumeric characters and apostrophes', treating all other characters such
  as white space, other punctuations as splitters.
  Remove all words containing digits 0-9 and remove all leading apostrophes'
  Return a list of words that contains only a-zA-Z and non-leading '.
  """
  words = []
  with open(filename) as fin:
    for line in fin:
      # Split the words in line using characters not alpha numeric or '
      line_words = re.split("[^0-9a-zA-Z']+", line)
      for word in line_words:
        # Filter out words containing digits
        if avoids(word, "0123456789"):
          # Remove the left most '
          word = word.lstrip("'")
          # Filter out empty words
          if len(word) > 0:
            words.append(word)
  return words

def load_dictionary_list(dictfilename):
  """
  Given a dictionary filename of a file that contains one word at a line,
  returns the list of words from the dictionary.
  """
  words = []
  with open(dictfilename) as dictfin:
    for line in dictfin:
      words.append(line.strip())
  return words

def get_misspelled_linear(dictionary, text):
  """
  dictionary is a list of sorted words in the dictionary; you may assume all
  words in the dictionary are lower case and only contains a-z and apostrophe'
  text is a list of words from any given text.
  Use linear search to find the list of all misspelled words in text,
  a misspelled word is a word that is in the text but not in the dicionary.
  The comparison is case insensitive. For example if cat is in the dictionary,
  then CAT, cAt, cAT, cat and etc. are all considered to be valid word.
  Return the list of misspelled word.
  Your list of misspelled word must appear in the original order as they were in
  the text list and keep original form (upper/lower case)
  if dictionary has N words and text has K words, then the running time for this
  method will be O(NK)
  """
  return [] 

def get_misspelled_binary(dictionary, text):
  """
  dictionary is a list of sorted words in the dictionary; you may assume all
  words in the dictionary are lower case and only contains a-z and apostrophe'
  text is a list of words from any given text.
  Use binary search to find the list of all misspelled words in text,
  a misspelled word is a word that is in the text but not in the dicionary.
  The comparison is case insensitive. For example if cat is in the dictionary,
  then CAT, cAt, cAT, cat and etc. are all considered to be valid word.
  Return the list of misspelled word.
  Your list of misspelled word must appear in the original order as they were in
  the text list and keep original form (upper/lower case)
  if dictionary has N words and text has K words, then the running time for this
  method will be O(K*logN)
  """
  return []

def get_misspelled_set(dictionary, text):
  """
  dictionary is a list of sorted words in the dictionary; you may assume all
  words in the dictionary are lower case and only contains a-z and apostrophe'
  text is a list of words from any given text.
  Use search in a set to find the list of all misspelled words in text,
  a misspelled word is a word that is in the text but not in the dicionary.
  The comparison is case insensitive. For example if cat is in the dictionary,
  then CAT, cAt, cAT, cat and etc. are all considered to be valid word.
  Return the list of misspelled word.
  Your list of misspelled word must appear in the original order as they were in
  the text list and keep original form (upper/lower case)
  if dictionary has N words and text has K words, then the running time for this
  method will be O(N + K), where the O(N) is the time it takes to convert a list
  of N words to a set, and O(K) is the time it takes to search for K words in
  a set.
  """
  return []

def run():
  dictname = input("Enter dictionary file name: ") 
  dictionary = load_dictionary_list(dictname)
  textname = input("Enter text file name: ")
  text = get_words_from_text(textname)
  option = int(input("Enter an option 0-2 (0:linear, 1:binary, 2:set): "))
  options = [get_misspelled_linear, get_misspelled_binary, get_misspelled_set]
  start = time.perf_counter() 
  misspelled = options[option](dictionary, text)
  end = time.perf_counter() 
  for w in misspelled:
    print(w)
  print(f"Dictionary has {len(dictionary)} words; Text has {len(text)} words.")
  print(f"Text has {len(misspelled)} misspelled words.")
  print(f"{end-start} seconds.")

if __name__ == "__main__":
  run()
