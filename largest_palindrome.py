
result = []

for i in range(100,1000):
    for j in range(100,1000):

        summ = i*j
        summ = str(summ)
        summreversed = summ[::-1]
        if summ == summreversed and summ not in result:
            summ = int(summ)
            result.append((summ))




result.sort()
print(result)