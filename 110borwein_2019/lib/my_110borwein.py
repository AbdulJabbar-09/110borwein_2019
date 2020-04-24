#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## borwein
## File description:
## borwein
##

import sys
import math

a, b, N = 0, 5000, 10000
h = (b - a) / N

def ime(x):
    cnt = 1
    k = 0
    n = float(sys.argv[1])
    while (k <= n):
        if (x != 0):
            cnt *= math.sin(x / (2 * k + 1)) / (x / (2 * k + 1))
        k += 1
    return (cnt)

def my_midpoint(n):
    res = 0
    for i in range (10000):
        res += ime(a + h/2.0 + (i * h))
    res *= h
    p = (math.pi / 2.0) - res
    print ("I{:.0f} = {:.10f}".format(n, res))
    if (str("%.10f" % p) == "-0.0000000000"):
        print(str("diff = " + "%.10f" % -p))
    else:
        print(str("diff = " + "%.10f" % p))

def my_trapezoidal(n):
    res = 0
    for i in range (1, 10000):
        res += ime((i * h))
    res = ((res * 2) + ime(a) + ime(b))
    calc = res * h / 2
    p = (math.pi / 2.0) - calc
    print ("I{:.0f} = {:.10f}".format(n, calc))
    if (str("%.10f" % p) == "-0.0000000000"):
        print(str("diff = " + "%.10f" % -p))
    else:
        print(str("diff = " + "%.10f" % p))

def my_simpson(n):
    res = (ime(a) + ime(b)) / 2 + 2 * ime(a + h / 2)
    x = a + h
    for i in range(1, N):
        res += ime(x) + 2 * ime(x + h / 2)
        x += h
    c_1 = (res * h) / 3
    c_2 = (math.pi / 2.0) - c_1
    print ("I{:.0f} = {:.10f}".format(n, c_1))
    if (str("%.10f" % c_2) == "-0.0000000000"):
        print(str("diff = " + "%.10f" % -c_2))
    else:
        print ("diff = {:.10f}".format(c_2))

if not len(sys.argv) == 2: exit(84)
try: arg = int(sys.argv[1])
except ValueError: exit(84)

if (arg < 0): exit(84)
print ('Midpoint:')
my_midpoint(arg)
print ('\nTrapezoidal:')
my_trapezoidal(arg)
print ('\nSimpson:')
my_simpson(arg)
exit (0)
