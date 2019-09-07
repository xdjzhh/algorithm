# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root == None:
            return []
        result = []

        current = [root, ]
        while current != []:
            temp = []
            value_list = []
            for i in current:
                value_list.append(i.val)
                if i.left != None:
                    temp.append(i.left)
                if i.right != None:
                    temp.append(i.right)
            result.append(value_list)
            current = temp
        print(result)
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    solurion = Solution()
    solurion.PrintFromTopToBottom(root)