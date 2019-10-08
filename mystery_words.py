import random

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
  
def get_difficulty(easy_words, medium_words, hard_words):
  choice = input("Welcome to Mystery Words! Please Select a Difficulty (Easy, Medium, Hard): ").lower()
  if choice == "easy":
    return easy_words
  elif choice == "medium":
    return medium_words
  elif choice == "hard":
    return hard_words
  else:
    print("Please choose a valid difficulty level...")
    get_difficulty(easy_words, medium_words, hard_words)
    

    
def game(word_pool):
  solution = random.choice(word_pool)
  print(solution)
  return

def main():
  easy, medium, hard = get_word_lists('words.txt')
  while True:
    game(get_difficulty(easy, medium, hard))
  
main()  