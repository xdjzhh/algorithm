def heap_sort(lst):
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1

            '''child这个index 大于 end index说明这个root下没有子节点'''
            if child > end:
                break

            '''root这个index下有子节点，对比大小，用大的child进行交换判断'''
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1

            '''交换判断，若root 小于 child 交换'''
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

# 创建最大堆
    # 从最后一个有子节点的孩子还是调整最大堆
    for start in range((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)

    print(lst)

# 堆排序
    # 将最大的放到堆的最后一个, 堆-1, 继续调整排序
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return lst



if __name__ == "__main__":
    l = [9, 2, 1, 7, 6, 8, 5, 3, 4]
    print(heap_sort(l))