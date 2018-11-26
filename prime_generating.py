def divisors(number):
    return [int(i) for i in range(1,number+1) if (number%i == 0)]

def prime(number):
    count = 0
    for i in range(2,number//2):
        if number % i == 0:
           count = count + 1      
    return count
      
def prime_generator(number):
    divisors_list = []
    verifier = 0
    divisors_list = divisors(number)
    print( divisors_list)
    for i in range( 0, len(divisors(number)) ):
        if prime(divisors_list[i] + number//divisors_list[i]):
           verifier = 1
           break
        else:
           continue
    return verifier
 
def verification(number):
    total = 0
    for i in range(1,number+1):
        if prime_generator(i) == 0 :
           print(total)
           total = total + i
    return total

print(verification(5))
