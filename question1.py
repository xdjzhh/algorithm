
import re
'''动态监控客户ID获得数量，创建对象 question1 之后，每输入yes true时会递增ID并判断ID是否符合要求，并计数'''
class question1:
    def __init__(self):
        self.signal = ['True','TRUE','true','Yes','YES','yes']
        self.flag = None
        self.count = 0
        self.ID = 0

    def string_id(self,number):
        if len(str(number)) < 8:
            string = '0'*(8-len(str(number)))+str(number)
            return string

    def solution(self,flag):
        self.flag = flag
        if self.flag in self.signal:
            if self.count == 0:
                self.count += 1
                return '00000000'
            else:
                self.count += 1
                self.ID += 1
                stringofID = self.string_id(self.ID)
                while (not re.match(r'[^347]{8}',stringofID)) and (self.ID < 100000000):
                    self.ID += 1
                    stringofID = self.string_id(self.ID)

                return stringofID


if __name__ == '__main__':
    answer1 = question1()
    for i in range(5):
        '''便于查看将 input（） 固定设置为字符串'''
        input_string= 'yes'
        print(answer1.solution(input_string),answer1.count)