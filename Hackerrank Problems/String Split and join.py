def split_and_join(line):
    # write your code here
    line = line.split()
    res = ""
    sz = len(line)
    i = 0
    for sr in line:
        res += sr
        i += 1
        if(i != sz):
            res += '-'
    return res