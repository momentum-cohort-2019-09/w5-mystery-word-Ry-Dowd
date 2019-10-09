import random
import re

regex = re.compile('^[A-Za-z]$')
first_play = True
def get_word_lists(file):
  """ Takes a txt file as an argument, assuming that each line contains a word. Then strips those words of 
  newlines and sorts them into word pools for the different difficulties, returning a tuple that contains:
  (easy words, medium words, hard words)"""
  
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
  """Takes the word pools for their respective difficulties as arguments, and prompts the user to choose
  which difficulty they would like to play the game on. Then returns the appropriate list of words"""
  
  choice = input("Please Select a Difficulty (Easy, Medium, Hard): ").lower()
  if choice == "easy":
    return easy_words
  elif choice == "medium":
    return medium_words
  elif choice == "hard":
    return hard_words
  else:
    print("Please choose a valid difficulty level...")
    return get_difficulty(easy_words, medium_words, hard_words)
    
def prompt_play():
  """Asks the user if they would like to play. Returns 'y' or 'n' if input is valid, else prompts again."""
  response = input("Would you like to play a game?? (y/n) : ").lower()
  if response !='y' and response != 'n':
    print("I didn't understand that. Please enter (y/n)")
    return prompt_play()
  else:
    return response
    
def game(word_pool):
  solution = random.choice(word_pool)
  length = len(solution)
  print(f"Your word has {len(solution)} letters")
  guesses_left = 8
  guesses = []
  progress = "_"*len(solution)
  word_pool = word_pool
  while guesses_left > 0:
    if word_pool[0]:
      print(f"You Win!! The word was {solution}")
      return
    if len(guesses) > 0:
      print(f"Letters guessed so far: {' '.join(guesses)}")
    print(f"You've got {guesses_left} guesses remaining!")
    print(' '.join(progress))
    guess = input("Please guess a letter: ").lower()
    if regex.match(guess):
      if guess not in guesses:
        guesses.append(guess)
        guesses = sorted(guesses)
        if guess in solution:
          print('Nice Guess!')
          progress = ''.join([letter if letter in guesses else '_' for letter in solution])
        else:
          guesses_left -= 1
    else :
      print("Please enter a valid letter!")
  print(f"You Lose!! The word was: {solution}")
  

def main(words_file):
  easy, medium, hard = get_word_lists(words_file)
  print("Welcome to Mystery Words!!")
  while True:
    response = prompt_play()
    if response == 'y':
      game(get_difficulty(easy, medium, hard))
    else:
      break
  
main('words.txt') 

def split_families(letter, list, count):
  possibilities = []
  return possibilities

def examine_dictionary(letter, base_case, possibilities_list, letter_count, word_length):
  """Continues reducing down the dictionary, examining the number of possibilities based off of letter
  position. Returns a new base case if found, otherwise keeps our old base case."""
  possibilities = split_families(letter, possibilities_list, letter_count)
  for possibility in possibilities:
    if len(possibility) > len(base_case):
      base_case = possibility
  return base_case


def evil_deep_compare(letter, base_case, possibilities_dict, word_length):
  """Takes the user's guess, the list of words without that guess, and a dictionary whose keys
  correspond to lists of words with a letter count of 'key' that can possibly be bigger than
  our base case"""
  for item in possibilities_dict.items():
    base_case = examine_dictionary(letter, base_case, item[1], item[0], word_length)
  return base_case


def evil_comparison(letter, list_without_letter, list_with_letter, word_length):
  """First level deeper comparison. Takes the user's guess, the list of words that contain that guess,
  the list of words that don't contain that guess, and the length of the word to help curtail unnecessary
  processing. If a deeper comparison is needed, calls the appropriate function, otherwise returns the list
  of options that don't contain the guess."""
  
  base_case = list_without_letter
  most_options = len(base_case)
  letter_count_lists = [[]for _ in range(word_length)]
  deep_necessary = False
  for word in list_with_letter:
    for i in range(word_length):
      if word.count(letter) == i + 1:
        letter_count_lists[i].append(word)
  possibilities_dict = {}
  for count_list in letter_count_lists:
    if len(count_list) > most_options:
      deep_necessary = True
      possibilities_dict[i+1] = count_list
  if deep_necessary == True:
    return evil_deep_compare(letter, list_without_letter, possibilities_dict, word_length)
  else:
    return list_without_letter
  
  
  

def evil_filter(guess, word_pool, word_length):
  """Takes the user's guess, the existing word pool, and length of the solution.
  Compares words that contain the guess and words that don't compare the guess.
  If words without is larger, return it. Otherwise, return the result of a deeper
  comparison"""
  
  words_without_guess = []
  words_with_guess= []
  for word in word_pool:
    if guess in word:
      words_with_guess.append(word)
    else:
      words_without_guess.append(word)
  if len(words_without_guess) > len (words_with_guess):
    return words_without_guess
  else:
    return evil_comparison(guess, words_without_guess, words_with_guess, word_length)