sayi = int(input("Herhangi bir sayi giriniz:"))
 
toplam=0
 
for i in range(1,sayi):
    if(sayi%i == 0):
        toplam +=i
        
if(sayi == toplam):
    print(sayi,"Mükemmel Sayidir.")
else:
    print(sayi,"Mükemmel Sayi Degildir")