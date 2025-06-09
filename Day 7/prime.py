

def is__prime(a):
    if a <= 1:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    m = int(a**0.5)+1
    for i in range(3, m, 2):
        if a % i == 0:
            return False
    return True


if __name__ == "__main__":
    input1 = int(input("enter a number: "))
    if is__prime(input1):
        print(f"{input1} is a prime number")
    elif not is__prime(input1):
        print(f"{input1} is not a prime number")
