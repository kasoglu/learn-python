# x = 0

# while x <= 100:
#     if x %2 == 0:
#       print(x)
#       x += 2
# print("bitti....")    

# sayilar = [1,3,5,7,9,12,19,21]

# result = sayilar.list()
# while result < 22:
#     if result % 2 == 1:
#         print(result)


urunler = []

adet = int(input('kaç ürün eklemek istiyorsunuz: '))

i = 0 

while i < adet:

   name = input('Ürün ismi: ')
   price = input('ürün fiyatı: ')
   urunler.append({
    "name": name,
    "price": price
   })
   i += 1

for urun in urunler:
    print(f'ürün adı:{urun["name"]} | ürün fiyatı: {urun["price"]}')

