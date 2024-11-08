def sum_even(n):
    sum = 0
    for i in range(1,n+1):
        sum += (i*2)
    return sum

def sum_even_list(n):
    evenlist = []
    sum = 0
    for i in range(1,n+1):
        evenlist.append(i)
    evenlist = list(map(lambda x: x*2, evenlist))
    for i in range(0,len(evenlist)):
        sum += evenlist[i]
    return sum

print(sum_even_list(10))