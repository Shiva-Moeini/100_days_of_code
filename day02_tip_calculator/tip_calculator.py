print("Welcome to the tip calculator!")
total = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill?"))
tip_percent = tip / 100
total_bill = total + (total * tip_percent)
bill_per_person = total_bill / number_of_people
rounded_bill_per_person = round(bill_per_person,2)
print(f"Each person should pay : {rounded_bill_per_person} $")