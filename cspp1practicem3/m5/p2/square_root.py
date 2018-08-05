"'enter the input'"
SR=int(input())
EP=0.01
I=0.0
INCREMENT=0.1
while abs(I**2 - SR) >= EP:
    I += INCREMENT
    
if abs(I**2 - SR) >= EP:
    print('failed')
else:
    print(I)
        
