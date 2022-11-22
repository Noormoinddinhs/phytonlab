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

# Given no is positive or negative or zero    
        
 n=int(input('enter a no'))
if (n<0):
    print('no is neg')
elif (n==0):
        print('no is zero')
else:
            print('number is  positive')       

# Given no is positive or negative or zero with use of nested if statement
        
n=int(input('enter a no'))
if (n<=0):
    if (n<0):
        print('no is neg')
elif(n==0):
    prin('no is zero')
else:
            print('number is  positive')        

# Greater of three no     

a=int(input('enter the value of a'))
b=int(input('enter the value of b'))
c=int(input('enter the value of c'))
if((a>b)and(a>c)):
    print('a is greater')
elif(b>c):
    print('b is greater')
else:
    print('c is greater')      

# print no 1 and 100    
    
for i in range(1,101):
    print(i)

# print mutipal of 4 and 7 between 100   
    
n=1
while (n<=100):
    if((n%4==0)and(n%7==0)):
        print(n)
    n=n+1    
