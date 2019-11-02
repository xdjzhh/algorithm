'''
暴力算法的时间复杂度为n!,完全不应该考虑.
方法一:动态规划.

初始化一个dp[len][len]的矩阵. boolean[][] dp = new boolean[len][len];
对角线上的值设置为true,作为动态规划的初始条件
for(i = 0; i < len; i++){
    dp[i][i] = true;
    count++;
}
判断是否存在回文有两种情况；1：当两个字符s[n]和s[m]相邻时，只需要这两个字符相等即可增加count的值；2：当s[n] 和s[m不相邻时，此时只需要判断dp[n+1][m-1]和是s[n],s[m]是否相等即可得出结论
row = j;
column = i + j;
current = s.charAt(row) == s.charAt(column);//当前字符是否相等
if(current && (i == 1 || dp[row + 1][column - 1])){
    dp[row][column] = true;
    count++;
}

'''

def solution(string):
    count = 0
    dp = [[0]* len(string) for i in range(len(string))]
    for i in range(len(string)):
        dp[i][i] = 1
        count +=1

    for l in range(2,len(string)+1):
        for i in range(len(string)-l+1):
            j = i + l -1
            if (string[i] == string[j]) and ((dp[i+1][j-1]) or l == 2):
                dp[i][j] = 1
                count +=1


    return count

if __name__ == '__main__':
    string = 'aaa'
    print(solution(string))