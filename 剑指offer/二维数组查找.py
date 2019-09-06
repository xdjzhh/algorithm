
'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


/* 思路
* 矩阵是有序的，从左下角来看，向上数字递减，向右数字递增，
* 因此从左下角开始查找，当要查找数字比左下角数字大时。右移
* 要查找数字比左下角数字小时，上移
'''


def solution(matrix,target):

    i = len(matrix)-1
    j = 0

    while 0<= i <len(matrix) and 0<= j <len(matrix):
        if target > matrix[i][j]:
            j+=1
        if target < matrix[i][j]:
            i-=1
        if target == matrix[i][j]:
            return [i,j]
    return False
    pass



if __name__ == '__main__':
    matrix = [[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20],
              [21,22,23,24,25]]
    target = 13

    print(solution(matrix,target))