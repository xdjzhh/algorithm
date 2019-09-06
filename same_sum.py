

def same_sum(number_list,sum):
    new_list = []
    for i in number_list:
        new_list.append(sum - i)

    for each in new_list:
        if each in number_list:
            print(str(each) + ' ' + str(sum - each))




def rec(i, m, res):
    ans = []
    for j in range(i, n + 1):
        if j == m:
            ans.extend([x + [j] for x in res])
            break
        if j < m:
            ans.extend(rec(j + 1, m - j, [x + [j] for x in res]))
        else:
            continue
    return ans


'''
此问题过程大概为：
1 sumofknum(sum,n-1)  ：  【1,2,3,4,5】 sum为6  =>   【1,2,3,4】 sum为6 ，【1,2,3】 sum为6 ，【1,2】 sum为6 ，【1】 sum为6
2 sumofknum(sum-n,n-1)=>sumofknum(sum,n-1)：  【1,2,3,4,5】 sum为6  =>   【1,2,3,4】 sum为1 ，【1,2,3】 sum为1 ，【1,2】 sum为1 ，【1】 sum为1加入list
3 sumofknum(sum-n,n-1)=>sumofknum(sum,n-1)：  【1,2,3,4】   sum为6  =>   【1,2,3】 sum为2 ，【1,2】 sum为2 加入list，【1】 sum为1
'''

res_list = []
def sumofknum(sum,n):


    if n<= 0 or sum <= 0:
        return


    #如果 sum 和 n相等 说明 递归中的sum 找到了和之前sum的匹配值    sum0- n(x) = sum1
    if sum == n:
        print(' '.join(str(i) for i in res_list) + ' ' +str(n))
        print('===================')
    res_list.append(n)
    sumofknum(sum-n,n-1)
    res_list.pop(-1)
    sumofknum(sum,n-1)




if __name__ == '__main__':
    sumofknum(6,9)
    # n, m = [int(x) for x in input().split()]
    # ans = rec(1, m, [[]])
    # for a in ans:
    #     print(' '.join([str(x) for x in a]))





# if __name__ == "__main__":
#     same_sum([1,2,3,4,5],6)