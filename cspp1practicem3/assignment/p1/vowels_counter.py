"'#Taking the input'"
STRING = input()
COUNT = 0
"'#counting the vowels'"
for i in STRING:
    if i in 'aeiou':
        COUNT += 1
print(COUNT)
