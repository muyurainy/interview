def find_small(card):
    tmp_list = []
    sub_sum = 0
    for i in range(len(card)):
        if card[i] == 0 and i == 0:
            continue
        if card[i] == 0 and sub_sum<0:
            tmp_list.append(sub_sum)
            sub_sum = 0
            continue
        sub_sum += card[i]
    if sub_sum < 0:
        tmp_list.append(sub_sum)
    min_num = min(tmp_list)
    tmp_list.remove(min_num)
    return (min_num + min(tmp_list))

card = list(map(int, input().split(', ')))
min_num = min(card)
if min_num >= 0:
    card.remove(min_num)
    print (min_num + min(card))
else:
    card_tmp = [i for i in card if i < 0]
    if len(card_tmp) == 1:
        card.remove(min_num)
        print (min_num + min(card))
    else:
        for i in range(len(card)):
            if card[i] > 0:
                card[i] = 0
        print (find_small(card))
#2, -2, 7, 6, -8, -10, -5