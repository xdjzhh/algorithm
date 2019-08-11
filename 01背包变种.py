

def getMaxGain(n, x, y):

    mx = max(x)  # 获取最大值，作为差的边界

    dp = [[0] * (mx+1) for _ in range(n+1)]  # 初始化dp

    for i in range(1, n+1):
        for j in range(mx+1):
            tmp1, tmp2 = 0, 0
            if j - x[i-1] >= 0:  # 这张卡牌给小a
                tmp1 = dp[i-1][j-x[i-1]] + y[i-1]

            if j + x[i - 1] <= mx:  # 这张卡牌给小b
                tmp2 = dp[i-1][j+x[i-1]] + y[i-1]

            dp[i][j] = max(dp[i - 1][j], tmp1, tmp2)  # 三种状态的最高得分

            if i == 1 and j == 0:  # 只有一张卡牌时
                dp[i][j] = 0
    return dp


if __name__ == '__main__':
    n = 4
    x = [3, 2, 1, 1]
    y = [1, 2, 4, 4]
    print(getMaxGain(n, x, y))


'''
using namespace std;
#include <algorithm>
 
int main()
{
	int w[5] = { 0 , 2 , 3 , 4 , 5 };			//商品的体积2、3、4、5
	int v[5] = { 0 , 3 , 4 , 5 , 6 };			//商品的价值3、4、5、6
	int bagV = 8;					        //背包大小
	int dp[5][9] = { { 0 } };			        //动态规划表
 
	for (int i = 1; i <= 4; i++) {
		for (int j = 1; j <= bagV; j++) {
			if (j < w[i])
				dp[i][j] = dp[i - 1][j];
			else
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i]);
		}
	}
 
	//动态规划表的输出
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 9; j++) {
			cout << dp[i][j] << ' ';
		}
		cout << endl;
	}
 
	return 0;
}
'''