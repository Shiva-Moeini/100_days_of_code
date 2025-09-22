import random
list_of_words = ["python","galaxy","umbrella","mirror","coffee","puzzle","river","castle","rocket","forest","lantern","storm","whisper","cloud","shadow"]
random_word = random.choice(list_of_words)
print(random_word)
word_length = len(random_word)
print(word_length)
placeholder = ""
display = ""
for _ in random_word:
    placeholder += "-"
print(placeholder)

 
guess = input("Guess a letter:\n").lower()



