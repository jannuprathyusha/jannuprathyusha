"'#Taking the input'"
STRING = input()
COUNT = 0
LENGTH = int(len(STRING))
A = 0
B = 3
"'Checking the string'"
while B <= LENGTH:
    I = STRING[A:B]
    if I == "bob":
        COUNT = COUNT+1
    A = A+1
    B = B+1
print(COUNT)
