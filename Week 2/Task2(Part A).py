import numpy as np

def main():
    n, m = map(int, input("Enter rows and columns (e.g., 3 4): ").split()) # taking input for number of rows and columns
    matrix = []
    for i in range(m):
        row = np.random.randint(1,100, n) # generates a row of n random integers between 1 and 100
        matrix.append(row)
    print("Generated Matrix :") # printing the generated matrix
    for row in matrix:
        print(row)
    transposed_matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(matrix[j][i])) # appending the elements of the original matrix in a transposed manner
        transposed_matrix.append(row)
    print("Transposed Matrix :") # printing the transposed matrix
    for row in transposed_matrix:
        print(row)
main()