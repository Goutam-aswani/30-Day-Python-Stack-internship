class DOBexception(Exception):
    pass


birth_year = int(input("Enter your age: "))
age = 2025 - birth_year
try:
    if age <= 21 and age > 18:
        print("Congrats, You are eligible for the exam")
    else:
        raise DOBexception
except DOBexception:
    print("you are not eligible for the exam")
