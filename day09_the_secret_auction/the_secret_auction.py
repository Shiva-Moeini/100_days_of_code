

information = { }

def winner():
    max_number = max(information , key = information.get)
    print(f"The winner is {max_number.title()} with bid of {information[max_number]}")

still_bidding = True
while still_bidding:
    name = input("What is your name?\n").lower()
    price = int(input("What is your bid?  $"))
    information[name] = price
    print(information)
    continue_bidding = input("Are there any other bidders? Type 'Yes' or 'No'.\n").lower()
    if continue_bidding == "yes":
        print('\n'* 30)
    elif continue_bidding == "no":
        still_bidding = False
        winner()




