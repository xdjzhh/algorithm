
import copy

class solution:
    def __init__(self,matrix):
        self.matrix = matrix
        self.path = []
        self.row = len(matrix[0])
        self.column = len(matrix)
        self.path_list = []
        self.flag = False

    def dfs(self,x,y,energy):
        if self.flag == True:
            return
        if (0 <=y< self.row) & (0 <=x< self.column) & (energy >= 0):
            if matrix[x][y] == 1:
                self.path.append([x,y])
                '''设置已通过的路径为0，使下一步递归不会重复点'''
                self.matrix[x][y] = 0
                if (x == self.row - 1) & (y == self.column - 1):

                    '''设置flag，找到结果后，提前跳出递归，若需要寻找最短路径 则不需要flag，因为需要全剧扫描比较'''

                    self.flag = True

                    '''若需要比较大小也可在此处'''
                    new_path = copy.deepcopy(self.path)
                    self.path_list.append([new_path,energy])
                    print(self.path)

                    '''若无最小小要求 无需后面两步，若有 则需退回前一层'''
                    self.path.pop(-1)
                    self.matrix[x][y] = 1
                    return
                else:
                    self.dfs(x, y+1, energy-1)
                    self.dfs(x+1, y, energy)
                    self.dfs(x-1, y, energy-3)
                    self.dfs(x, y-1, energy-1)


                    self.path.pop(-1)
                    self.matrix[x][y] = 1
                return

        else:
            return



if __name__ == '__main__':

    matrix = [[1   ,1   ,1   ,0   ,0],
              [1   ,0   ,0   ,1   ,1],
              [1   ,1   ,1   ,1   ,1],
              [1   ,0   ,1   ,1   ,0],
              [1   ,1   ,0   ,1   ,1]]

    solution = solution(matrix)
    solution.dfs(0,0,8)
    print(solution.path_list)