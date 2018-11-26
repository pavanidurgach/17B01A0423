211
def sum_of_squares_of_divisors_in_range(number):
    temp = 2
    total = 1
    while temp < number:
          total = total + sum_of_squares_of_divisors(temp)
          temp = temp + 1     
    return total

def sum_of_squares_of_divisors(number):
    divisors = list_of_divisors(number)
    sum = 1
    i = 0
    while i < len(divisors):
          sum = sum + divisors[i]**2
          i = i + 1
    return sum 

def list_of_divisors(number):
    return [x for x in range(2,number+1) if number%x==0]

print(sum_of_squares_of_divisors_in_range(64000000))
