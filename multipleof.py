# sums up every multiple of 3 and 5
def multiple_of(n):
    sum = 0

    for i in range(n):

        if i % 3 == 0 and i % 5 == 0:
            sum+= i

    return sum


thousand = multiple_of(1001)

print(thousand)