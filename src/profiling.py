## 
# @file profiling.py
# @author Adam Bojnanský
# @brief Profiling pre kalkulačku
import sys
from calc import *

sum = 0
sum_2 = 0
N = 0
x = 0
bracket = 0
fraction = 0
s = 0

if len(sys.argv) > 1:
    # Ak bol zadaný súbor ako argument príkazového riadku
    subor = sys.argv[1]
    with open(subor, 'r') as file:
        for riadok in file:
            cisla = riadok.split()
            # Vypíšeme každé číslo zo získaného zoznamu
            for cislo in cisla:
                sum = add(sum, float(cislo))
                sum_2 = add(sum_2, pow(float(cislo), 2))
                N += 1

    x = div(sum, N)
    bracket = sub(sum_2, mult(N, pow(x, 2)))
    fraction = div(1, sub(N, 1))
    s = root(mult(fraction, bracket), 2)
    print("sum: %d" % sum)
    print("sum_2: %d" % sum_2)
    print("N: %d" % N)
    print("x: %f" % x)
    print("bracket: %f" % bracket)
    print("fraction: %f" % fraction)
    print(s)


else:
    # Inak čítame zo štandardného vstupu
    for cislo in sys.stdin:
        # Spracovanie riadku zo štandardného vstupu
        print(cislo)
