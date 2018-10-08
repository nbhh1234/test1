
#7
for i in range ()


'''
#6
def computeNum(rate, loanAmount, numYears):
    totalPayment = loanAmount * ((1+rate)**numYears)
    return totalPayment

loanAmount = eval(input('输入贷款总额：'))
numYears =  eval(input('输入贷款周期（年）：'))
for i in range(0, 25):
    rate = 0.05 + i*0.00125
    totalPay = computeNum(rate, loanAmount, numYears)
    print('利率为%f的月还款额为%f，总还款额为%f' %(rate, totalPay/60, totalPay))
'''
'''
#5
'''
逻辑思想:
-------
 寻找n**3 一定会先比n**2找到n值
 找到了之后，我们就不打印n**3找到的n值
 使用count关闭打印n值，再继续去寻找n**2的n值
'''

n = 0.0
count = True
while 1:
    n = n + 1.0
    if n * n * n > 12000:
        if count:
            print('n**3', n - 1)
            count = False

    # print('hahah')
    if n * n >= 12000:
        print(n * n)
        print('n**2', n)
        break

	

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
