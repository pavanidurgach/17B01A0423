def simber(number):
    even_count = 0
    odd_count = 0
    while number > 0:
          if number % 2 == 0:
             even_count = even_count + 1
          else:
             odd_count = odd_count + 1
          number = number//10
    return odd_count % 2 != 0 and even_count % 2 == 0

def sum_of_simbers(limit):
    sum = 0
    for i in range(1,limit+1):
        if simber(i):
           sum = sum + i
    return simber

print(sum_of_simbers(7))
