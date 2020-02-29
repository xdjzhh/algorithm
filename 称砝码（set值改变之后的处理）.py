import copy

number = int(input())
weight = list(map(int, input().strip().split()))
count = list(map(int, input().strip().split()))
weight_set = set([0,])
for i in range(number):
    d = weight_set.copy()
    for j in d:
        for k in range(1, count[i] + 1):
            current = j + weight[i] * k
            weight_set.add(current)
print(len(weight_set))
