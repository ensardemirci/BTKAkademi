def findA(num):
    a = 2
    b=[]
    while a<num:
        if num % a == 0:
            b.append(a)
        a += 1
    return b
print(findA(20))