T = 3
game = [1,2,3]
for i in range(0,T):
    item = game[i]
    count = 0 
    while item != 1:
        if item % 2 == 0:
            item = int(item/2)
        else:
            item = 3*item +1
        count += 1
    print (count)

