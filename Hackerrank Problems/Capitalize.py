def solve(s):
    for a in s[:].split():
        s = s.replace(a, a.capitalize())
    print(s)
    return s   