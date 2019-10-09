# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        length = len(rotateArray) - 1
        mid = length // 2
        if rotateArray[0] > rotateArray[mid]:
            new_list = rotateArray[:mid + 1]
        else:
            new_list = rotateArray[mid:]
        print(new_list)
        if len(new_list) == 2:
            return new_list[-1]

        return self.minNumberInRotateArray(new_list)

list1 = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,
         1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
solution = Solution()
print(solution.minNumberInRotateArray(list1))