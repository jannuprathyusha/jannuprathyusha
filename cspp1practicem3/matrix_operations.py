def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    matrix1_rows=len(matrix_1)
    matrix1_rows=len(matrix_1[0])
    matrix2_rows=len(matrix_2)
    matrix2_rows=len(matrix_2[0])

    result_matrix=[]
    for r in range(matrix1_rows):
    	result_matrix=[0]*
    

    result_matrix=matrix_1
    if matrix1_cols=matrix2_rows:
    	for r in range(matrix_rows):
    		for c in range(matrix2_cols):
    			for i in range(matrix2_rows):

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    res = input().split(',')
    global rows
    columns = int(res[0])
    global columns
    for r in range(rows):
    	matrix.append(list(input().strip().split(' ')))
    return matrix	
    for c in columns:
    	matrix.append()


def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    pass

if __name__ == '__main__':
    main()
