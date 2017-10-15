#!/usr/bin/python3
        
bridgera = ['Arijit','Soumya','Gunjan','Arptia','Bishwa','Rintu','Satya','Lelin']

# Generator Function iterarates through all items of array
def gen_func(data):
    for i in range(len(data)):
        yield data[i]
    

data_gen = list(gen_func(bridgera))
print (data_gen) 

# Normal Function iterates through only first item of array
def norm_func(data):
    for i in range(len(data)):
        return data[i]

norm_gen = list(norm_func(bridgera))
print (norm_gen) 