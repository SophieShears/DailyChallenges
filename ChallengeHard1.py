import random

yourNumber = random.randint(1,101)
higherThan =1
lowerThan= 101


print("Is your number higher, lower or equal to %s?" % yourNumber)
answer = input("higher/lower/equal")


while answer != "equal":
    randNum = random.randint(higherThan, lowerThan)
    print("Is your number higher, lower or equal to %s?" % randNum)
    answer = input("higher/lower/equal")
    if answer == "lower":
        lowerThan = randNum
    elif answer == "higher":
        higherThan = randNum

