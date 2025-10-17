# COUNTING NUMBER OF DIGIT IN AN INTEGER

n=int(input("Enter the number : "))
num=n
count=0
while num>0:
    count=count+1
    num=num//10
print("Number Of Digit : ",count)
