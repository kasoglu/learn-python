q=1

dizi=[]

while True:

    try:

        a=int(input(f'{q}. kenari giriniz: '))

        if a<0:

            print("Lütfen pozitif sayi girin")

            continue

        dizi.append(a)

        q=q+1

        if len(dizi)==3:

            break

    except Exception:

        print("Lütfen bir sayi girin")

x=dizi[0]

y=dizi[1]

z=dizi[2]

if (abs(x+y)>z and abs(x+z)>y and abs(y+z)>x):

    if (x==y and x==z and y==z):

        print("Bu bir eskenar ucgendir.")

    elif (x==y or x==z or y==z):

        print("Bu bir ikizkenar ucgendir.")

    else:

        print("Bu bir cesitkenar ucgendir.")

else:

    print("Ucgen olma kosullarını saglamıyor!")
