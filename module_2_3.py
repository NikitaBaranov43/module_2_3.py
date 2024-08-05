my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, ]
c = 0
while my_list[c] >= 0:
    if c != len(my_list):
        if my_list[c] == 0:
            c = c + 1
            continue
        else:
            print(my_list[c])
            c = c + 1
            continue
    else:
        break
