'''

题目描述
问题描述：数独（Sudoku）是一款大众喜爱的数字逻辑游戏。玩家需要根据9X9盘面上的已知数字，推算出所有剩余空格的数字，并且满足每一行、每一列、每一个粗线宫内的数字均含1-9，并且不重复。
输入：
包含已知数字的9X9盘面数组[空缺位以数字0表示]
输出：
完整的9X9盘面数组

输入描述:
包含已知数字的9X9盘面数组[空缺位以数字0表示]

输出描述:
完整的9X9盘面数组

示例1
输入
复制
0 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
0 4 5 2 7 6 8 3 1
输出
复制
5 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
9 4 5 2 7 6 8 3 1
'''




matrix = [[] for i in range(9)]

for i in range(9):
    input_list = list(map(int,input().split()))
    matrix[i] = input_list



def check(matrix,row,column,value):
    for i in range(9):
        if matrix[row][i] == value or matrix[i][column] == value:
            return False
    area_row = (row // 3) * 3
    area_col = (column // 3) * 3
    for i in range(area_row, area_row + 3):
        for j in range(area_col, area_col + 3):
            if matrix[i][j] == value:
                return False
    return True

def solveSudoku(matrix,count=0):
    """
    遍历每一个未填元素，遍历1-9替换为合适的数字
    """
    if (count==81):#递归出口
        return True
    row=count//9#行标
    col=count%9#列标
    if (matrix[row][col]!=0):#已填充
        return solveSudoku(matrix,count=count+1)
    else:#未填充
        for i in range(1,10):
            if check(matrix,row,col,i):#找到可能的填充数
                matrix[row][col]=i
                if solveSudoku(matrix,count=count+1):#是否可完成
                    return True#可完成
                #不可完成
                matrix[row][col]=0#回溯
        return False#不可完成

solveSudoku(matrix)
print(len(matrix))
print(matrix)
