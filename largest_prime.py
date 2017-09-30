import math

# finds largest prime factor
def largest_prime(n):
    print(n)
    sum = 1
    original = n
    n = round(math.sqrt(n)) + 10
    print(n)
    print ("------------------")



    for i in (range(2,n+1)):
        if original % i == 0:
            sum*=i
            print(i)

    print(sum)





largest_prime(600851475143)
