def word_break(string,string_list):
    label = [0 for i in range(len(string)+1)]
    label[0] = 1
    for i in range(len(string)+1):
        j = 0
        while j < i:
            print(string[j:i])
            if string[j:i] in string_list:
                print(string[j:i])
                if label[j] == 1:
                    label[i] = 1
                    break
            j+=1

    return label
    pass


if __name__ == '__main__':
    string = 'leetcodemake'
    string_list = ['leet','code','make']
    label = word_break(string,string_list)
    print(label)