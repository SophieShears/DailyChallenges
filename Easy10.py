
def numchecker (x):
    numbers = []
    for s in x:
        if s.isdigit()== True:
            numbers.append(s)
    if len(numbers) == 10:
        print "valid"
    else:
        print "not valid"

x = raw_input("Enter your number")
numchecker(x)