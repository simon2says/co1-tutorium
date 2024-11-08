def max_of_two(a,b):
    if (a > b):
        return a
    return b

def max_of_three(a,b,c):
    if(a > b):
        if(a > c):
            return a
        return c
    if(b > c):
        return b
    return c