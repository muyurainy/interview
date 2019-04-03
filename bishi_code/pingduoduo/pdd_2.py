def set_min(num_list):
    for i in range(len(num_list)):
        if num_list[i] > 0:
            num_list[i] -= 1
            return i
def list_num(number):
    tmp = 0
    for i in range(len(number)):
        tmp += number[i]*int(pow(10, len(number)-i-1))
    return tmp
        
num_list = map(int, raw_input().split(' '))
a_bit = int(raw_input())
b_bit = int(raw_input())
if a_bit > b_bit:
    tmp = b_bit
    b_bit = a_bit
    a_bit = tmp
a_list = []
b_list = []
num_zero = num_list[0]
for i in range(num_list[0]):
    a_list.append(0)
num_list[0] = 0
#print (num_list, a_bit, b_bit)

for i in range(a_bit-num_zero):
    a_list.append(set_min(num_list))
    b_list.append(set_min(num_list))
for j in range(b_bit-a_bit+num_zero):
    b_list.append(set_min(num_list))
#print a_list, b_list
print list_num(a_list) * list_num(b_list)


