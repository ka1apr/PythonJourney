# Hangman Word Game

import random

stages = [
'''
 +------+
 |      |
 |      |
(")     |
/|\     |
 |      |
/ \     |
        |
        |
        |
  +-----+
  |     |
  +-----+
''',
'''
 +------+
 |      |
 |      |
(")     |
/|\     |
 |      |
/       |
        |
        |
        |
  +-----+
  |     |
  +-----+
''',
'''
 +------+
 |      |
 |      |
(")     |
/|\     |
 |      |
        |
        |
        |
        |
  +-----+
  |     |
  +-----+
''',
'''
 +------+
 |      |
 |      |
(")     |
/|      |
 |      |
        |
        |
        |
        |
  +-----+
  |     |
  +-----+
''',
'''
 +------+
 |      |
 |      |
(")     |
 |      |
 |      |
        |
        |
        |
        |
  +-----+
  |     |
  +-----+
''',
'''
 +------+
 |      |
 |      |
(")     |
        |
        |
        |
        |
        |
        |
  +-----+
  |     |
  +-----+
''',
'''
 +------+
 |      |
 |      |
        |
        |
        |
        |
        |
        |
        |
  +-----+
  |     |
  +-----+
''']

word_list = ["dwarika","ayodhya","kailash","lanka","warrior"]

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "-"
print(placeholder)

game_over = False

correct_letters = []

while not game_over:
    guess = input("Guess a letter : ").lower()
    
    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "-"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose!")

    if "-" not in display:
        game_over = True
        print("You Win!")

    print(stages[lives])















