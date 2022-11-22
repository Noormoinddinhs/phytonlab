# additon of two number

a=int(input('enter the 1st value'))
b=int(input('enter the 2nd value'))
c=a+b
print(c)

# square root of a number

a=int(input('enter a number'))
b=a**0.5
print(b)

# area of a triangle

b=int(input('input base'))
h=int(input('input height'))
area = 1/2 * b * h
print(area)

# swape of a two number with using temporary variable

a=int(input('1st number'))
b=int(input('2nd number'))
temp=a
a=b
b=temp
print('a=' +str(a))
print('b=' +str(b))

# swape of a two number without using temporary variable

x = int(input('enter the value of x'))
y = int(input('enter the value of y'))
x, y = y, x
print("Value of x : ", x, " and y : ", y)

# addition subration multiplication divistion and exor of two number

a=int(input('1st number'))
b=int(input('2nd number'))
c=a+b
d=a-b
e=a*b
f=a/b
g=a^b
print(c)
print(d)
print(e)
print(f)
print(g)
