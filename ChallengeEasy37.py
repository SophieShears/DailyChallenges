from collections import Counter
def getthatfile(file):
    file= open(r"Y:\mpirkl.BLM\PDF\BLM-Coos-MAMU-20180613-GBP-LI-2-TAC-1_1_f.txt",'r')
    count = len(open(r"Y:\mpirkl.BLM\PDF\BLM-Coos-MAMU-20180613-GBP-LI-2-TAC-1_1_f.txt",'r').readlines())
    print("Lines:",count)
    words = Counter(file.read().split())
    num=0
    for item in words.items():
        num+=1
    print ("Words:", num)

file=open(r"Y:\mpirkl.BLM\PDF\BLM-Coos-MAMU-20180613-GBP-LI-2-TAC-1_1_f.txt",'r')
getthatfile(file)
file.close()