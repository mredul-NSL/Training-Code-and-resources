testcase = int(input())
for a in range (0,testcase):
    try:
        a,b = map(int,input().split())
        print(a//b)
    except BaseException as e:
        print("Error Code:", e)
