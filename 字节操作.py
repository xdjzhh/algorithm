
'''题目描述
编写一个截取字符串的函数，输入为一个字符串和字节数，输出为按字节截取的字符串。但是要保证汉字不被截半个，如"我ABC"4，应该截为"我AB"，输入"我ABC汉DEF"6，应该输出为"我ABC"而不是"我ABC+汉的半个"。



输入描述:
输入待截取的字符串及长度

输出描述:
截取后的字符串

示例1
输入
复制
我ABC汉DEF
6
输出
复制
我ABC'''

while True:
    try:
        # 测试用例中的用例，参数是两行。而提交的代码跑的用例是一行。这点需要注意！
        string, len_defined = input().strip().split()
        len_total = 0
        rst = ''
        for i in list(string):
            # 网站的Python环境，默认编码是UTF-8，这样一个汉字占用三个字节。
            # 而题目的意思应该默认编码是gbk，一个汉字占用两个字节。
            # 因此，为了保险起见，在代码中应特别指明encode的方式。
            len_total += len(i.encode('gbk'))
            if len_total <= int(len_defined):
                rst += i
        print(rst)

    except:
        break