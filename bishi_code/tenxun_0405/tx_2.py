def solution():
    '''消除相邻不同的字符
    输入:
    4
    1100

    Notes
    -----
    直接从左到右循环去判断
    '''
    _, string = int(input()), input()
    old_length = 0
    new_str = ""
    while old_length != len(string) and len(string) >= 2:
        index = 0
        while index < len(string):
            if index == len(string) - 1:
                new_str += string[index]
                break
            if string[index] == string[index+1]:
                new_str += string[index]
                index += 1
            else:
                index += 2
        old_length = len(string)
        string = new_str
        new_str = ""
    print (len(string))

solution()