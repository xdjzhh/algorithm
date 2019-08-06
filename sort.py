a = [(1, 2), (3, 4), (2, 1), (7, 4), (5, 3), (6, 1), (2, 5)]
a.sort(key=lambda x: x[1])
print(a)

new = sorted(a,key=lambda x:x[0],reverse=True)
print(new)