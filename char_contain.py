def contain(list1,list2):
    sign = 1
    for index1 in range(len(list1)):
        for index2 in range(len(list2)):
            if list1[index1] == list2[index2]:
                sign = 1
                break
            else:
                sign = 0
        if sign == 0:
            return False
    return True

def contain2(list1,list2):
    number1 = len(list1)-1
    number2 = 0
    while number1 >=0:
        number2 = 0             #每次置0
        while number2 < len(list2):
            if list1[number1] == list2[number2]:
                print(list1[number1] ,list2[number2])
                break
            number2 +=1
        if number2 >= len(list2):
            return False
        number1 -=1
    return True

def contain3(list1,list2):
    vocal_dict = {}
    for i in list2:
        if i in vocal_dict:
            vocal_dict[i] +=1
        else:
            vocal_dict[i] = 0
    for j in list1:
        if j in vocal_dict:
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    list1 = 'asw'
    list2 = 'asdfhfjadasd'
    print(contain3(list1,list2))
