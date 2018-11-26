def reverse(number):
    return [int(i) for i in str(number)] 

def binary_number(number):
    binary = []
    while number > 0:
          binary.append(number % 2)
          number = number // 2
    return binary

def palindrome(binary): 
    return binary[0:] == binary[::-1]
 
def sum_of_numbers(range1):
    sum = 0
    for number in range(0,range1):
        if palindrome(reverse(number)):
           if palindrome(binary_number(number)):
              sum += number 
    return sum

print(sum_of_numbers(1000))
