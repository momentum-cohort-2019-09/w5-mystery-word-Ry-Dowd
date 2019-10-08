
def get_word_lists(file):
  easy_words = []
  medium_words = []
  hard_words = []
  with open(file) as words:
    for word in words.readlines():
      word = word.strip('\n')
      if 4 <= len(word) <= 6:
        easy_words.append(word)
      if 6 <= len(word) <= 8:
        medium_words.append(word)
      if 8 <= len(word):
        hard_words.append(word)
  return(easy_words, medium_words, hard_words)
    
def main():
  easy_words, medium_words, hard_words = get_word_lists('words.txt')
  input