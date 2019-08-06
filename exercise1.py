from collections import defaultdict,Counter
def singlechar(string):
    multilist = []
    list = []
    single = None
    for i in string:
        if i in list:
            multilist.append(i)
        else:
            list.append(i)

    for i in list:
        if i not in multilist:
            single = i
            break

    return single

def singlechar1(string):
    chardict = defaultdict(list)
    for index in range(len(string)):
        chardict[string[index]].append(index)

    for i in chardict:
        if len(chardict[i]) == 1:
            single = i
            break
    return single


if __name__ == '__main__':
     result = singlechar('asdfffsskasd')
     print(result)
     result = singlechar1('asdajfgsd')
     print(result)