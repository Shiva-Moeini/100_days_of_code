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
num1 = float(input("Enter the first number:\n"))

for i in information:
    print(i)
operation = input("Choose one of the operators.\n")
num2 = float(input("Enter the second number:\n"))
