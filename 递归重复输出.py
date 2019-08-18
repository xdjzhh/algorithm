

def decode(string):

    label = []
    all_string = []
    substring = []
    count = 0

    for i in string:
        if i == '|':
            count += 1

    if count == 1:
        return res(string)

    all_label = 0
    for i in string:
        if i == '[':
            if all_label == 0:
                all_string.append(i)
            all_label = 1
            label.append('[')


        if i == ']':
            label.pop(-1)
            if len(label) == 0:
                all_label = 0

        if all_label == 1:
            substring.append(i)

        if all_label == 0 :
            if substring != []:
                print('sub:{}'.format(substring))
                substring = decode(substring[1:])
                all_string.pop(-1)
                all_string += substring
                print(all_string)
                # if i == ']':
                #     all_string.append(i)
                return res(all_string)

            else:
                all_string.append(i)


def res(string):
    count = 0
    for i in string:
        if i == '|':
            count += 1
    if count == 0 :
        return ''.join(i for i in string)
    if string == []:
        return []
    real_string = ''.join(i for i in string)
    print(real_string)
    string_list = real_string.split('|')
    number = int(string_list[0])
    repeat = string_list[1]
    newstring = [repeat for i in range(number)]
    print(newstring)
    return newstring


if __name__ == '__main__':
    input = 'HG[1|[3|B[2|CA]]]F'
    print(decode(list(input)))
