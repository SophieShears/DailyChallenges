shift = int(input("Shift how much?: "))
txt = input("Text you want encoded: ")
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
toprint = []
for letter in txt:
    position = letters.index(letter)
    toprint.append((letters[position+shift]))

print(''.join(toprint))
