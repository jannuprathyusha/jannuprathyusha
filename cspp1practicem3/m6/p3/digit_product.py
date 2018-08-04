n = int(input())
product=1
temp=0
while n!=0:
     temp=n%10
     product=product*temp
     n=n//10
print(product)
    
    
