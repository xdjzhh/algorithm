



def solution(string1,string2):
    dp = [[0]*len(string2) for i in range(len(string1))]
    for i in range(len(string1)):
        if string1[i] == string2[0]:
            dp[i][0] = 1
        else:
            dp[i][0] = 0
    for i in range(len(string2)):
        if string2[i] == string1[0]:
            dp[0][i] = 1
        else:
            dp[0][i] = 0

    max_number = 0
    for i in range(1,len(string1)):
        for j in range(1,len(string2)):
            if string1[i] == string2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0
            max_number = max(dp[i][j],max_number)
    print(max_number)

    end = []
    for i in range(len(string1)):
        for j in range(len(string2)):
            if max_number == dp[i][j]:
                end.append(i)
    # print(end)
    result = []
    for i in end:
        result.append(string1[i-max_number+1:i+1])
    result = sorted(result)
    return result



    pass

if __name__ == '__main__':
    string1,string2 = input().split(' ')
    result = solution(string1,string2)
    for i in result:
        print(i)

#1234567 12893457