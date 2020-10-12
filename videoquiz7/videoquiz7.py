def get_words(filename):
  """"
  Given a filename (as a str), open the file and retrieve words from
  each line to create a list with whitespaces stripped.
  """
  ans = []
  with open(filename) as fin:
    for line in fin:
      ans.append(line.strip())
  return ans

def has_no_e(word):
  return 'e' not in word

def myfilter(t, cond):
  """
  t is a list, cond(x) is a boolean function that returns True or False
  given an element x in t.
  Return a new list that only includes element x from t such cond(x) is True. 
  """
  ans = []
  for x in t:
    if cond(x):
      ans.append(x)
  return ans

def mymap(t, f):
  """
  t is a list, f is a function that maps an element x in t to
  a different value f(x).
  Return a new list that has every element x from t mapped to f(x).
  """
  ans = []
  for x in t:
    ans.append(f(x))
  return ans

if __name__ == "__main__":
  words = get_words("words.txt")
  print(f"{len(words)} words in words.txt.")
  words1 = myfilter(words, has_no_e)
  print(f"{len(words1)} words has no 'e'.")
  print(f"{len(words1)/len(words)} of the words has no e.")
  wordlens = mymap(words, len)
  print(max(wordlens))

