class Person:
    pass

    #attributes

    #conscractor (yapıcı metod)

    def __init__(self, name, year,city):
        self.name = name
        self.year = year
        self.city = city


    #object attributes

    #methods

    
#object instance methods
p1 = Person("Aytaç",2000,"Malatya")



#updating
p1.name = "Alex"
p1.year = 1995
p1.city = "New York"

print(f"name: {p1.name} year: {p1.year} city: {p1.city}")