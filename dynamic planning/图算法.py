'''

dijstra：无法解决负权重问题，选择每一次便利的最短路径保存，详见：https://www.cnblogs.com/biyeymyhjob/archive/2012/07/31/2615833.html：

    假如 A-B：6 ，，，，  A-C-B：4  A-C-D：5 A-C-E：6 这三个集合中选A-C-B更新 因为找不到A-C-*的任意路径比A-C-B大 只需比较A-C-B A-B就能确定B的值


floyd：带权图中的多源最短路径，动态规划
    k为被通过的点 所以问题分为  不通过k点   dp[i][j]
                            通过所有k点   dp[i][k]+dp[k][j]    例  dp[0][1]会比较  dp[0][1], dp[0][0]+dp[0][1], dp[0][1]+dp[1][1], dp[0][2]+dp[2][1]


Bellman Ford：回路不可为负权，

'''
import sys

def dijstra(matrix,source_point):
    remain = [i for i in range(len(matrix))]
    print(remain)
    remain.remove(source_point)
    print(remain)

    # distance = [[maxint]*len(matrix) for i in range(len(matrix))]
    #
    # for i in range(len(matrix)):
    #     distance[i][i] = 0

    raw_dis = 0
    popvalue = source_point
    while remain != []:
        minvalue = maxint


        '''更新到原点到每个点的距离'''
        for j in remain:
            if raw_dis + matrix[popvalue][j] < matrix[source_point][j]:
                matrix[source_point][j] = raw_dis + matrix[popvalue][j]
            print(j, matrix[source_point][j])

        '''比较取得最短的距离，记录最短距离及最短距离的点 j'''
        for j in remain:
            if minvalue > matrix[source_point][j]:
                minvalue = matrix[source_point][j]
                popvalue = j


        print(popvalue)
        '''删除以确定的最短距离点 popvalue'''
        remain.remove(popvalue)
        raw_dis = matrix[source_point][popvalue]
        print('raw_dis:{}'.format(raw_dis))
    print(matrix)
    pass


def floyd(matrix):
    n = len(matrix)
    # dp = [[maxint]*n for i in range(n)]
    # for i in range(n):
    #     dp[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])

    print(matrix)
    return matrix[0]

    pass

def bellman(matrix):   #BELLMAN 是对边进行遍历 而不是点
    '''
    bool Bellman_Ford()
    {
        for (int i = 1; i <= nodenum; ++i) //初始化
            dis[i] = (i == original ? 0 : INF);
        for (int i = 1; i <= nodenum - 1; ++i)
            for (int j = 1; j <= edgenum; ++j)
                if (dis[edge[j].v] > dis[edge[j].u] + edge[j].cost) //松弛（顺序一定不能反~）
                {
                    dis[edge[j].v] = dis[edge[j].u] + edge[j].cost;
                    pre[edge[j].v] = edge[j].u;
                }
        bool flag = 1; //判断是否含有负权回路
        for (int i = 1; i <= edgenum; ++i)
            if (dis[edge[i].v] > dis[edge[i].u] + edge[i].cost)
            {
                flag = 0;
                break;
            }
        return flag;
    }

    void print_path(int root) //打印最短路的路径（反向）
    {
        while (root != pre[root]) //前驱
        {
            printf("%d-->", root);
            root = pre[root];
        }
        if (root == pre[root])
            printf("%d\n", root);
    }

    int main()
    {
        scanf("%d%d%d", &nodenum, &edgenum, &original);
        pre[original] = original;
        for (int i = 1; i <= edgenum; ++i)
        {
            scanf("%d%d%d", &edge[i].u, &edge[i].v, &edge[i].cost);
        }
        if (Bellman_Ford())
            for (int i = 1; i <= nodenum; ++i) //每个点最短路
            {
                printf("%d\n", dis[i]);
                printf("Path:");
                print_path(i);
            }
        else
            printf("have negative circle\n");
        return 0;

    '''

    pass

if __name__ == '__main__':
    maxint = sys.maxsize
    print(maxint<maxint+1)
    print(maxint)
    matrix = [[0     ,6     ,3     ,maxint,maxint,maxint],

              [6     ,0     ,2     ,5     ,maxint,maxint],

              [3     ,2     ,0     ,3     ,4     ,maxint],

              [maxint,5     ,3     ,0     ,2     ,3     ],

              [maxint,maxint,4     ,2     ,0     ,5     ],

              [maxint,maxint,maxint,3     ,5     ,0     ]]
    dijstra(matrix, 0)
    print(floyd(matrix))


