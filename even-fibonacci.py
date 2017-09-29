dict = {}
def fib(n):
    if n < 2:
        return 1

    else:
        if n in dict:
            return dict[n]
        else:
            result = fib(n-1) + fib(n-2)
            dict[n] = result
            return result


sum = 0
for i in range(1,100):
    result = fib(i)

    if result<4000000 and result % 2  == 0:

        sum+= result

print(sum)


