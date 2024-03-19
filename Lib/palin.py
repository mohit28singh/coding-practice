n=int(input("Enter number to check palindrome:"))
copy=n
sum=0
while n>0:
    rem=n%10
    sum=sum*10+rem
    n=n//10
if sum==copy:
    print(f'{copy} is a palindrome number')
else:
    print(f'{copy} is not a palindrome number')


