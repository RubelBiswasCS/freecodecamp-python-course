
result = 0.0
a = int(input("Enter First Numbet"))
b = int(input("Enter 2nd Numbet"))

try:
    print(a/b)
except ZeroDivisionError as Err:
    print(Err)