from itertools import product

def square(val):
    val = int(val)
    return val*val
    
k,m = map(int,input().split())
List = []
for i in range(0,k):
    List.append(list(map(square,input().split()[1:])))

combinations = product(*List)

mx = -10000

for i in combinations:
    res = sum(i) % m
    if(res>mx):
        mx = res
        
print(mx)