# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 == None or pRoot2 == None:
            return False

        result = False
        if pRoot1.val == pRoot2.val:
            result = self.check(pRoot1,pRoot2)


        if result == False:
            result = self.HasSubtree(pRoot1.left,pRoot2)
        if result == False:
            result = self.HasSubtree(pRoot1.right,pRoot2)

        return result

        pass

    def check(self,t1,t2):
        if t2 == None:
            return True
        if t1 ==None:
            return False

        if t1.val == t2.val:
            return self.check(t1.left,t2.left) and self.check(t1.right,t2.right)
        else:
            return False






if __name__ == '__main__':
    pass