#EXTRACTING DIGITS USING LOOP

n = int(input("Enter The Number : "))
num=n
while num > 0 :
    ld=num%10
    print(ld)
    num=num//10