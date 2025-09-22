import random

hangman_ascii_art = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',  '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
========='''
]
list_of_words = ["python","galaxy","umbrella","mirror","coffee","puzzle","river","castle","rocket","forest","lantern","storm","whisper","cloud","shadow"]
random_word = random.choice(list_of_words)
print(random_word)
lives = 6
word_length = len(random_word)
print(word_length)
placeholder = ""

for _ in range (word_length):
    placeholder += "-"
print(placeholder)


game_over = False 
word = []
while not game_over:
    guess = input("Guess a letter:\n").lower()
    display = ""
    for _ in random_word:
        if _ == guess:
            display += _
            word.append(guess)
        elif _ in word:
            display += _
        else:
            display += "_"
            
        
    print(display)

    if guess not in random_word:
        lives -= 1
        if lives == 0:
            game_over == True
            print("*********You lose.*********")

    if "_" not in display:
        game_over = True
        print("*********You win!*********")

    print(hangman_ascii_art[lives])

