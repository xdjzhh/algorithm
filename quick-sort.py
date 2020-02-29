# def quicksort(data):     #快速排序
#     print(data)
#     stone = data[0]
#     i = 1
#     j = len(data)-1
#     if len(data) > 1:     #分为len(data) >2和len(data) == 2两种情况，可合并
#         while j > i:
#             if data[j] <= stone:
#                 if data[i] > stone:
#                     data[j], data[i] = data[i], data[j]
#                 else:
#                     i += 1
#             else:
#                 j -= 1
#         if data[j] <= stone:     #当len(data) == 2时只执行此部分
#             data[0], data[j] = data[j], data[0]
#         return quicksort(data[:j]) + quicksort(data[j:])
#     else:     #回归条件，len(data) <= 1
#         return data

def quicksort(list):#降序
    key = list[0]
    i = 1
    j = len(list) - 1
    if len(list) > 1:
        while j > i:
            if list[j] >= key:
                if list[i] < key:
                    list[i],list[j] = list[j],list[i]
                else:
                    i +=1
            else:
                j -= 1
        if list[j] >=key:
            list[0],list[j] = list[j],list[0]
        return quicksort(list[:j]) + quicksort(list[j:])
    else:
        return list



if __name__ == '__main__':
    list = [6,9,3,8,7,1]
    print(quicksort(list))