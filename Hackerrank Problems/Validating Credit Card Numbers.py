import re

for _ in range (int(input())):
    s = input()
    res = re.search(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s) and not re.search(r"([\d])\1\1\1", s.replace("-", ""))
    if res:
        print("Valid")
    else:
        print("Invalid")