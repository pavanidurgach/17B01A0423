def list_formation(number):
    return [int(i) for i in range(1,number+1)]

def left_elimination(list):
    i = 0
    while i < len(list):
          list.remove(list[i])
          i = i + 1
    return list

def final_elimination(limit):
    sum = 0
    number = 1
    while number < (limit+1):
          list = list_formation(number)
          while len(list) >= 1:
                if len(list) == 1:
                   sum = sum + list[0]
                   break
                left_elimination(list)
                list[0:] = list[::-1]
          number = number + 1
    return sum

print(final_elimination(10**18)%987651)
