class question2:
    def __init__(self):
        pass


    '''根据日期（想要知道的某日期到某日期的销售利润）从数据库中拉出数据
    将数据库column扩展为id,price,quatity,signal  'signal'标签用1，2
    区分是卖出还是买入,id视为日期
    
    '''
    def get_content(self,id1,id2):

        '''
        db = pymysql.connect(...)
        cursor = db.cursor()

        生成选定日期区间的买卖列表，排列顺序为先排日期后排买卖：
        sql = 'select * from sales_record where id >{} and id<{} union select * from purchase_record where id >{} and id<{}
        order by id，signal value (id1,id2,id1,id2)'

        将提取的数据转换为数组惊醒操作：
        :return: np.asarray(execute(sql))

        '''

        pass


    '''此函数对买卖进行操作，对sales_record和purchase_record进行动态操作，若为卖，入队列temp_deque，若为买，入队列purchase_deque
    每次遇到买操作时对每个浸入temp_deque队列的元素进行操作，若出现超卖purchase_deque队列里元素减少数量不用leftpop，当且仅当purchase_deque队列
    里index=0的元素里的数量 为0时 leftpop （当purchase——deque[0][2]  quantity == 0 时）
    '''

    def caculate(self):

        '''
            #运用deque库进行先进先出的操作

        deque = self.get_content(id1,id2)

            #从头开始遍历 若表示列deque[i][-1]为1（表示为买）则将元素加入新的temp_deque，若表示变为2（表示为卖）

        temp_deque = deque()
        purchase_deque = deque()
        for i in range(len(deque)):
            if deque[i][-1] == 1:
                temp_deque.append(deque[i])


            else:
                purchase_deque.append(deque[i])
                for k in range(len(purchase_deque)):


                        #先入先出进行判断数量的大小,若买的大那么将当前temp_deque[j][1]元素的数量大，改变当前数量值变为temp_deque[j][2]-purchase_deque[k][2]

                    purchase_deque[k][2] = 0

                        #初始化每次计算的盈利

                    benifit = 0
                    for j in range(len(temp_deque)):
                        if temp_deque[j][2] >purchase_deque[k][2]:
                            temp_deque[j][2] = temp_deque[j][2] - deqpurchase_dequeue[i][2]
                            purchase_deque[k][2] = 0

                            print('当前盈利{时间purchase_deque[i]}benefit = （temp_deque[j][2] - purchase_deque[k][2]）*（purchase_deque[k][2]-temp_deque[j][2]）')
                        else:


                                #若买的大那么将当前temp_deque[j][1]元素的数量小，leftpop(),当前purchase_deque中的卖出数量变为purchase_deque[k][2]-temp_deque[j][2]
                                #并记录每次计算的盈利 benifit

                            temp_deque.leftpop()
                            purchase_deque[k][2] = purchase_deque[k][2]-temp_deque[j][2]
                            benefit += temp_deque[j][2]*（purchase_deque[i][1]-temp_deque[j][2]）'
                            if purchase_deque[k][2] == 0:
                                purchase_deque.leftpop()
                                print('当前盈利benefit')
    
                    #经过循环后如果出现超卖，此时temp_deque必定为空,purchase_deque必定不为空，deque元素继续后移直至下个卖点




        :return:
        '''
        pass




if __name__ == '__main__':
    pass