

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


def maxproduct2(raw_list):
    dp = [[0]*len(raw_list) for i in range(len(raw_list))]
    mindp = [[0] * len(raw_list) for i in range(len(raw_list))]
    maxresult = raw_list[0]
    for i in range(len(raw_list)):
        dp[i][i] = raw_list[i]

    for i in range(len(raw_list)):
        for j in range(i,len(raw_list)):
            dp[i][j] = max(dp[i][j-1] * raw_list[j],raw_list[j],mindp[i][j-1] * raw_list[j])
            mindp[i][j] = min(mindp[i][j-1] * raw_list[j],raw_list[j])
            maxresult = max([dp[i][j], maxresult])
    return maxresult

if __name__ == '__main__':
    raw_list = [ -2.5,4,3,0.5,8,-1]
    print(maxproduct2(raw_list))