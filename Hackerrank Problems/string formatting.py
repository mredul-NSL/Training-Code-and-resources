def print_formatted(number):
    width = len(str(bin(number)).replace('0b',''))
    for i in range(1, number+1):
        b = bin(int(i)).replace('0b','').rjust(width, ' ')
        o = oct(int(i)).replace('0o','').rjust(width, ' ')
        h = hex(int(i)).replace('0x','').upper().rjust(width, ' ')
        dec = str(i).rjust(width, ' ')
        print(dec, o, h,b)