'''


题目描述
计算最少出列多少位同学，使得剩下的同学排成合唱队形

说明：

N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学排成合唱队形。
合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1，2…，K，他们的身高分别为T1，T2，…，TK，   则他们的身高满足存在i（1<=i<=K）使得T1<T2<......<Ti-1<Ti>Ti+1>......>TK。
你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。



输入描述:
整数N

输出描述:
最少需要几位同学出列

示例1
输入
复制
8
186 186 150 200 160 130 197 200
输出
复制
4
'''



'''使用pypy跑！！！！！！！！！！！'''


from array import array
while True:
    try:
        number = int(input())
        talls = [int(i) for i in input().split(' ')]
        talls = array('I',talls)


        dp_left = [1] * (number)
        dp_right = [1] * (number)

        for i in range(len(talls)):
            for j in range(i):
                if talls[i] > talls[j]:
                    dp_left[i] = max(dp_left[i], dp_left[j] + 1)

        for i in range(len(talls) - 1, -1, -1):
            for j in range(len(talls) - 1, i, -1):
                if talls[i] > talls[j]:
                    dp_right[i] = max(dp_right[i], dp_right[j] + 1)

        result = 0
        for i in range(len(talls)):
            result = max(result, dp_left[i] + dp_right[i])

        print(number - result + 1)
    except:
        break