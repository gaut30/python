a = 10
b = 10
c = 10.0
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(a is c)

# Python program to illustrate the use of 'is' identity operator
x = 5
y = 5
print(x is y)
print(id(x))
print(id(y))

print(a is not c)
print(b is not c)
print(a is not b)

# Python program to illustrate the use of 'is not' identity operator

x = 5
if (type(x) is not int):
    print("true")
else:
    print("false")
