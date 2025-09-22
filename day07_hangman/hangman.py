import random
hangman_ascii_art = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
list_of_words = ["python","galaxy","umbrella","mirror","coffee","puzzle","river","castle","rocket","forest","lantern","storm","whisper","cloud","shadow"]
random_word = random.choice(list_of_words)
print(random_word)
word_length = len(random_word)
print(word_length)
placeholder = ""

for _ in range (word_length):
    placeholder += "-"
print(placeholder)
word = []
game_over = False 
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

    if "_" not in display:
        game_over = True
        print("You win!")


