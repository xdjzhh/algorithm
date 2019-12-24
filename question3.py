
class question3:
    def __init__(self,number):
        self.number = number

        '''self.number_list保存所有的序列'''
        self.number_list = None
        self.count_record = None

    '''对每个序列集合做简化 筛选每个序列集合中最短的子集'''
    def shortest_list(self,temp_list):
        sorted_list = sorted(temp_list,key=lambda x:x[0])
        for i in sorted_list:
            if i[0] == sorted_list[0][0]:
                yield i
            else:
                break


    def solution(self):
        self.number_list = [[] for i in range(self.number+1)]
        self.count_record = [1000 for i in range(self.number+1)]
        if self.number <= 1:
            return 0
        if self.number == 2:
            return [[1,2],2]

        self.number_list[2].append([2,1,2])
        index = 2

        while index <= self.number:
            shortest_item = self.shortest_list(self.number_list[index])
            for each_list in shortest_item:

                '''每个保存在number_list中的列表的开头为长度，所以index从1开始'''
                for each in range(1,len(each_list)):

                    '''做每个元素与最后一个元素的和，避免重复运算'''
                    sum_index = each_list[each] + each_list[-1]

                    if sum_index <= self.number :
                        '''将每个sum_list记录为 【长度+序列】所以每个保存在number_list中的列表的开头为长度'''
                        sum_list = list([len(each_list)] + each_list[1:] + [sum_index])

                        '''记录元素个数载index =0'''
                        self.number_list[sum_index].append(sum_list)


            index += 1

        return self.shortest_list(self.number_list[self.number])

    def advanced_solution(self):
        self.number_list = [[] for i in range(self.number+1)]
        self.count_record = [1000 for i in range(self.number+1)]
        if self.number <= 1:
            return 0
        if self.number == 2:
            return [[1,2],2]

        self.number_list[2].append([2,1,2])
        index = 2
        while index <= self.number:
            for each_list in self.number_list[index]:
                for each in range(1, len(each_list)):
                    sum_index = each_list[each] + each_list[-1]

                    if sum_index <= self.number:
                        sum_list = list([len(each_list)] + each_list[1:] + [sum_index])

                        '''差别在于不用进行排序判断长度，直接保存最短长度子集'''
                        if len(each_list) < self.count_record[sum_index]:
                            self.count_record[sum_index] = len(each_list)
                            self.number_list[sum_index] = [sum_list]
                        elif len(each_list) == self.count_record[sum_index]:
                            self.number_list[sum_index].append(sum_list)
                        else:
                            continue

            index += 1
        return self.shortest_list(self.number_list[self.number])




if __name__ == '__main__':
    input_number = int(input())
    answer3 = question3(input_number)

    all_answer_list = list(answer3.solution())

    print('solution()最短递增序列的长度:{}'.format(all_answer_list[0][0]))
    print('满足最短递增序列的长度为{}的共有{}个'.format(all_answer_list[0][0],len(all_answer_list)))
    print(all_answer_list)

    print()

    all_answer_list1 = list(answer3.advanced_solution())
    print('advanced_solution()最短递增序列的长度:{}'.format(all_answer_list1[0][0]))
    print('满足最短递增序列的长度为{}的共有{}个'.format(all_answer_list1[0][0],len(all_answer_list1)))
    print(all_answer_list1)
