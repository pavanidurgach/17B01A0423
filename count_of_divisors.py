def divisors(number):
    return [int(i) for i in range(1,number+1) if (number%i == 0)]

def count_of_divisors(limit):
    count = 0 
    for i in range(1,limit+1):
        if len(divisors(i)) == 8:
           count = count + 1
    return count

print(count_of_divisors(100))
