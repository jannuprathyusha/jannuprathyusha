string = input()
length = len(string)
for i in range (0,length+1):
    for letters in string:
        if string[i]== '!' or '@' or '#' or '%' or '^' or '&' or '*':
            string(i)=" "
print(string)        
        
        
    
