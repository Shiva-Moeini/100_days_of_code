def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def devide(n1, n2):
    return n1 / n2

information = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : devide
}

def calculator():
    still_going = True
    num1 = float(input("Enter the first number:"))
    while still_going:

        for i in information:
            print(i)
        operation = input("Choose one of the operators.")
        num2 = float(input("Enter the second number:"))
        result = information[operation](n1=num1,n2=num2)
        print(result)
        choice = input(f"Type 'y' to continue with {result} or type 'n' to start a new calculation.")
        if choice == 'y':
            num1 = result
        else:
            still_going = False
            print('\n' * 30)
            calculator()

calculator()