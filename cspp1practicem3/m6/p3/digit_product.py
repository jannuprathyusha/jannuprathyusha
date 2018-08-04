N = int(input())
PRODUCT = 1
TEMP = 0
while N != 0:
    TEMP = N%10
    PRODUCT = PRODUCT*TEMP
    N = N//10
print(PRODUCT)
    
    
