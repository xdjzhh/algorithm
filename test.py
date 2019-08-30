
import sys


def solution(raw_list):
    n = len(raw_list)
    if n == 0:
        return 0
    if n == 1:
        return raw_list[0]
    minint = -sys.maxsize
    dp = [[minint]*n for i in range(n)]

    for i in range(n):
        dp[i][i] = raw_list[i]

    for l in range(1,n):
        for i in range(n-l):
            j = i + l
            dp[i][j] = max(dp[i][j-1]+raw_list[j],raw_list[j])
    return dp[0][n-1]

    pass


if __name__ == '__main__':
    raw_list = input().split(' ')
    for index in range(len(raw_list)):
        raw_list[index] = int(raw_list[index])

    print(solution(raw_list))
