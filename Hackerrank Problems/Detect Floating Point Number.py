import re
for _ in range(int(input())):
    res = re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())
    if res:
        print("True")
    else:
        print("False")