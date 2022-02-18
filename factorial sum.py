n=int(input("enter n:"))
sum=0
for i in range (1,n+1):
    fact=1
    for j in range (1,i+1):
        fact=fact*j
    print(fact)
    sum=sum+fact
print("sum=",sum)
