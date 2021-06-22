import re
sr = input()
raw = input()
raw_pattern = re.compile(raw)
results = raw_pattern.search(sr)
if not results: 
    print ("(-1, -1)")
while results:
    print ("({0}, {1})".format(results.start(), results.end() - 1))
    results = raw_pattern.search(sr,results.start() + 1)
