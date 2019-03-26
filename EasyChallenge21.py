def compare(list1,list2):
    for i in list2:
        if i not in list1:
            list1.append(i)
    print(list1)

list1 = [42, "X", "Hey"]
list2 = [55, "lol", "X"]
compare(list1,list2)