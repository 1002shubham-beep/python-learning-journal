# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary  

def net_price(price,discount=0,tax=0.05):
    return price * (1-discount) * (1+tax)

# print(net_price(500,0.1,0.01))
# print(net_price(200))

import time

def count(end,start = 0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1) # sleeps for 1 second
    print("Time's Up!")


count(10)