
class solution:
    def __init__(self,matrix,point_number,start):
        self.matrix = matrix
        self.path = [start,]
        self.point_number = point_number
        self.visited = [0 for i in range(point_number+1)]
        self.visited[start] = 1

    def dfs(self,start):
        i = 1
        # print(start)
        while i < self.point_number + 1:
            print(self.matrix[start][i],i)
            if (self.matrix[start][i] == 1) & (self.visited[i] != 1):
                self.visited[i] = 1
                '''成功寻路，递归下一层，将这一层的点加入path'''
                self.path.append(i)
                self.dfs(i)
                '''寻路未成功，返回上一层，将上一层的点加入path'''
                self.path.append(start)

            i+=1





if __name__ == '__main__':
    string = input().split(' ')
    point_number = int(string[0])
    ledge_number = int(string[1])
    start = int(string[2])

    '''可用两种结构 字典关系 和 矩阵'''
    '''矩阵:'''
    ledge_list = []
    for i in range(ledge_number):
        string = input().split(' ')
        ledge_list.append([int(string[0]),int(string[1])])

    matrix = [[0]*(point_number+1) for i in range(point_number+1)]

    for i in ledge_list:
        matrix[i[0]][i[1]] = 1
        matrix[i[1]][i[0]] = 1
    print(ledge_list)
    print(matrix)

    solution = solution(matrix,point_number,start)
    print(solution.visited)
    solution.dfs(1)
    print(solution.path)