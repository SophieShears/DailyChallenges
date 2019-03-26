file = open("E:\Python\PDFs\dict.txt",'r+')
new_file = file.readlines()
file.seek(0)
for line in new_file:
    if "I LIEK CHOCOLATE MILK" in line:
        file.write("I quite enjoy chocolate milk" + '\n')
    else:
        file.write(line)

file.close()