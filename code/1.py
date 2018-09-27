'''
#1.12
a,b,c=eval(raw_input('>>'))
if(a+b)>c:
	print('The perimeter is {}'.format(a+b+c))
else:
	print('write error')
'''

'''
#1.11
a=int(raw_input('>>'))
x=a/100%10
y=a%10
if (x==y):
	print('{} is a palidrome'.format(a))
else:
	print('{} is not a palidrome'.format(a))
'''
'''
#1.10


import random
list1=('A','2','3','4','5','6','7','8','9','10','J','Q','K')
list2=('meihua','hongtao','fangkuai','haitao')
x=random.sample(list1,1)
y=random.sample(list2,1)
str_x=str(x)
str_y=str(y)
print(str_x,str_y)
'''
'''
#1.8


import random
y=eval(raw_input('y>>'))
x=random.randint(0,3)
if (y==0):
	if x==1:
		print('ni ying le')
	elif x==2:
		print('ni shu le')
	else:
		print('zai lai yi ci')
elif(y==1):
	if(x==0):	
		print('ni ying le')
	elif (x==2):
		print('ni shu le')
	else:
		print('zai lai yi ci')
else:
	if (x==0):
		print('ni ying le')
	elif (x==1):
		print('ni shu le')
	else:
		print('zai lai yi ci')
'''
'''
#1.7
import random
y=eval(raw_input('y>>'))
if (y=randow.randint()):
	print('T')
else:
	print('F')
'''

'''
#1.6
m,y=eval(raw_input('m,y>>'))
if(y%400!=0):
	if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
		print('d=31')
	elif(m==2):
		print('d=28')
	else:
		print('d=30')
else:
	if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
                print('d=31')
	elif(m==2):
                print('d=29')
        else:
                print('d=30')

'''	




'''
#1.5
a,b=eval(raw_input('a,b>>'))
c,d=eval(raw_input('c,d>>'))
if(a/b>c/d):
	print('1')
else:
	print('2')

'''

'''
#i.4

a,b,c=eval(raw_input('a,b,c>>'))
if (a>c and b>c):
	if(a>b):
		if (b>c):
			print(a,b,c)
		else:
			print(a,c,b)
	else:
		if (a>c):
			print(b,a,c)	
		else:
			print(b,c,a)

	
else:
	if(a>b):
		print(c,a,b)
	else:
		print(c,b,a)
'''

'''
#1.3
a,b=eval(raw_input('a,b>>'))
for i in range (0,7):
	if (a==i):
		c=(b-7+a)%7
		print('today is {} and future is {}'.format(i,c))
		break
	else:
		print('write error')

'''


'''
#1.2
import random
x=random.randint(0,100)
y=random.randint(0,100)
w=x+y
for i in range (10):
	a=eval(raw_input('a>>'))
	if(a>w or a< w):
		print('Float')
	else:
		print('True')


'''


'''
#1.1
import math
a=eval(raw_input('a>>'))
b=eval(raw_input('b>>'))
c=eval(raw_input('c>>'))
if (b**2-4*a*c>0):
	r1=(-b+math.sqrt(b**2-4*a*c))/2*a
	r2=(-b-math.sqrt(b**2-4*a*c))/2*a
	print('The roots are {} and {}'.format(r1,r2))
elif (b**2-4*a*c==0):
	r=-b/2*a
	print('The roots are {}'.format(r))
else:
	print('The equation has no real roots')
'''


'''


#7
a=raw_input('>>')
if int(a)<0:
	a=a[1:]
	b=-int(a[::-1])
else:
	b=int(a[::-1])

print(b)

'''
'''
#1
import math
r=eval(raw_input('Enter the length from the center to a vertex:'))
s=2*r*math.sin(math.pi/5.0)
Area=round(5*s**2/(4*math.tan(math.pi/5.0)))
print(Area)
'''
'''


#2
import math
x1,y1=eval(raw_input('Enter point 1 in degrees>>'))
x2,y2=eval(raw_input('Enter point 2 in degrees>>'))
radius=6371.01
a=math.sin(math.radians(x1))
b=math.sin(math.radians(x2))
c=math.cos(math.radians(x1))
d=math.cos(math.radians(x2))
e=math.cos(math.radians(y1)-math.radians(y2))

h=radius *math.acos(a*b+c*d*e)
print(h)

'''
'''

#3
import math
s=eval(raw_input('>>'))
Area=(5*s**2)/(4*math.tan(math.pi/5.0))
print(Area)
'''
'''



#4
import math
n=eval(raw_input('>>'))
s=eval(raw_input('>>'))
Area=(n*s**2)/(4*math.tan(math.pi/n))
print(Area)
'''
'''

#5


n=eval(raw_input('>>'))
print(chr(n))
'''
'''
#6


name=raw_input('name>>')
time=eval(raw_input('time>>'))
meony=eval(raw_input('meony>>'))
lyk=eval(raw_input('lyk>>'))
zyk=eval(raw_input('zyk>>'))
meonys=meony*10
lyk1=meonys*lyk
zyk1=meonys*zyk
total=zyk1+lyk1
print('name:{}'.format(name))
print('time:{}'.format(time))
print('meony:${}'.format(meony))
print('meonys:${}'.format(meonys))
print('DEductions:')

print('  lyk1:{}'.format(lyk1))
print('  zyk1:{}'.format(zyk1))
print('  lyk1+zyk1:{}'.format(total))

'''






















