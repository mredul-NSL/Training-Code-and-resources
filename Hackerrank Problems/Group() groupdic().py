import re

sr = input()

results = re.search(r'([a-zA-Z0-9])\1+',sr)
if results:
    print(results.group(1))
else:
    print('-1')