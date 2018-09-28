
#7
for i in range ()


'''
#6
x,y=eval(input('>>'))
z=0
for i in range (0,100):
	l=0.05*(1+0.125)**i
	z=(x*(1+l))**y
	print(z)
	if(l>0.08):
		break
'''
'''
#5
a=0
for i in range (1,1000):
	while(i**2>12000):
		a=i
		continue
print(a)

	

'''
'''
#4
j=0
for i in range (100,1001):
	if(i%5==0 and i%6==0):
		print(i,end=' ')
		j+=1
		if(j==10):
			print(end='\n')
			j=0
'''		
'''
#2
a=eval(raw_input('>>'))
b=a*(1+0.05)**10
sum_=0
for i in range (10,14):
	sum_=sum_+ a*(1+0.05)**i
	i+=1
print(b,sum_)

'''

'''
#1
a=eval(raw_input('>>'))
i=0
j=0
sum1=0
sum2=0
while(a!=0):

	if(a>0):
		sum1=sum1+a
		i+=1
		a=eval(raw_input('>>'))
	else:
		sum2=sum2+a
		j+=1
		a=eval(raw_input('>>'))

	continue
float_i=float(i)
float_j=float(j)
print(sum1/float_i)
print(sum2/float_j)
'''
