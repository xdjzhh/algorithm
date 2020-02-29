s = input()
score = 0
digit_num = 0  # 密码中数字的个数
upper_num = 0  # 密码中大写字母的个数
lower_num = 0  # 密码中小写字母的个数
index_num = 0  # 密码中符号的个数
for i in s:  # 遍历密码，确定上述各项的值
    if i.isdigit():
        digit_num += 1
    elif i.isupper():
        upper_num += 1
    elif i.islower():
        lower_num += 1
    else:
        index_num += 1
n = len(s)
if n <= 4:
    score += 5  # 密码长度小于等于4，分值加5
elif n <= 7:
    score += 10  # 密码长度大于等于5小于等于7，分值加10
else:
    score += 25  # 密码长度大于等于8，分值加25
if digit_num == 0:  # 密码中数字个数为0，分值加0
    score += 0
elif digit_num == 1:  # 密码中数字个数为1，分值加10
    score += 10
else:  # 密码中数字个数大于1，分值加20
    score += 20
if index_num == 0:  # 密码中符号个数为0，分值加0
    score += 0
elif index_num == 1:  # 密码中符号个数为1，分值加10
    score += 10
else:  # 密码中符号个数大于1，分值加25
    score += 25
if upper_num == 0 and lower_num == 0:  # 密码中大小写字母个数都为0，分值加0
    score += 0
# elif upper_num==n or lower_num==n:#密码中大（小）写字母个数为n（密码长度），分值加10
#    score+=10
# elif upper_num!=0 and lower_num!=0 and ((upper_num+lower_num)==n):#密码为大小写混合字母，分值加20
#    score+=20
elif upper_num == 0 or lower_num == 0:  # 密码中的字母都为大（小）写字母，分值加10（这里应该不要求密码全是字母————但还是不对，问题到底在哪？）
    score += 10
else:
    score += 20  # 密码中的大（小）写字母混合，分值加20
if digit_num != 0 and (upper_num != 0 or lower_num != 0):  # 密码中有数字和字母，分值加2
    score += 2
elif digit_num != 0 and (upper_num != 0 or lower_num != 0) and index_num != 0:  # 密码中有数字、字母和符号，分值加3
    score += 3
elif upper_num != 0 and lower_num != 0 and digit_num != 0 and index_num != 0:  # 密码中有数字、大小写字母和符号，分值加5
    score += 5
if score >= 90:
    print('VERY_SECURE')
elif score >= 80:
    print('SECURE')
elif score >= 70:
    print('VERY_STRONG')
elif score >= 60:
    print('STRONG')
elif score >= 50:
    print('AVERAGE')
elif score >= 25:
    print('WEAK')
else:
    print('VERY_WEAK')