
def solution(B,A,n):
    if B < A:
        return -1
    if B == A:
        return n

    if B%2 == 0:
        return solution(B//2,A,n+1)
    elif (B-1)%10 == 0:

        return solution((B-1)//10,A,n+1)
    else:
        return -1

if __name__ == '__main__':
    number = int(input())
    ablist = []
    for i in range(number):
        each = list(map(int,input().split(' ')))
        ablist.append(each)
        # print(solution(each[1],each[0],0))
    for each in ablist:
        print(solution(each[1], each[0], 0))
