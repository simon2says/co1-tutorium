def ggt(a, b):
    while (b != 0):
        if(a > b):
            a = a - b
        else:
            b = b - a
    return a

a = int(input("Bitte erste Zahl eingeben: "))
b = int(input("Bitte zweite Zahl eingeben: "))
print(ggt(a,b))
