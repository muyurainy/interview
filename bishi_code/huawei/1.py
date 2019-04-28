while(True):
    s = input()
    if len(s) % 2 == 1:
        print('false')
        continue
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
    if s1 != s2[::-1] :
        print('false')
        continue
    s3 = ''
    tag = True
    for i in range(len(s)//2):
        if s[2*i] != s[2*i+1]:
            print('false')
            tag = False
            break
        s3 += s[2*i]
    if tag:
        print (s3)