

information = { }

def winner():
    max_number = max(information , key = information.get)
    print(f"The winner is {max_number.title()} with bid of {information[max_number]}.")

still_bidding = True

while still_bidding:

    while True:
        name = input("What is your name?\n").lower()
        if name.isalpha():
            break
        else:
            print("Name must contain only letters!")

    while True:
        try:
            price = int(input("What is your bid? $"))
            if price > 0:
                break
            else:
                print("Bid must be greater than 0.")
        except ValueError:
            print("Not a number!")

    information[name] = price
    while True:
        continue_bidding = input("Are there any other bidders? Type 'Yes' or 'No'.\n").lower()
        if continue_bidding == "yes":
            print('\n'* 30)
            break
        elif continue_bidding == "no":
            still_bidding = False
            winner()
            break
        else:
            print("Type 'yes' or 'no'!")

        




