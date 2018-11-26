def divisibility(number): 
    total = 0
    for x in range(2,number+1):  
        for i in range(2,x+1):
            if factorial(i) % x == 0:
               total = total + i 
               break
    return total

def factorial(number):
    factorial = 1
    while number > 0:
          factorial = factorial * number
          number = number - 1
    return factorial

print(divisibility(1000))
