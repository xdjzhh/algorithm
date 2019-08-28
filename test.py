




def solution(special_node,sequence,distance):
    node_set = []
    for index in range(len(sequence)):
        if sequence[index] in special_node:
            if index >= distance:
                node_set = node_set + sequence[index-distance:index-1] + sequence[index+1:index+distance+1]
            else:
                node_set = node_set + sequence[0:index - 1] + sequence[index + 1:index + distance + 1]
    number = len(set(node_set))
    return number

if __name__ == '__main__':
    string1 = input().split(' ')
    node_number = int(string1[0])
    special =  int(string1[1])
    distance = int(string1[2])

    special_node = input().split(' ')
    sequence = input().split(' ')

    print(solution(special_node,sequence,distance))