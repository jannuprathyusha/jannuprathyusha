'"#Input number"'
def sumofdigits(n_num):
    '''
    n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    if n_num == 0:
        return 0
    return (n_num%10) + sumofdigits(n_num//10)
'"#Output result"'
def main():
    a_num = input()
    print(sumofdigits(int(a_num)))
if __name__ == "__main__":
    main()
