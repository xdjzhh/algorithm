class Solution:
    def __init__(self):
        self.dp = []
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        self.dp = [0 for i in range(number+1)]
        self.dp[1] = 1
        self.dp[2] = 2
        for i in range(3,number+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[number]


#连续数列的和
class MaxSum {
public:
    int getMaxSum(vector<int> A, int n) {
        // write code here
        if (A.empty())
            return 0;
        vector<int> f(A.size(), 0);
        //初始化
        f[0] = A[0];
        for (int i = 1; i < A.size(); i++)
        {
            //状态递推
            f[i] = max(f[i - 1] + A[i], A[i]);
        }
        //输出结果
        int resault = A[0];
        for (int i = 0; i < A.size(); i++)
        {
            resault = max(f[i], resault);
        }
        return resault;
    }
};
---------------------
版权声明：本文为CSDN博主「Billy12138」的原创文章，遵循CC 4.0 by-sa版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/flowing_wind/article/details/81949689