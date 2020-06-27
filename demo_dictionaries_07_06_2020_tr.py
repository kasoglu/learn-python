ogrenciler = {

    "190509026": {
        "ad":"Aytaç",
        "soyad":"Kaşoğlu",
        "telefon":"5442903647"
    },

    "190509010": {
        "ad":"Mehmet Kadir",
        "soyad":"Cırık",
        "telefon":"5387984501"
    },

    "190543014": {
        "ad":"Safa",
        "soyad":"Çubuk",
        "telefon":"5442516479"
    }
}

ogrenciler = {}

number = input("Öğrenci No: ")
first_name = input("Öğrenci adı: ")
last_name = input("Öğrenci soy adı: ")
phone_number = input("Telefon: ")


ogrenciler[number] = {
    "ad": first_name,
    "soyad": last_name,
    "telefon": phone_number
}

ogrenciler.update({
    number:{
        "ad": first_name,
        "soyad": last_name,
        "telefon": phone_number
    }
})

print(ogrenciler)

ogrNo = input("NO giriniz: ")
ogrenci = ogrenciler[number]
 
print(ogrenci)