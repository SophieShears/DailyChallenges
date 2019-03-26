def stripDuplicates(given):
    strip = []
    dup = []
    for cnt in range(len(given)):
        if given[cnt-1] == given[cnt]:
            dup.append(given[cnt])
        else:
            strip.append(given[cnt])
    print (''.join(strip))
    print (''.join(dup))

test = "ddaaiillyypprrooggrraammeerr"
stripDuplicates(test)