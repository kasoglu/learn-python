isim = input('Adınız : ')
yas = int(input('Yaşınız : '))


if yas >= 18 and yas < 65:

    egitim = input('Eğitim Durumunuz :')

    lower_egitim = egitim.lower()
  
    if lower_egitim == 'lise' or lower_egitim == 'üniversite':
        print("Ehliyet alma hakkınız bulunuyor")
    else:
        print("Ehliyet alabilmek için lise yada üniveriste mezunu olmanız gerekiyor.")
else:
    print("Ehliyet alabilmek için yaşınızın 18-65 arasında olması gerekiyor")
    