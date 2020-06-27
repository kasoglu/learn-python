# asal sayi olup olmadigini bulan program

sayi = int(input("Bir sayi giriniz:"))

# 1'den buyuk olup olmadigini kontrol etme
if sayi > 1:
   
   for i in range(2,sayi):
       if (sayi % i) == 0:
           print(sayi,"asal sayi degildir.")
           print(i, " x ", sayi//i, " = " , sayi)
           break
   else:
       print(sayi,"asal sayidir.")
       
#Eger girilen sayi 1 yada 1'den kucukse
else:
   print(sayi,"asal sayi degildir.")