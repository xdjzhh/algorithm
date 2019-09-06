'''

对于一个链表 L: L0→L1→…→Ln-1→Ln,
将其翻转成 L0→Ln→L1→Ln-1→L2→Ln-2→…
输入是一串数字，请将其转换成单链表格式之后，再进行操作

'''


class listnode:
    def __init__(self, x):
        self.val = x
        self.next = None


class solution:
    def ReverseList(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        pre = None
        cur = pHead
        while cur != None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def change(self,head,number):
        new_head = head
        '''将head链 分成两段'''
        for i in range((number//2)):
            new_head = new_head.next
        temp = new_head.next
        new_head.next = None
        new_head = temp

        reverse_head = self.ReverseList(new_head)

        '''设置new_cur为新链，将head，reversehead的前两个添加到新连末尾， 并移动head，reversehead的头指针分别到各连的下一个'''
        new_cur = listnode(0)
        new_head = new_cur
        while head != None and reverse_head != None:
            new_cur.next = head
            new_cur = head
            head = head.next
            new_cur.next = reverse_head
            new_cur = reverse_head
            reverse_head = reverse_head.next
        if head != None:
            new_cur.next = head
        if reverse_head != None:
            new_cur.next = reverse_head

        # while new_head != None:
        #     print(new_head.val)
        #     new_head = new_head.next
        string = new_head.next.val
        new_head = new_head.next.next
        while new_head != None:
            print(string)
            string = string + ',' + new_head.val
            new_head = new_head.next
        return string
        # return new_head.next
        pass


if __name__ == '__main__':
    string = input().split(',')
    head = listnode(string[0])
    node = head
    for index in range(1, len(string)):
        new_node = listnode(string[index])
        node.next = new_node
        node = new_node
    solution = solution()
    print(solution.change(head,len(string)-1))

