'''

给出一个有n个整数的数组S，在S中找到三个整数a, b, c，找到所有使得a + b + c = 0的三元组。
输入:[2,7,11,15]
输出:[]
输入:[-1,0,1,2,-1,-4]
输出:[[-1, 0, 1],[-1, -1, 2]]

思路：先排序，然后固定遍历数组i，list[i：]的数设置start end指针 判断哪些数字能使 input_list[i] + input_list[start] + input_list[end] == 0
'''

def solution(input_list):
    res = []

    input_list = sorted(input_list)
    for i in range(len(input_list)):
        start = i +1
        end = len(input_list)-1
        if input_list[i] == input_list[i - 1]:
            continue
        while start < end:
            numsum = input_list[i] + input_list[start] + input_list[end]
            if numsum < 0:
                start +=1
            elif numsum > 0:
                end -=1
            else:
                res.append([input_list[i] , input_list[start] , input_list[end]])
                start +=1
                end -=1
                # 循环中nums[i]已确定，当再确定1个数时，另一个数也确定，左右端任一端出现重复均可跳过
                while input_list[start] == input_list[start-1] and start < end:
                    start += 1
                while input_list[end] == input_list[end+1] and start < end:
                    end -= 1



    return res
    pass


if __name__ == '__main__':
    input_list = [-1,0,1,2,-1,-4]
    print(solution(input_list))