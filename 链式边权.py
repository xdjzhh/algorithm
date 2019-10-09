'''

n个点连成一条链，从左往右依次从1到n编号。相邻点之间有边相连，一共有n-1条边。所有的边从1到n-1编号，第i条边连接了点i和i+1。

第i个点有点权ai，定义第i条边的权重为wi：有多少点对x，y满足在第i条边的左侧（x≤i），y在第i条边的右侧（y>i），且x和y的点权不同。

给出每个点的点权，请求出所有边的边权。

例子：
4
1 2 1 1
 输出 1 2 1

解释：
    (r_count - rw[a[i]]) - (l_count - lw[a[i]]) 以上述为例是指 边位1时，有1，2对 边为2时 点2左移计算2在左和在右的对数的差值
'''

import collections

n = eval(input())
a = list(map(int, input().split()))

lw = collections.Counter()
l_count = 0
rw = collections.Counter(a)
r_count = n
res = [0] * (n - 1)
for i in range(n - 1):
    lw[a[i]] += 1
    l_count += 1
    rw[a[i]] -= 1
    r_count -= 1
    res[i] = res[i - 1] + (r_count - rw[a[i]]) - (l_count - lw[a[i]])
    # 第0次循环不需要单独加判断，因为res[-1]=res[0]=0

print(' '.join(map(str, res)))