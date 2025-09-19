import random
rock = ("""
   _______
---'   ____)
     (_____)
     (_____)
     (____)
---.__(___)
""")


paper = ("""
    _______
---'    ____)____
          ______)
         _______)
        _______)
---.__________)
""")


scissors = ("""
   _______
---'   ____)____
         ______)
      __________)
     (____)
---.__(___)
""")
images = [rock , paper , scissors]

choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))
if choice < 0 or choice > 2:
    print("Invalid number!")
else:
    print(f"You chose: {choice}")
    print(images[choice])

    computer_choice = random.randint(0,2)
    print(f"Computer chose: {computer_choice}")
    print(images[computer_choice])


    if choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and choice == 2:
        print("Computer wins!")
    elif choice == computer_choice:
        print("It's a draw!")
    elif computer_choice > choice:
        print("Computer wins!")
    else:
        print("You win!")






