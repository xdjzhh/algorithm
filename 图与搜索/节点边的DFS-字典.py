
class solution:
    def __init__(self,point_dict,point_number,start):
        self.point_dict = point_dict
        self.path = [start,]
        self.point_number = point_number
        self.visited = [0 for i in range(point_number+1)]
        self.visited[start] = 1
        pass

    def dfs(self,start):
        print(sorted(self.point_dict[start]))
        for i in sorted(self.point_dict[start]):
            if self.visited[i] != 1:
                self.visited[i] = 1
                self.path.append(i)
                self.dfs(i)
                self.path.append(start)





if __name__ == '__main__':
    string = input().split(' ')
    point_number = int(string[0])
    ledge_number = int(string[1])
    start = int(string[2])

    '''可用两种结构 字典关系 和 矩阵'''
    '''字典:'''
    point_dict = {}
    for i in range(1,point_number+1):
        point_dict[i] = []

    for i in range(ledge_number):
        string = input().split(' ')
        point_dict[int(string[0])].append(int(string[1]))
        point_dict[int(string[1])].append(int(string[0]))

    print(point_dict)
    solution = solution(point_dict,point_number,start)
    solution.dfs(start)
    print(solution.path)
