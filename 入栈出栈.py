'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是
某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''


def solution(pusharray,poparray):
    pushindex = 0
    while poparray:
        print(pusharray)
        if (pushindex<len(pusharray)) and (pusharray[pushindex] != poparray[0]):
            pushindex +=1
        elif (pushindex<len(pusharray)) and (pusharray[pushindex] == poparray[0]):
            pusharray.pop(pushindex)
            poparray.pop(0)
            pushindex -= 1
        else:
            return False
    return True

# -*- coding:utf-8 -*-
class Solution:

    def IsPopOrder(self, pushV, popV):
        # stack中存入pushV中取出的数据
        stack = []
        while popV:
            # 如果第一个元素相等，直接都弹出，根本不用压入stack
            if pushV and popV[0] == pushV[0]:
                popV.pop(0)
                pushV.pop(0)
            # 如果stack的最后一个元素与popV中第一个元素相等，将两个元素都弹出
            elif stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            # 如果pushV中有数据，压入stack
            elif pushV:
                stack.append(pushV.pop(0))
            # 上面情况都不满足，直接返回false。
            else:
                return False
        return True


if __name__ == '__main__':
    pusharray = [1,2,3,4,5]
    poparray = [4,5,3,2,1]
    print(solution(pusharray,poparray))
