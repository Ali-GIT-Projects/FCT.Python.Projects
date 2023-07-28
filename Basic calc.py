import math

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

def get_first_number():
    return int(input("Enter the first number: "))
def get_second_number():
    return int(input("Enter the second number: "))

def print_result(result):
    print("The result is: {}.".format(result))

def main():
    first_number = get_first_number()
    second_number = get_second_number()

    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operation = int(input("Enter operation(1/2/3/4): "))

    if operation == 1:
        result = add(first_number, second_number)
    elif operation == 2:
        result = subtract(first_number, second_number)
    elif operation == 3:
        result = multiply(first_number, second_number)
    elif operation == 4:
        result = divide(first_number, second_number)
    else:
        print("Invalid operation.")
        return

    New_calculation = input("Do you want to do another calcluation (yes/no): ")
    if New_calculation == "no":
        quit()
    else:
        main()

if __name__ == "__main__":
    main()
