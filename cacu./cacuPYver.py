#!/usr/bin/python3

import os
import time

os.system('clear')
os.system('figlet "CACUpyVer"')

print("")

x = input("(enter first number)> ")
print ("")
eqs = input("(enter equation sign)> ")
print ("")
y = input("(enter second number)> ")

y = int(y)
x = int(x)

if eqs == "x" :
    print (x, "x", y, "=", int(x * y))
elif eqs == "*" :
    print (x, "x", y, "=", int(x * y))
elif eqs == "**" :
    print (x, "**", y, "=", int(x ** y))
elif eqs == "/" :
    print (x, "/", y, "=", int(x / y))
elif eqs == "%" :
    print (x, "%", y, "=", int(x % y))
elif eqs == "+" :
    print (x, "+", y, "=", int(x + y))
elif eqs == "-" :
    print (x, "-", y, "=", int(x - y))
else :
    print("error")
