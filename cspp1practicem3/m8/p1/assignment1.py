# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one
# number and returns the factorial of given number.
# This function takes in one number and returns one number.
'"#Input integer"'
def factorial(n_num):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if n_num in (0, 1):
        return 1
    return n_num*factorial(n_num-1)
def main():
'"#output factorial"'    
    a_num = input()
    print(factorial(int(a_num)))
if __name__ == "__main__":
    main()
