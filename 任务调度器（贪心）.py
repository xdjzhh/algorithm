'''
思路
完成所有任务的最短时间取决于出现次数最多的任务数量。

看下题目给出的例子

输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
因为相同任务必须要有时间片为 n 的间隔，所以我们先把出现次数最多的任务 A 安排上（当然你也可以选择任务 B）。例子中 n = 2，那么任意两个任务 A 之间都必须间隔 2 个单位的时间：

A -> (单位时间) -> (单位时间) -> A -> (单位时间) -> (单位时间) -> A
中间间隔的单位时间可以用来安排别的任务，也可以处于“待命”状态。当然，为了使总任务时间最短，我们要尽可能地把单位时间分配给其他任务。现在把任务 B 安排上：

A -> B -> (单位时间) -> A -> B -> (单位时间) -> A -> B
很容易观察到，前面两个 A 任务一定会固定跟着 2 个单位时间的间隔。最后一个 A 之后是否还有任务跟随取决于是否存在与任务 A 出现次数相同的任务。

该例子的计算过程为：

(任务 A 出现的次数 - 1) * (n + 1) + (出现次数为 3 的任务个数)，即：

(3 - 1) * (2 + 1) + 2 = 8
所以整体的解题步骤如下：

计算每个任务出现的次数
找出出现次数最多的任务，假设出现次数为 x
计算至少需要的时间 (x - 1) * (n + 1)，记为 min_time
计算出现次数为 x 的任务总数 count，计算最终结果为 min_time + count
特殊情况
然而存在一种特殊情况，例如：

输入: tasks = ["A","A","A","B","B","B","C","C","D","D"], n = 2
输出: 10
执行顺序: A -> B -> C -> A -> B -> D -> A -> B -> C -> D
此时如果按照上述方法计算将得到结果为 8，比数组总长度 10 要小，应返回数组长度。

'''
from collections import Counter
def solution(task,n):
    task_count = Counter(task)
    task_count = sorted(task_count.items(),key = lambda x:x[1])
    print(task_count)
    max_count = task_count[-1][1]
    res = (max_count-1) * (n+1)
    for i in range(len(task_count)-1,-1,-1):
        print(task_count[i])
        if task_count[i][1] != max_count:
            break
        res += 1

    if res < len(task):
        res = len(task)

    return res

    pass

if __name__ == '__main__':
    task1 = ["A","A","A","B","B","B"]
    n1 = 2
    task2 = ["A","A","A","B","B","B","C","C","D","D"]
    n2 = 2
    print(solution(task1,n1))
    print(solution(task2,n2))