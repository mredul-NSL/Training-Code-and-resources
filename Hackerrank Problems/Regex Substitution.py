import re

def change_symbol(match):
    if match.group(0) == "&&":
        return str("and")
    else:
        return str("or")

for _ in range(int(input())):
    sr = input()
    print (re.sub(r'(?<= )(&&|\|\|)(?= )', change_symbol, sr))