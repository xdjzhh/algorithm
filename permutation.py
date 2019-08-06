import itertools
import copy

def method_1(string):
    permutation_list = itertools.permutations(string,len(string))
    combination_list = itertools.combinations(string,2)
    return permutation_list,combination_list


def perm(listVar):  #全排列  但不能取其中几个
    if len(listVar) == 1:
        return [listVar]

    retlist = []

    for i in range(len(listVar)):

        # 得到一个新的列表，列表中去掉了i指向的元素

        restList = listVar[:i] + listVar[i + 1:]

        # 1

        # perm([2,3])-> [[2,3],[3,2]]

        # 1 加到 perm(2,3) 的结果中去

        perResult = perm(restList)

        for x in perResult:
            # 习题：此行代码是否可以这样写，为何？ listVar[i] is int ,listVar[i:i+1] is list,x is list

            # retlist.append(listVar[i]+x)

            retlist.append(listVar[i:i + 1] + x)

    return retlist


def lexicographically_next_permutation(a):  #顺序要求从小到大
    """
    Generates the lexicographically next permutation.

    Input: a permutation, called "a". This method modifies
    "a" in place. Returns True if we could generate a next
    permutation. Returns False if it was the last permutation
    lexicographically.
    """
    i = len(a) - 2
    while not (i < 0 or a[i] < a[i + 1]):
        i -= 1
    if i < 0:
        return False
    # else
    j = len(a) - 1
    while not (a[j] > a[i]):
        j -= 1
    a[i], a[j] = a[j], a[i]  # swap
    a[i + 1:] = reversed(a[i + 1:])  # reverse elements from position i+1 till the end of the sequence
    return True


def mycombination(lis=[],m=0):
    allAns = []                    #用来存储所有递归中的子列表
    ans = [None for i in range(m)] #预先填充m个None,用来存储每次递归中的子列表
    subLists(lis,m,ans,allAns)
    return allAns

def subLists(lis=[],m=0,ans=[],allAns=[]):   #combination   不重复的组合
    # recursive function  codes
    if m==0:
        # m==0是某次递归返回的条件之一：子列表的第三个数已经选出。
        # 意味着已到达某个方向的最大递归深度

        allAns.append(ans.copy())
        #这里有意思了，如果不用copy,那么ans即使已经存储在allAns，也会被其它递归方向中的ans刷新

        return
    if len(lis)<m:
        # 递归函数直接返回的条件之一：从4个数里面选5个数出来是不可能的。
        print("short list!")
        return
    length=len(lis)
    for iter in range(length-m+1):  #可以作为子列表一员的数在lis中的index
        ans[-m]=lis[iter]           #lis[iter]作为子列表倒数第m个数
        if iter+1<length:           #可以调用递归函数的条件：保证lis[iter+1:]里面还有东东才行
            subLists(lis[iter+1:],m-1,ans,allAns)
        else:
            allAns.append(ans.copy())
            return
#############################################################################


if __name__ =='__main__':
    stringlist = 'abc'
    # list1,list2= method_1(string)
    # for i in list1:
    #     print(i)
    # for i in list2:
    #     print(i)
    # print(perm([1,2,3,4]))
    # li = [1,2,4,3]
    # while lexicographically_next_permutation(li):  # 除【1,2,3,4】外的所有排列
    #     print(li)  # process

    print(mycombination([1,2,3,4],2))
