

def maxproduct(raw_list):
    maxend = raw_list[0]
    minend = raw_list[0]
    maxresult = raw_list[0]

    i = 1
    while i < len(raw_list):
        maxend = maxend * raw_list[i]
        minend = minend * raw_list[i]
        maxend = max([max([maxend,minend]),raw_list[i]])
        minend = min([min([maxend,minend]),raw_list[i]])
        maxresult = max([maxend,maxresult])
        i += 1
    return maxresult


if __name__ == '__main__':
    raw_list = [ -2.5,4,0,3,0.5,8,-1]
    print(maxproduct(raw_list))