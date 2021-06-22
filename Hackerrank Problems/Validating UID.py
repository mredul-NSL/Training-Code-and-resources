import re

for _ in range (int(input())):
    s = input()
    res = re.search(r'[a-zA-Z0-9]{10}',s)
    res2 = re.search(r'([A-Z].*){2}',s)
    res3 = re.search(r'([0-9].*){3}',s)
    res4 = re.search(r'.*(.).*\1', s)
    if res and res2 and res3 and not res4:
        print("Valid")
    else:
        print("Invalid")