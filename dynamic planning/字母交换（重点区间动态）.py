
'''
字符串S由小写字母构成，长度为n。定义一种操作，每次都可以挑选字符串中任意的两个相邻字母进行交换。询问在至多交换m次之后，字符串中最多有多少个连续的位置上的字母相同？
input ：abcbaa 2
output ：2

这题算是这场笔试最难的题了，区间动态规划，这也只有一线互联网公司会考，如果是不那么大的厂，顶多考一个背包问题。

要求移动后形成的最长连续子串，这个最长连续子串可能全是a或b……c。因此，这里需要枚举移动后形成的最长连续子串里面所包含的字母；

确定了里面包含的字母，就可以专注于这个字母了，也就是说其余的字母都是没有用的，把它们从序列中挖掉；然后就值剩下目标字母了，目标字母离散地分布在序列中，

因此，再离散化一下，搞完之后会生成一个行的序列，之后的动态规划就在新的序列上进行。

123456
abcbaa

tag= 'a'  :156
           aaa
tag= 'b'  :24
           bb
tag= 'c'  :3
           c


现在新的序列pos看起来是合在了一起，形成了最长连续子序列，但是，形成这些连续序列所需要的操作次数是多少呢？如果操作次数大于m，那么该序列就是不满足要求的；

因此，这里面就可以得出区间动态规划了，先从小到大枚举段长，依次求得该段长的所有子序列的操作次数，并判断是否小于等于m，如果满足要求，就更新答案。

从小到大枚举段长是为了利用子问题的结果；dp[i][j]表示把pos[i]和pos[j]之间的目标字母移动到一起，形成j - i + 1长度的连续子序列所需要的操作次数；

状态转移方程：dp[i][i + len - 1] = dp[i + 1][i + len - 2] + pos[i + len - 1] - pos[i] - len + 1;，依据是|x−a|+|x−b||x−a|+|x−b|在什么时候

取得最小值。用最小的移动次数把两个目标字母移动到一起的方法就是把两个目标字母都往中间靠，状态转移方程就是根据这个来的，先把pos[i + 1] ~ pos[i + len - 2]

之间的目标字母移动到一起，这个移动次数就是dp[i + 1][i + len - 2]，然后把两个端点pos[i]和pos[i + len -1]处的目标字母往中间靠，所需要的移动次数是

pos[i + len - 1] - pos[i] - len + 1。


'''

def solution(string,m):
    c = 'a'
    result =1
    while c <= 'z':
        position = []
        for index in range(len(string)):
            if c == string[index]:
                position.append(index)
            # print(position)

        if len(position) < 2:
            c = ord(c) + 1
            c = chr(c)
            continue
        print(position)
        ret = 1

        dp = [[0]*len(position) for i in range(len(position))]
        print(position,dp)
        for length in range(2,len(position)+1):
            for i in range(len(position)-length+1 ):
                j = i + length -1
                dp[i][j] = dp[i + 1][j-1] + position[i + length - 1] - position[i] - length + 1
                if dp[i][j] <= m:
                    ret = length
        result = max(ret,result)

        c = ord(c) +1
        c = chr(c)
        print(c)

    return result

    pass


if __name__ == '__main__':
    string,m = input().split(' ')
    m = int(m)
    print(solution(string,m))