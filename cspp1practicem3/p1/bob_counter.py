"'#Taking the input'"
STRING = input()
COUNT = 0
LENGTH = int(len(STRING))
a = 0
b = 3
"'Checking the string'"
while b <= LENGTH:
    I = STRING[a:b]
    if I == "bob":
        COUNT = COUNT+1
    a = a+1
    b = b+1
print(COUNT)
    
        
                

