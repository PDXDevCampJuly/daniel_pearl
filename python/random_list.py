from random import randint
from random import randrange
from time import time

rand_lst = []

for i in range(10):
    rand_int = [randint(0,100)]
    rand_lst.append(rand_int)

def check_list(num, list):
    if num in list:
        return true

#print(rand_lst)

start = time()
print(time() - start)
 
