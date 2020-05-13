num1 = int(input('sayı 1:'))
num2 = int(input('sayı 2:'))
def findA(num1, num2):
    for sayi in range(num1, num2+1):
        if sayi > 1:
            for i in range(2,sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)
findA(num1,num2)