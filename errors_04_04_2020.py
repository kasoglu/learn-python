x = 42
y = 0

try: 
    print(x/y)
except ZeroDivisionError as e:
    print('Not allowed to divided by zero')
else:
    print('Something went wrong')
finally:
    print('This is our cleanup code')