def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_name = input("Enter a your name : ")
first_name_initial = get_initial(first_name, True)
print(first_name_initial)