import re

s = input()

con = "qwrtypsdfghjklzxcvbnm"

results = re.findall(r'(?<=['+con+'])([aeiou]{2,})(?=['+con+'])', s, re.I)

print('\n'.join(results or ['-1']))