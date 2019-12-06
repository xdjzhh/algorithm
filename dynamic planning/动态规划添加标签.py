'''

logo的添加
1：直接追加1logo
2：选择之前的logo
3：复制之前的logo
4：追加复制的logo到已有logo后

求最多添加多少logo
input 操作次数

'''


def solution(number):
    dp = [0 for i in range(number+1)]
    for i in range(number+1):
        dp[i] = i

    for i in range(4,number+1):
        dp[i] = max(dp[i],dp[i-1]+dp[i-1]-dp[i-2],dp[i-3]*2)

    print(dp)

if __name__ == '__main__':
    num = int(input())
    solution(num)