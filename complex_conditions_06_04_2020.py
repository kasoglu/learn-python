# A student makes honour roll if their average is >=85
# and their lowest grade is not below 75

gpa = float(input("What is your Grade Point Average? "))
lowest_grade = float(input("What was your lowest grade? "))

#if gpa >= 85:
#   if lowest_grade >= 75:
#        print("You made honour roll")

if gpa >= 85 and lowest_grade >= 75:
        honour_roll = True
else: 
            honour_roll = False

print(honour_roll)