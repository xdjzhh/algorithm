def change(number_list):
    i = 0
    j = len(number_list)-1

    while j > i:
        if (number_list[i]%2 != 0)& (number_list[j]%2 == 0):
            number_list[i],number_list[j] = number_list[j],number_list[i]
            i+=1
            j-=1
        elif (number_list[i]%2 != 0)& (number_list[j]%2 != 0):
            j-=1
        elif (number_list[i]%2 == 0)& (number_list[j]%2 == 0):
            i+=1
        else:
            i+=1
            j-=1
        print(i,j)
    return number_list

raw_string = input().split(' ')
for i in range(len(raw_string)):
    raw_string[i] = int(raw_string[i])
print(change(raw_string))