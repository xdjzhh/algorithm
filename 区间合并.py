
temp = [[1,10],[22,56],[5,16]]
# 按每段病句[l, r]的第一个位置l排序
temp = sorted(temp, key=lambda x: x[0])

# [[1, 10]]
ret = [temp[0]]

# 与之后的病句段进行比较
for item in temp[1:]:

    # res[-1][1] == 10从后往前取
    # item == [32, 45], item[0] == 32
    if ret[-1][1] >= item[0]:
        # 贪心：对 [l1,r1], [l2,r2]，如果 r1 > l2，则 r1 = max(r1, r2)
        # [5, 16], [16, 32], 16 >= 16, max(16, 32) ---> [5, 32]
        ret[-1][1] = max(ret[-1][1], item[1])
    else:
        # [[1, 10], [32, 45]]
        ret.append(item)

s = ''

# 不取最后一位，因为最后一位末尾不添加分号
for item in ret[:-1]:
    s += str(item[0]) + ',' + str(item[1]) + ';'

# 单独处理
s += str(ret[-1][0]) + ',' + str(ret[-1][1])

print(s)