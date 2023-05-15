number = input("input the number you want to approximate ")
dec_place = input('Input the number of decimal place you want to keep it to ')


# to check if the number inputted is a decimal
if '.' in number:
    value = number.split('.')
    # list 1 will be the list containing elements of decimal parts
    list1 = []
    for i in value[1]:
        list1.append(int(i))
    new_List = list1[::-1]

    while len(new_List) > int(dec_place):
        for i in new_List:
            if i >= 5:
                i = 1
                new_List[1] += i
                new_List.pop(0)
            elif i < 5:
                i = 0
                new_List.pop(i)

        last_list = []
        for i in new_List[::-1]:
            i = str(i)
            last_list.append(i)

        print(value[0] + '.' + ''.join(last_list))

else:
    print('The number you inputted is not a decimal')
