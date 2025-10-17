# PRINT FACTORS OF THE NUMBER

n=int(input("Enter The Number : "))
num=n
a = 1
while num>0:
    if(num%a==0):
        print(a)
    a=a+1
