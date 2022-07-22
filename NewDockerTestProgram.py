# New Docker test program

# Interactive

from math import *

str_input = str(input())
counter = 0
str_length = len(str_input)

while str_input != 'END' and counter < 100:
     if 'END' in str_input:
        print('The end! Bye!')
        break
     else:
        counter += 1
        sum_quad = pow(counter, 3)
        print("Let's proceed!", counter, sum_quad, str_length)

