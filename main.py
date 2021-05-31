import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages
print(logo)
lives=6
chosen_word = random.choice(word_list)
display=list()
for char in chosen_word:
  display+="_"
  
while "_" in display:
 guess = input("Guess a letter: ").lower()
 if guess in display:
   print("You already guessed this. ")
 for position in range(len(chosen_word)):
  char=chosen_word[position]
  if char==guess:
    display[position]=char
 print(display)
 
 if guess not in chosen_word:
  lives=lives-1
  print(f"You guessed {guess}, that's not in the word so you lose a life.")
  print(stages[lives])
  if lives==0:
   print("You lose")
   print(f'The solution is {chosen_word}.')
   break #See the functionality of break
