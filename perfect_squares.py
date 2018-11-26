import math
def perfect_square(number): 
    if int(math.sqrt(number)) == math.sqrt(number) :
       return True
    else:
       return False

x = 0
y = 0
z = 0
def perfect_square_collection(num):
    while x < num:
          while y < x:
                while z < y:
                      if perfect_square(x+y) and perfect_square(x-y) and perfect_square(x+z) and perfect_square(x-z) and perfect_square(y+z) and perfect_square(y-z):
                         return x+y+z

print(perfect_square_collection(100))
