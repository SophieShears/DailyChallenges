def ScaleInterpreter(scale, solfege):
    #create a list of all notes for index value purposes
    chromatic = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B","C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    #create a number value for the key based on it's index position
    key = chromatic.index(scale)
    #Create a list containing the actual notes in the scale refrences by "scale" input
    exactscale = []
    exactscale.append(chromatic[key])
    exactscale.append(chromatic[key+2])
    exactscale.append(chromatic[key+4])
    exactscale.append(chromatic[key+5])
    exactscale.append(chromatic[key+7])
    exactscale.append(chromatic[key+9])
    exactscale.append(chromatic[key+11])
    #create a list to refrence solfege against
    sscale = ["Do", "Re", "Mi", "Fa", "So", "La", "Ti"]
    #the index number of the called solfege
    snum = sscale.index(solfege)
    print exactscale[snum]

#test
ScaleInterpreter("F#", "Do")