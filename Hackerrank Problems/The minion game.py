import sys
sys.setrecursionlimit(200000)


def minion_game(string):
    stuart = 0
    kevin = 0
    for i in range(0,len(string)):
        if string[i] == 'A' or string[i] == 'E' or string[i] == 'I' or string[i] == 'O' or string[i] == 'U':
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    if(stuart>kevin):
        res = "Stuart" + " " + str(stuart)
        print(res)
    elif(kevin == stuart):
        print("Draw")
    else:
        res = "Kevin" + " "+ str(kevin)
        print(res)