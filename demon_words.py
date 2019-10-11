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
      word = word.strip('\n').lower()
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
  print(f"Your word has {length} letters")
  guesses_left = 15
  guesses = []
  progress = "_"*length
  word_pool = [word for word in word_pool if len(word)==length]
  while guesses_left > 0:
    if word_pool[0]==progress:
      print(f"You Win!! The word was {progress}")
      return
    if len(guesses)>0:
      print(f"Letters guessed so far: {' '.join(guesses)}")
    print(' '.join(progress))
    print(f"You've got {guesses_left} guesses left")
    # ask for guess
    guess = input("Please guess a letter: ").lower()
    if regex.match(guess):
      if guess not in guesses:
    # filter word pool
        guesses.append(guess)
        guesses = sorted(guesses)
        word_pool = evil_filter(guess, word_pool, length)
    # check guess against new word pool's first entry
        updated_progress = ''.join([letter if letter in guesses else '_' for letter in word_pool[0]])
        if updated_progress != progress:
          print("Hmmph, good guess")
          progress = updated_progress
        else:
          print("NOPE")
          guesses_left -= 1
    else:
      print("Please enter a valid letter!")
  print(f"You lose!!!!! The word was {word_pool[0]}")
  

def main(words_file):
  easy, medium, hard = get_word_lists(words_file)
  print("Welcome to Mystery Words!!")
  while True:
    response = prompt_play()
    if response == 'y':
      game(get_difficulty(easy, medium, hard))
    else:
      break
  


def one_letter_split(letter, base_case, word_list, length):
  print("Inside one letter analysis")
  print("======")
  pool = word_list
  best = base_case
  for i in range(length):
    current_check = []
    remaining_pool = []
    for word in pool:
      if word[i] == letter:
        current_check.append(word)
      else:
        remaining_pool.append(word)
    if len(current_check) > len(best):
      best = current_check
    if len(best) > len (remaining_pool):
      return best
    pool = remaining_pool

def two_letter_split(letter, base_case, word_list, length):
  print("inside two letter analysis")
  print('======')
  pool = word_list
  best = base_case
  for first in range(length-1):
    for second in range(first+1, length):
      current_check = []
      remaining_pool = []
      for word in pool:
        if word[first] != letter:
          remaining_pool.append(word)
        else:
          if word[second] == letter:
            current_check.append(word)
          else:
            remaining_pool.append(word)
      if len(current_check) > len(best):
        best = current_check
      if len(best) > len (remaining_pool):
        return best
      pool = remaining_pool
    
def three_letter_split(letter, base_case, word_list, length):
  print("inside three letter analysis")
  print('======')
  pool = word_list
  best = base_case
  if len(best)>len(word_list):
    return best
  for first in range(length-2):
    for second in range(first+1, length-1):
      for third in range(second+1, length):
        current_check = []
        remaining_pool = []
        for word in pool:
          if word[first] != letter:
            remaining_pool.append(word)
          else:
            if word[second] != letter:
              remaining_pool.append(word)
            else:
              if word[third] != letter:
                remaining_pool.append(word)
              else:
                current_check.append(word)
        if len(current_check) > len(best):
          best = current_check
        if len(best) > len (remaining_pool):
          return best
        pool = remaining_pool
        
def four_letter_split(letter, base_case, word_list, length):
  print("inside four letter analysis")
  print('======')
  pool = word_list
  best = base_case
  if len(best)>len(word_list):
    return best
  for first in range(length-3):
    for second in range(first+1, length-2):
      for third in range(second+1, length-1):
        for fourth in range(third+1, length):
          current_check = []
          remaining_pool = []
          for word in pool:
            if word[first] != letter:
              remaining_pool.append(word)
            else:
              if word[second] != letter:
                remaining_pool.append(word)
              else:
                if word[third] != letter:
                  remaining_pool.append(word)
                else:
                  if word[fourth] != letter:
                    remaining_pool.append(word)
                  else:
                    current_check.append(word)
          if len(current_check) > len(best):
            best = current_check
          if len(best) > len (remaining_pool):
            return best
          pool = remaining_pool
    

def evil_deep_compare(letter, base_case, possibilities_dict, word_length):
  """Takes the user's guess, the list of words without that guess, and a dictionary whose keys
  correspond to lists of words with a letter count of 'key' that can possibly be bigger than
  our base case"""
  # for item in possibilities_dict.items():
  #   base_case = examine_dictionary(letter, base_case, item[1], item[0], word_length)
  # return base_case
  best = one_letter_split(letter, base_case, possibilities_dict.get('1', []), word_length)
  best = two_letter_split(letter, best, possibilities_dict.get('2', []), word_length)
  best = three_letter_split(letter, best, possibilities_dict.get('3', []), word_length)
  best = four_letter_split(letter, best, possibilities_dict.get('4',[]), word_length)
  return best
  
      
  


def evil_comparison(letter, list_without_letter, list_with_letter, word_length):
  """First level deeper comparison. Takes the user's guess, the list of words that contain that guess,
  the list of words that don't contain that guess, and the length of the word to help curtail unnecessary
  processing. If a deeper comparison is needed, calls the appropriate function, otherwise returns the list
  of options that don't contain the guess."""
  
  base_case = list_without_letter
  most_options = len(base_case)
  deep_necessary = False
  possibilities_dict = {'1':[], '2':[], '3':[], '4':[]}
  for word in list_with_letter:
    for i in range(4):
      if word.count(letter) == i + 1:
        possibilities_dict[f"{i+1}"].append(word)
  for item in possibilities_dict.items():
    if len(item[1]) > most_options:
      deep_necessary = True
  if deep_necessary == True:
    return evil_deep_compare(letter, list_without_letter, possibilities_dict, word_length)
  else:
    return list_without_letter
  
  
  

def evil_filter(guess, word_pool, word_length):
  """Takes the user's guess, the existing word pool, and length of the solution.
  Compares words that contain the guess and words that don't compare the guess.
  If words without is larger, return it. Otherwise, return the result of a deeper
  comparison"""
  if len(word_pool) == 1:
    return word_pool
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
    
main('words.txt') 