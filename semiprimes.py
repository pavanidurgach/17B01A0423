def prime(number):
    count = 0
    for i in range(2,number//2):
        if number % i == 0:
           count = count + 1      
    return count
      
def is_prime(number):
    if prime(number)
