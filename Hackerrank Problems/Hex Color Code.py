import re
for _ in range(int(input())):
    s = input()
    results = re.findall(r"(#(?:[\da-f]{3}){1,2})(?!\w)(?=.*;)", s, re.IGNORECASE)
    for result in results:
        print(result)