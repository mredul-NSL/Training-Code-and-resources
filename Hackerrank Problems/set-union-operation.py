s1 = int(input())
set1 = set(map(int,input().split()))
s2 = int(input())
set2 = set(map(int,input().split()))
print(len(set1.union(set2)))