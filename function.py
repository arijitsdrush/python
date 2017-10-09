#!/usr/bin/python3

def fahrenheit(T_in_celsius):
    """ returns the temperature in degrees Fahrenheit """
    return (T_in_celsius * 9 / 5) + 32

for t in (22.6, 25.8, 27.3, 29.8):
    print(t, ": ", fahrenheit(t))
    
    
def even_odd(n):
    
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

for i in range(1,10):
    print(even_odd(i))