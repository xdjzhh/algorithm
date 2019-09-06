# coding=utf-8
class Graph(object):
    def __init__(self, maps):
        self.maps = maps
        self.nodenum = self.get_nodenum()
        self.edgenum = self.get_edgenum()

    def get_nodenum(self):
        return len(self.maps)

    def get_edgenum(self):
        count = 0
        for i in range(self.nodenum):
            for j in range(i):
                if self.maps[i][j] > 0 and self.maps[i][j] < 9999:
                    count += 1
        return count

    '''此算法可以称为“加边法”，初始最小生成树边数为0，每迭代一次就选择一条满足条件的最小代价边，加入到最小生成树的边集合里。'''
    def kruskal(self):
        res = []
        if self.nodenum <= 0 or self.edgenum < self.nodenum - 1:
            return res
        edge_list = []
        for i in range(self.nodenum):
            for j in range(i, self.nodenum):
                if self.maps[i][j] < 9999:
                    edge_list.append([i, j, self.maps[i][j]])  # 按[begin, end, weight]形式加入
        edge_list.sort(key=lambda a: a[2])  # 已经排好序的边集合

        '''初始化 所有顶点为单独的集合'''
        group = [[i] for i in range(self.nodenum)]
        # for edge in edge_list:
        #     for i in range(len(group)):
        #         if edge[0] in group[i]:
        #             m = i
        #         if edge[1] in group[i]:
        #             n = i
        #     if m != n:
        #         res.append(edge)
        #         group[m] = group[m] + group[n]
        #         group[n] = []
        '''根据边搜寻顶点，将相连的边归为一个集合'''
        for edge in edge_list:
            for i in range(len(group)):
                '''如果edge【0】在集合i中，记录集合i为m'''
                if edge[0] in group[i]:
                    m = i
                '''如果edge【1】在集合i中，记录集合i为n'''
                if edge[1] in group[i]:
                    n = i
            '''如果m==n  那么说明edge的两端点已经在一个集合，若不等 则合并'''
            if m != n:
                res.append(edge)
                group[m] = group[m] + group[n]
                group.pop(n)
                print(len(group))
        return res

    '''此算法可以称为“加点法”，每次迭代选择代价最小的边对应的点，加入到最小生成树中。算法从某一个顶点s开始，逐渐长大覆盖整个连通网的所有顶点。'''
    def prim(self):
        res = []
        if self.nodenum <= 0 or self.edgenum < self.nodenum - 1:
            return res
        res = []
        seleted_node = [0]
        candidate_node = [i for i in range(1, self.nodenum)]

        while len(candidate_node) > 0:
            begin, end, minweight = 0, 0, 9999

            '''此算法两个集合u，v， 每一步选取u中点与v中点能构成的边中代价最小值'''

            for i in seleted_node:
                for j in candidate_node:
                    print('边与代价：{}'.format([i,j,maps[i][j]]))
                    if self.maps[i][j] < minweight:
                        minweight = self.maps[i][j]
                        begin = i
                        end = j
            print('选择最小代价边为：{}'.format([begin,end,minweight]))
            print('==============================')
            res.append([begin, end, minweight])
            seleted_node.append(end)
            candidate_node.remove(end)
        return res


max_value = 9999
row0 = [0, 7, max_value, max_value, max_value, 5]
row1 = [7, 0, 9, max_value, 3, max_value]
row2 = [max_value, 9, 0, 6, max_value, max_value]
row3 = [max_value, max_value, 6, 0, 8, 10]
row4 = [max_value, 3, max_value, 8, 0, 4]
row5 = [5, max_value, max_value, 10, 4, 0]
maps = [row0, row1, row2, row3, row4, row5]
graph = Graph(maps)
print('邻接矩阵为\n%s' % graph.maps)
print('节点数据为%d，边数为%d\n' % (graph.nodenum, graph.edgenum))
print('------最小生成树kruskal算法------')
print(graph.kruskal())
print('------最小生成树prim算法')
print(graph.prim())

