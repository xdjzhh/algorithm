class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode == None:
            return []
        result = []
        while listNode.next != None:
            result.append(listNode.val)
            listNode = listNode.next
        result.append(listNode.val)
        return result[::-1]


if __name__ == '__main__':
    node0 = ListNode(1)
    node1 = ListNode(3)
    node2 = ListNode(5)
    node3 = ListNode(7)
    node0.next = node1
    node1.next = node2
    node2.next = node3
    solution = Solution()
    print(solution.printListFromTailToHead(node0))
