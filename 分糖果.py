

#  回溯法

def candy(score_list):
    final_list = [1 for i in range(len(score_list))]
    i = 1
    while i < len(score_list):
        if score_list[i-1] < score_list[i]:
            final_list[i] = final_list[i-1] + 1
        if score_list[i - 1] == score_list[i]:
            final_list[i] = final_list[i - 1]
        i+=1
    i = len(score_list) - 2
    print(final_list)
    while i >= 0:
        if (score_list[i] > score_list[i+1]) & (final_list[i] <= final_list[i+1]):
            final_list[i] = final_list[i+1] + 1
        if (score_list[i] == score_list[i+1]) & (final_list[i] <= final_list[i+1]):
            final_list[i] = final_list[i+1]

        i -= 1

    print(final_list)

    pass


if __name__ == '__main__':
    score_list = [1,2,4,2,3,1]
    candy(score_list)