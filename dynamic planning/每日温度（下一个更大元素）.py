
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


'''正序遍历'''
class Solution:
    def dailyTemperatures(self, T):
        stack = []
        result = [0 for i in range(len(T))]
        for index in range(len(T)):
            if stack == []:
                stack.append((index,T[index]))
            if T[index] < stack[-1][1]:
                stack.append((index,T[index]))
            else:
                while (stack != []) and (T[index] > stack[-1][1]):
                    current = stack.pop(-1)
                    result[current[0]] = index - current[0]
                stack.append((index,T[index]))
        return result

if __name__ == '__main__':
    temperature = [73, 74, 75, 71, 69, 72, 76, 73]
    print(solution2(temperature))
