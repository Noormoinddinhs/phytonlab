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

# convertion from km to miles

km=int(input('enter distance in km'))
miles= 0.62137119 * km
print(str(km) + ' kms is equals to ' + str(miles))

# quadratic equation

a=int(input('enter the value of a:'))
b=int(input('enter the value of b:'))
c=int(input('enter the value of c:'))
d=(b*b)-(4*a*c)
sol1=(-b-(d)**0.5)/(2*a)
sol1=(-b+(d)**0.5)/(2*a)
print('the solution are ' + str(sol1),str(sol2))

# Given number is even or odd

n=int(input('enter the no'))
if (n%2==0):
    print('even no')
else:
        print('odd no')
