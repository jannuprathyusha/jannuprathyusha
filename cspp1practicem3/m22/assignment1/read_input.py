'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
	str=""
    lines = int(input())
    for i in range(lines):
    	str.append(input())
    	i+=1

if __name__ == '__main__':
    main()
