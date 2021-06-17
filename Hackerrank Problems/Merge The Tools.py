def merge_the_tools(string, s):
    for i in range(0,len(string),s):
        ls = string[i:i+s]
        new_ls = ""
        for j in range(0,len(ls)):
            if ls[j] not in new_ls:
                new_ls += ls[j]
        print(new_ls)
