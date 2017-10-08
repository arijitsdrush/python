#!/usr/bin/python3

a, b = 0, 10

while a < b:
    print(a)
    a = a + 1
    print('Done') #Here this line also is a part of While loop

    
for i in range(1,10):
    print(i)

#Example of iterating through array    
bridgera = ['Arijit','Soumya','Gunjan','Arptia','Bishwa','Rintu','Satya','Lelin']
for i in range(len(bridgera)):
    print(i,bridgera[i])