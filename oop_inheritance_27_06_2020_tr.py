#Inheritance (Kalıtım): Miras alma

class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print("Person Created")
    
    def who_ami(self):
        print("I am a person!")
    
    def eat(self):
        pass

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.StudentNumber = number
        print("Student Created")

    #override
    def who_ami(self):
        print("I am a student!")

class Teacher(Person):
    def __init__(self,fname, lname,branch):
        Person.__init__(self, fname,lname)
        self.branch = branch
        print("Teacher Created.")
    
    def who_ami(self):
        print("I am a Teacher!")


p1 = Person("Richard","Hendriks")
p2 = Student("Bill","Gates","778523")
p3 = Teacher("Elon","Musk","Mathematics")

print(p1.fname + " " + p1.lname) 
print(p2.fname + " " + p2.lname + " " + p2.StudentNumber)
print(p3.fname + " " + p3.lname + " " + p3.branch)

p1.who_ami()
p2.who_ami()