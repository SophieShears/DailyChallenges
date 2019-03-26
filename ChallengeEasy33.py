from random import *
rnd = {0:"12*12", 1:"2*5", 2:"5*5", 3:"Species? Canis:"}
correct = {0:"144", 1:"10", 2:"25", 3:"lupis"}

num = randint(0,3)
ans = input((rnd[num]))
while ans != "exit":
    if ans == correct[num]:
        num = randint(0,3)
        ans = input((rnd[num]))
    else:
        print(correct[num])
        num = randint(0,3)
        ans = input((rnd[num]))