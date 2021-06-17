if __name__ == '__main__':
    s = input()
    flag = 0
    for a in s:
        if a.isalnum():
            print("True")
            flag = 1
            break
    if(flag == 0):
        print("False")
    flag = 0
    for a in s:
        if a.isalpha():
            print("True")
            flag = 1
            break
    if(flag == 0):
        print("False")
    flag = 0
    for a in s:
        if a.isdigit():
            print("True")
            flag = 1
            break
    if(flag == 0):
        print("False")
    flag = 0
    for a in s:
        if a.islower():
            print("True")
            flag = 1
            break
    if(flag == 0):
        print("False")
    flag = 0
    for a in s:
        if a.isupper():
            print("True")
            flag = 1
            break
    if(flag == 0):
        print("False")