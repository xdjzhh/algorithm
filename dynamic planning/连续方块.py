class Solution {
public:
    int rectCover(int number) {
        if (number <= 0)
            return 0;
        if (number == 1)
            return 1;
        if (number == 2)
            return 2;
        vector<int> f(number + 1, 0);
        //初始化
        f[0] = 0;
        f[1] = 1;
        f[2] = 2;
        for (int i = 3; i <= number; i++)
        {
            //状态递推
            f[i] = f[i - 1] + f[i - 2];
        }
        //返回结果
        return f[number];
    }
};



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