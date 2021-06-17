def count_substring(string, sub_string):
    co = 0
    sssize = len(sub_string)
    for i in range (0, len(string) - sssize +1):
        test_str = string[i:i+sssize]
        if test_str == sub_string:
            co += 1
    return co
