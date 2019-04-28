while(True):
    s = input()
    if len(s) % 2 == 1:
        print('false')
        continue
    tag = True
    s1 = ''
    for i in range(len(s)//2):
        if not tag:
            break
        if s[i] != s[len(i)-i-1]:
            tag = False
            break
        if s[2*i] != s[2*i+1]:
            tag = False
            break
        s1 += s[2*i]
    if tag:
        print(s1)
    else:
        print('false')