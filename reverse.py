#回文


def reverse_string(string):
    index_list = []
    max_len = 0
    for i in range(len(string)):
        j = 0
        while (i - j >= 0) & (i+j <len(string)):
            if string[i-j] != string[i+j]:
                break
            else:
                j +=1
        length = 2 * (j-1) +1
        if max_len < length:
            max_len = length
            index_list.append(i)


    for i in range(len(string)):
        j = 0
        while (i - j >= 0) & (i+j+1 <len(string)):

            if string[i-j] == string[i+j+1]:
                j +=1
            else:
                break

        length = 2 * j
        if max_len <length:
            max_len = length
            index_list.append(i)
    return max_len,index_list


def reverse_string_2(string):
    string_list = ['$','#']
    for i in string:
        string_list.append(i)
        string_list.append('#')
    # print(string_list)
    p = [0 for i in range(len(string_list))]
    # print(p)
    mx = 0
    id = 0
    index = 1 ###因为必须用$来限定0和2不等  不然会检索-1
    while index < len(string_list):
        if mx > index:
            p[index] = min(p[2*id - index],mx - index)
        else:
            p[index] = 1
        # print('string_index:{}'.format(string_list[index]))
        while ((index + p[index]) < len(string_list)-1) and (string_list[index + p[index]] == string_list[index - p[index]]):
            # print(string_list[index + p[index]])
            # print(string_list[index - p[index]])
            p[index] +=1
        if index + p[index] > mx:
            mx = index + p[index]
            id = index
        index += 1
    return p



if __name__ == '__main__':
    string = 'asddsaaaaaaaaaaaq'
    string1 = 'asdsaaaaaaaaaaaaq'
    string2 = 'google'
    max_len, index_list =(reverse_string(string2))
    print('max_len lenght of reverse string:' + str(max_len))
    print('the index of mid term:' + str(index_list[-1]))
    p = reverse_string_2(string2)
    print(p)
    print(max(p)-1)