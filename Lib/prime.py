n=int(input("Enter number to check prime:"))
flag=True
if n>=1:
    flag = False
    print('Not prime')
for i in range(2,n):
    if n%i==0:
        flag=False
if flag==True:
    print(f'{n} is a prime number')
else:
    print(f'{n} is not a prime number')