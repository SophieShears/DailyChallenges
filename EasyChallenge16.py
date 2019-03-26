string1 = input(("Enter text: "))
string2 = input(("Enter your removal text: "))
stringA = []
stringB = []

for i in string2:
    stringB.append(i)

for i in string1:
    if i not in stringB:
        stringA.append(i)

print(''.join(stringA))