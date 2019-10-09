N = int(input())
N_list = list(map(int,input().split(' ')))
insert_number = int(input())
flag = False
# for index in range(len(N_list)):
#     if N_list[index] > insert_number:
#         N_list.insert(index,insert_number)
#         flag = True
#         break
# if flag == False:
#     N_list.append(insert_number)
def rec(list1):
    mid = len(list1)//2
    if list1[mid] < insert_number:
        new_list = list1[mid+1:]
    elif list1[mid] > insert_number:
        new_list = list1[:mid]
    else:
        return N_list.index(list1[mid])
    if len(new_list) == 0:
        return N_list.index(list1[mid])

    return rec(new_list)

result = rec(N_list)
if N_list[result] >= insert_number:
    N_list.insert(result, insert_number)
else:
    N_list.insert(result+1, insert_number)
print(' '.join(str(i) for i in N_list))