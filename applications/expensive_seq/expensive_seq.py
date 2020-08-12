# Your code here

# create a dictionary
dic = {}
def expensive_seq(x, y, z):
    # Your code here

    # set the x, y and z as a key
    key = (x, y, z)

    # see if key is not in the dictionary
    if key not in dic:
        # and if x is less or equal to 0
        # then set the key to y + z
        if x <= 0:
            dic[key] = y + z
        # and if x is bigger than 0
        # then set the key to below
        if x > 0:
            dic[key] = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
    
    # return the key in the dectionary
    return dic[key]



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
