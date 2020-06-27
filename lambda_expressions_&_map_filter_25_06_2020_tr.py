def square(num):
    return num ** 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8,9,10]

result = list(map(square, numbers))

for item in map(square, numbers):
    print(item)

print(result)

# def check_even(num): return num % 2 ==0
check_even = lambda num: num%2==0

result = list(filter(check_even, numbers))

print(result)