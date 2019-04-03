n = int(raw_input())
str_list = map(int, raw_input().split(' '))
str_list = sorted(str_list)
print str_list
sum_list = []
for i in xrange(n/2):
    sum_list.append(str_list[i] + str_list[n-1-i])
print max(sum_list) - min(sum_list)
