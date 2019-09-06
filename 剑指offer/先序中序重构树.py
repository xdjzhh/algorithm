class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    '''对tin.index(pre[0])的理解很重要，这个值刚好分割了前序的左右子树'''
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        tinL = tin[:tin.index(pre[0])]
        tinR = tin[tin.index(pre[0]) + 1:]
        root.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0]) + 1], tinL)
        root.right = self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1:], tinR)
        return root

    '''自设定一个index来操作前序的左右子树'''

if __name__ == '__main__':
    pre = [4,1,3,2,6,5,7]
    tin = [1,2,3,4,5,6,7]

    solution = Solution()
    root = solution.reConstructBinaryTree(pre,tin)
    print(root.left.right.val)