s_list = raw_input()
#print s_list
s_list = s_list.replace('{', '').replace('}', '')
word = map(int, s_list.split(', '))
d = int(raw_input())
#word = [31, 18, 19, 1, 25]
length = len(word)
word = sorted(word)
print (word)
all_num = length * (length - 1) / 2
num = 0
for i in range(length):
    j = i + 1
    while(j < length):
        if word[j] <= (word[i] +d):
            num += 1
            j +=1
        else:
            break
print '%.6f' % (1.0 * num/all_num)