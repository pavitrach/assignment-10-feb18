n=int(input("enter n"))
count=0
for num in range (2,n+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break 
        else:
            print(num)
            count=count+1
print("total",count)
