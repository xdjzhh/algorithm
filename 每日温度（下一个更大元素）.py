'''
根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
。
方法一：
题目要求我们找出下一次温度比当天高距离的天数。因为温度只能在 [30，100] 之内，如果现在的温度是 T[i]=50，我们只需要找到下一个出现的 51，52，…，100，然后取最快出现的那个位置。

算法：

我们按逆序遍历列表，对于每个 T[i]，我们要知道 (T[i],100] 温度所出现的位置，为此我们用一个 next 数组记录该数据，若当前位置出现 T[i]=100，则我们将该索引记录在 next[100]。
warmer_index 记录比当前温度高的索引位置，它等于 next[T[i]+1], next[T[i]+2], ..., next[100] 的最小值。

思路 ：通俗讲就是用[30, 100]的数组从后往前逐步嵌套 温度的index（当温度重复出现时，覆盖温度的index，因为求的是最近的温度index，所以要逐步嵌套）
def dailyTemperatures(T):
    nxt = [float('inf')] * 102
    print(nxt)
    ans = [0] * len(T)
    for i in range(len(T) - 1, -1, -1):
        print(i)
        #Use 102 so min(nxt[t]) has a default value
        print([nxt[t] for t in range(T[i]+1, 102)])
        warmer_index = min(nxt[t] for t in range(T[i]+1, 102))
        print(warmer_index)
        if warmer_index < float('inf'):
            ans[i] = warmer_index - i
        nxt[T[i]] = i
    return ans

print(dailyTemperatures([73, 74, 75, 71, 69,71, 72, 76, 73]))
'''

def solution1(T): #O(nw)
    res = []
    compare = [30001 for i in range(102)]   #index最大值为30000，共 0-100   102个温度标
    for i in range(len(T)-1,-1,-1):
        index = []
        for j in range(T[i]+1,102):
            index.append(compare[j])
        warmer = min(index)
        if warmer != 30001:
            res.insert(0,warmer-i)
        else:
            res.insert(0, 0)
        compare[T[i]] = i

    return res
    pass


'''
方法二：栈
我们需要找到比当前 T[i] 温度更高的位置，那么必须要记录哪些信息？
我们试着找到 T[0] 过后温度升高的位置。如果知道 T[10]=50，则 T[20]=50 是无效信息，因为 T[i] 在 T[20] 以前已经到达了 50。如果 t[20]=100 将是有用的信息，因为如果 t[0]=80，那么 T[20] 将有可能是它的下一个温度升高的位置，而 T[10] 则不可能是。
因此，我们需要记住一个索引的列表，索引代表的温度严格递增。我们可以利用栈来实现这样的效果。
算法：

我们用栈记录索引，满足 T[stack[-1]] < T[stack[-2]] < ...，其中 stack[-1] 是栈的顶部，stack[-2] 是从顶部开始的第二个元素，依此类推；我们将在处理每个 T[i] 时保持 stack[-1] > stack[-2] > ...。
我们通过当前温度和栈顶索引所代表的温度比较来找到温度升高的位置。
举个例子：我们反向遍历处理 t=[73，74，75，71，69，72，76，73] ，通过看栈元素的变化来理解是如何工作的。为了清楚 stack 只包含索引 i，但是将把 T[i] 的值写在旁边的括号中，例如 0 (73)。
当 i = 7，stack = [7 (73)]。ans[i] = 0。
当 i = 6，stack = [6 (76)]。ans[i] = 0。
当 i = 5，stack = [6 (76),5 (72)]。ans[i] = 1。
当 i = 4，stack = [6 (76),5 (72),4 (69)]。ans[i] = 1。
当 i = 3，stack = [6 (76),5 (72),3 (71)]。ans[i] = 2。
当 i = 2，stack = [6 (76),2 (75)]。ans[i] = 4。
当 i = 1，stack = [6 (76),2 (75),1 (74)]。ans[i] = 1。
当 i = 0，stack = [6 (76),2 (75),1 (74),0 (73)]。ans[i] = 1。

思路： 只保留比当前T[i]大的温度，stack必为递减，扣除了在stack[-1] -stack[-2]之间比stack[-1]更小的数


'''
def solution2(temperature):  #O(n)
    res = []
    stack = []
    for i in range(len(temperature)-1,-1,-1):
        while stack and temperature[i] >= temperature[stack[-1]]:
            stack.pop()
        if stack:
            res.insert(0,stack[-1]-i)
        else:
            res.insert(0, 0)
        stack.append(i)

    return res


if __name__ == '__main__':
    temperature = [73, 74, 75, 71, 69, 72, 76, 73]
    print(solution1(temperature))
    print(solution2(temperature))
