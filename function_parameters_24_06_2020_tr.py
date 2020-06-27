# def printWord(word):
#     for i in range(hak):
#         print(word)

# print("Yazacağınız kelimeyi kaç kere tekrar edelim?")
# hak = int(input())
# word = input()
# print()
# printWord(word)

# def listeyeCevir(*params):
#     liste=[]

#     for param in params:
#         liste.append(param)

#     return liste

# result = listeyeCevir(10,20,30,"Merhaba")

# print(result)

# def findPrimeNumber(num1,num2):
#     for number in range(num1,num2+1):
#         if number > 1:
#             for i in range(2,number):
#                 if(number % i == 0):
#                     break
#             else:
#                 print(number)

# num1 = int(input("sayi 1:"))
# num2 = int(input("sayi 2:"))

# findPrimeNumber(num1,num2)

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2,sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenleriBul(20))