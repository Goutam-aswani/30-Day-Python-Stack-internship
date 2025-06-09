def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    if b == 0:
        print("Cannot divide by zero")
    else:
        return a / b


if __name__ == "__main__":
    input1 = int(input("Enter first number: "))
    input2 = int(input("Enter second number: "))
    operation = input("Choose operation(add:1,subtract:2,multiply:3,divide:4): ")

    if operation == "1":
        print(f"The result is: {add(input1, input2)}")
    elif operation == "2":
        print(f"The result is: {subtract(input1, input2)}")
    elif operation == "3":
        print(f"The result is: {multiply(input1, input2)}")
    elif operation == "4":
        result = divide(input1, input2)
        if result is not None:
            print(f"The result is: {result}")
    else:
        print("Invalid operation selected")
