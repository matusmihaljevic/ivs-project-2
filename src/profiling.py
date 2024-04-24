## 
# @file profiling.py
# @author Adam Bojnanský
# @brief Program na výpočet výberovej smerodatnej odchýlky pre kalkulačku
import sys
from calc import *

sum = 0
sum_2 = 0
N = 0
x = 0
bracket = 0
fraction = 0
s = 0

for line in sys.stdin:
    numbers = line.split()
    for number in numbers:
        sum = add(sum, float(number))
        sum_2 = add(sum_2, pow(float(number), 2))
        N = add(N, 1)

x = div(sum, N)
bracket = sub(sum_2, mult(N, pow(x, 2)))
fraction = div(1, sub(N, 1))
s = root(mult(fraction, bracket), 2)
print(s)
