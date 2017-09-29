# sums up every multiple of 3 or 5
def multiple_of(n):
    sum = 0

    for i in range(n):

        if i % 3 == 0 or i % 5 == 0:
            sum+= i

    return sum


thousand = multiple_of(1000)

print(thousand)