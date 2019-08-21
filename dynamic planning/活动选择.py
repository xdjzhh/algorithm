
def activity_count(raw_list):
    if raw_list == []:
        return 0

    n = len(raw_list)

    dp = [0 for i in range(len(raw_list))]
    for i in range(n):
        dp[i] = 1
    # raw_list.append([10000,10000])

    for i in range(0,n):
        for j in range(0,i):
            if (raw_list[j][1] <= raw_list[i][0]) :
                print(i,j)
                dp[i]  = max(dp[i],dp[j] + 1)
    print(dp)
    return dp[n-1]

def active(raw_list):
    if raw_list == []:
        return 0

    n = len(raw_list)

    dp = [0 for i in range(len(raw_list))]
    for i in range(n):
        dp[i] = raw_list[i][1] -raw_list[i][0]
    # raw_list.append([10000,10000])

    for i in range(0,n):
        for j in range(0,i):
            if (raw_list[j][1] <= raw_list[i][0]) :
                print(i,j)
                dp[i]  = max(dp[i],dp[j] + raw_list[i][1] - raw_list[i][0])
    print(dp)
    return dp[n-1]


if __name__ == '__main__':
    raw_list = [[0,4],[0,2],[1,3],[2,6],[6,7],[5,8],[4,6]]
    sortedraw = sorted(raw_list,key=lambda x:x[1])
    print(sortedraw)
    print(activity_count(sortedraw))