
def check_plus(n,signal):
    for i in range(n,len(signal)):
        if signal[i] != '+':
            return i-1
    return len(signal)-1

def check_multi(n,signal):
    for i in range(n,len(signal)):
        if signal[i] != '*':
            return i-1
    return len(signal)-1


def solution(string):
    number = []
    signal = []
    first = ['*','/']
    flag =0
    for index in range(len(string)):
        if string[index].isdigit():
            if flag == 0 :
                number.append(int(string[index]))
            else:
                number.append(-int(string[index]))
        else:
            if string[index] == '-':
                if index == 0:
                    flag = 1
                    continue
                if index >= 1:
                    if string[index-1] in ['*','/','-','+']:
                        flag = 1
                        continue
            signal.append(string[index])
    print(number)
    print(signal)

    change = []
    start = 0
    index = 0
    while index < len(signal):
        if signal[index] == '+':
            stop = check_plus(index,signal)
            if stop < len(signal)-1:
                if signal[stop+1] == '-':
                    change.append([index,stop+1])
                else:
                    change.append([index,stop])
            else:
                change.append([index, stop+1])
            index = stop+1
        if signal[index] == '*':
            stop = check_multi(index,signal)
            change.append([index,stop+1])
            pass
            index = stop + 1

        index+=1
    print( change)

    for i in change:
        sorted_number = sorted(number[i[0]:i[1]+1])
        number[i[0]:i[1]+1] = sorted_number

    print(number)







if __name__ == '__main__':
    string = input()

    solution(string)