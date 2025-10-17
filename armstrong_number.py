#CHECKS IF A NUMBER IS A ARMSTRONG

n = int(input("Enter The Number :"))
num=n
nod=len(str(num))
result=0
while num>0:
    ld=num%10
    result=result+(ld**nod)
    num=num//10
if(result==n):
    print("It is a Armstrong Number :")
else :
    print("It is not a Armstrong Number")