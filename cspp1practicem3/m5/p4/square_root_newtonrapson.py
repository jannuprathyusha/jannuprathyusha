"'Enter the input'"
E = 0.01
B = int(input())
A = B/2.0
while abs(A*A - B) >= E:
    A = A - (((A**2)-B)/(2*A))
print(A)