# class Person:
#     pass

#     #class attributes
#     address = "no information"

#     #conscractor (yapıcı metod)

#     def __init__(self, name, year,city):

#         #object attributes
#         self.name = name
#         self.year = year
#         self.city = city

#     #instance methods
#     def intro(self): 
#         print("Hello There I'm " + self.name)

#     def calculateAGe(self):
#         return 2020 - self.year
        


    
# #object instance methods
# p1 = Person("Aytaç",2000,"Malatya")
# p1.intro()


# #updating
# p1.name = "Alex"
# p1.year = 1995
# p1.city = "New York"

# print(f"name: {p1.name} age: {p1.calculateAGe()} city: {p1.city}")

class Circle:
    #class object attribute
    pi = 3.14

    def __init__(self,yaricap=2):
        self.yaricap = yaricap

    #methods

    def cevre_hesaplama(self):
        return 2 * self.pi * self.yaricap

    def alan_hesaplama(self):
        return self.pi * (self.yaricap**2)

c1 = Circle() 
c2 = Circle(5)

print(f"Alan= {c2.alan_hesaplama()} Çevre= {c2.cevre_hesaplama()} ")