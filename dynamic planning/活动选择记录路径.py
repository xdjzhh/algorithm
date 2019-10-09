from copy import *
def active(raw_list):
    if raw_list == []:
        return 0

    n = len(raw_list)

    dp = [[0,[]] for i in range(len(raw_list))]
    for i in range(n):
        dp[i][0] = raw_list[i][1] -raw_list[i][0]
        dp[i][1].append(i)
    # raw_list.append([10000,10000])

    for i in range(0,n):
        for j in range(0,i):
            if (raw_list[j][1] <= raw_list[i][0]) :
                print(i,j)
                # dp[i]  = max(dp[i],dp[j] + raw_list[i][1] - raw_list[i][0])
                if dp[i][0] < dp[j][0] + raw_list[i][1] - raw_list[i][0]:
                    dp[i][0] = dp[j][0] + raw_list[i][1] - raw_list[i][0]
                    new_dp = deepcopy(dp[j][1])
                    new_dp.append(i)
                    dp[i][1] = new_dp

    print(dp)
    '''dp[n-1]是前n-1个活动的时长的最大值（活动从0开始），所以可能出现后n-2和后n-1的时长一样长的可能性，最后需要遍历判断路径'''
    result_path = []
    for each in dp:
        if each[0] == dp[n-1][0]:
            result_path.append(each)
    return result_path


if __name__ == '__main__':
    raw_list = [[0,4],[0,2],[1,3],[2,6],[6,7],[5,8],[4,6]]
    sortedraw = sorted(raw_list,key=lambda x:x[1])
    print(sortedraw)
    print(active(sortedraw))