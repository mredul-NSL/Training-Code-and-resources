import re
for _ in range(int(input())):
    sr = input()
    if re.search(r'^(7|8|9)[0-9]{9}$', sr):
        print("YES")
    else:
        print("NO")