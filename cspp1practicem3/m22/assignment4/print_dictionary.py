'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    k = list(dictionary.keys)
    v = list(dictionary.values)
    keys = k.sort()
    values = v.sort()
    for i in range dictionary(keys):
        print(keys[i] "-" values[j])




    


def main():
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
