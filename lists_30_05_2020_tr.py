carName = ["Opel","mazda", "mercedes","bmw","honda"]

# print(carName[:3])
# print(len(carName)) # Liste uzunluğunu gösterir.

# carName[1] = ["Toyota"]
# carName.remove("honda")
# result = "Opel" in carName
# print(result)

# studentA = ["Ali","Ersoy",2000,[50,40,70]]
# studentB = ["Beril","Asyalı",2001,[90,80,70]]
# studentC = ["Melisa","Durak",2003,[80,100,90]]

carName.append("audi")
carName.insert(0, "hundai")
carName.sort()
carName.reverse()
print(carName)