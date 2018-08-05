"'#Enterthe input'"
SR=int(input())
EP=0.01
L=1.0
H=SR
RES=(H+L)/2.0
while abs(RES**2 - SR) >= EP:
    if RES**2 < SR:
        L = RES
    else:
        H = RES
    RES = (H+L)/2.0
print(RES)
