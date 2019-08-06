

#传统的Fibonacci算法  时间负责度O(2**n)

def original_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return original_fibonacci(n-1) + original_fibonacci(n-2)

def dynamic_fibonacci(n):
    fib_list = [None for i in range(n+1)]
    fib_list[0] = 0
    if n == 0:
        return fib_list[0]
    fib_list[1] = 1
    if n == 1:
        return fib_list[1]
    for index in range(2,n+1):
        fib_list[index] = fib_list[index-1] + fib_list[index-2]
    print(fib_list)
    return fib_list[n]

#还可优化为赋值类记忆

def advance(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f1 = 0
    f2 = 1
    for i in range(2,n+1):
        f1,f2 = f2,f1 + f2
    return f2



if __name__ == '__main__':
    result1 = original_fibonacci(10)
    print(f'original_fibonacci result: {result1}')
    result2 = dynamic_fibonacci(10)
    print(f'dynamic_fibonacci result: {result2}')
    print(advance(10))