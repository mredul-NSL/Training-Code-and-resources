testcase = int(input())

for a in range(testcase):
    s1 = int(input())
    set1 = set(map(int,input().split()))
    s2 = int(input())
    set2 = set(map(int,input().split()))
        
    flag = 0
    if set1.issubset(set2):
        print("True")
    else:
        print("False")