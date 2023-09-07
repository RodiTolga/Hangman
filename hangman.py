

import random

from hangman_words import word_list
from hangman_art import logo
print(logo)
lives = 6

attempts = []
chosen_word = random.choice(word_list)                #Choosing random word from imported word_list
display=[] 
wordlength = len(chosen_word)
for _ in range(wordlength):  
  display += "_"                                      #Uses len function to count no. of letters in word and replaces it with a _
print(display)

end_of_game = False

while not end_of_game:                  

  guess = input("Guess a letter: ").lower()
  if guess in display:                                #If the letter gussed has already been guessed and was correct, then don't punish
    print(f"You've already gussed {guess}")
  for position in range(wordlength):
    letter = chosen_word[position]
    if letter == guess:                 
      display[position] = letter                      #If chosen letter is in the word, then replace the _ with the letter
  if guess not in chosen_word:
    attempts.append(guess)                            #Adds the incorrect choices to attempts array to show the user what letters have been used already
    print(attempts)
    print(f"You guessed {guess}, that's not in the word. You lose a life ")
    lives -= 1                                        #If chosen letter isnt in the word, then lose a life
    if lives == 0:
      end_of_game = True                              #After 6 incorrect choices, end_of_game changes to true and game ends
      print("You lose")
      print(f"The word was {chosen_word}")
  print(display)

  if "_" not in display:                              #When there's no more _ in the display, then end_of_game becomes True and you win. 
    end_of_game = True
    print("You win!")
  from hangman_art import stages
  print(stages[lives])                                #With every incorrect answer, another body part is added to the hangman. 