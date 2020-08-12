# Your code here
import math, random



def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

# create a dictionary
slowfun_dic = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here

    # set x and y as the keys
    key = (x, y)

    # see if key is not in the dictionary
    # then set the keys in slowfun_too_slow method to
    # the new dictionary key
    if key not in slowfun_dic:
        slowfun_dic[key] = slowfun_too_slow(x, y)
    
    # and return the new dictionary key
    return slowfun_dic[key]



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    # print(f'{i}: {x},{y}: {slowfun_too_slow(x, y)}')
    print(f'Range # {i}: {x}, to the power of {y}: {slowfun(x, y)}')
