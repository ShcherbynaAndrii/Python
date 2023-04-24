print()

import random

word_list = ["ardvark", "bavabon", "camel"]

chosen_word = random.choice(word_list).lower()
print (chosen_word)
display = []
for letter in range(len(chosen_word)):
  display += "_"

guess = input("Guess a letter: ").lower()

for position in range(len(chosen_word)):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter

print (display)