
'''
题目描述
给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，每辆火车以数字1-9编号。要求以字典序排序输出火车出站的序列号。
输入描述:
有多组测试用例，每一组第一行输入一个正整数N（0<N<10），第二行包括N个正整数，范围为1到9。

输出描述:
输出以字典序从小到大排序的火车出站序列号，每个编号以空格隔开，每个输出序列换行，具体见sample。

示例1
输入
复制
3
1 2 3
输出
复制
1 2 3
1 3 2
2 1 3
2 3 1
3 2 1

'''

from copy import copy

number= int(input())

input_seq = list(input().split())
result1 = []
result2 = []

def simulate(input_seq,stack,out,dopush):
    if len(input_seq) == 0:
        if dopush:
            return
        else:
            while len(stack) != 0:
                out.append(stack.pop())

            result1.append(copy(out))
            return
    else:
        if dopush:
            stack.append(input_seq.pop(0))
        else:
            if len(stack) != 0 :
                out.append(stack.pop())
            else:
                return

        simulate(input_seq.copy(),stack.copy(),out.copy(),True)
        simulate(input_seq.copy(),stack.copy(),out.copy(),False)



def simulate2(input_seq,stack,out):
    if len(input_seq) == 0 and len(stack) == 0:
        result2.append(out)
    else:
        if len(input_seq) !=0:
            temp_input_seq = input_seq.copy()
            temp_stack = stack.copy()
            temp_out = out.copy()
            temp_stack.append(temp_input_seq.pop(0))
            simulate2(temp_input_seq,temp_stack,temp_out)
        if len(stack) != 0:
            temp_input_seq = input_seq.copy()
            temp_stack = stack.copy()
            temp_out = out.copy()
            temp_out.append(temp_stack.pop())
            simulate2(temp_input_seq, temp_stack, temp_out)


simulate(input_seq,[],[],True)
simulate2(input_seq,[],[])
print(sorted(result1))

print(sorted(result2))