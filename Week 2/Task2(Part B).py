import numpy as np

def main():
    n = int(input("Enter a number for square matrix: "))
    matrix = []
    for i in range(n):
        row = np.random.randint(1,100, n) # generates a row of n random integers between 1 and 100
        matrix.append(row)
    print("Generated Matrix :") # printing the generated matrix
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()
    pds = 0 # primary diagonal sum
    sds = 0 # secondary diagonal sum
    for i in range(n):
        pds += matrix[i][i] # adding the elements of primary diagonal 1,1 2,2 3,3 and so on
        sds += matrix[i][n - 1 - i] # adding the elements of secondary diagonal 1,n 2,n-1 3,n-2 and so on
    print(f"Sum of primary diagonal : {pds}")
    print(f"Sum of secondary diagonal : {sds}")
main()