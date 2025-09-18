small_pizza = 15
medium_pizza = 20
large_pizza = 25
bill = 0

print("Welcome to Python Pizza Deliveries!")
size = input ("What size pizza would you like to order? S, M, or L?")
pepperoni = input ("Would you like pepperoni on your pizza? Y or N?")
cheese = input ("Would you like extra cheese on your pizza? Y or N?")

# Calculating the price of pizza
if size == "S":
    bill += small_pizza
elif size == "M":
    bill += medium_pizza
elif size == "L":
    bill +=large_pizza
else:
    print("You typed the wrong inputs.")


# Calculating the price of pizza with pepperoni
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else :
        bill += 3

# Calculating the price of pizza with extra cheese
if cheese == "Y":
    bill += 1

print (bill)


