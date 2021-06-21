from itertools import permutations

sr, size = input().split(" ")
size = int(size)
permutations = list(permutations(sr, size))
permutations.sort()

for i in permutations:
    print("".join(i))