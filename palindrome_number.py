#CHECKS IF A NUMBER IS A PALINDROME:

n = int(input("Enter The Number : "))
num=n
result=0
while num>0:
    ld=num%10
    result=(result*10)+ld
    num=num//10
if(n==result):
    print("It is a Palindrome number")
else :
    print("It is Not a Palindrome number")