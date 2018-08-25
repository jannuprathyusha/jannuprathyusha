'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    str = ""
    list = []
    for i in string:
        if i not in '!@#$%^&*()':
            list = list.append(i)
            str = join(list)
    return str

            


def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
