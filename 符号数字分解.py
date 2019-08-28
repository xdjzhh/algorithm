import itertools


def num(n):
    count = 0
    for i in n:
        count += 1
    return count

def solution(string):
    number = []
    signal = []
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






if __name__ == '__main__':
    string = input()

    solution(string)