#EXTRACTION OF DIGIT USING 

n = int(input("Enter The Number : "))
while n > 0 :
    last_digit=n%10
    print(last_digit)
    n=n//10