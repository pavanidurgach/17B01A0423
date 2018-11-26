def factorial(number):
    factorial = 1
    while number > 0:
          factorial = factorial * number
          number = number - 1
    return factorial

def prime(number):
    count = 0
    for i in range(2,number//2):
        if number % i == 0:
           count = count + 1      
    return count

def sum_of_factorial(start,limit):
    total = 0
    for k in range(start,limit):
        if prime(k) == 0:
           sum = 0
           for i in range(1,6):
               sum = sum + factorial(k-i)
           total = total + sum % k
    return total

print(sum_of_factorial(5,1000))
