import numpy as np

def main():
    n = int(input("Enter a number for square matrix: "))
    matrix = []
    for i in range(n):
        row = np.random.randint(1,100, n)
        matrix.append(row)
    print("Generated Matrix :")
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()
    pds = 0
    sds = 0
    for i in range(n):
        pds += matrix[i][i]
        sds += matrix[i][n - 1 - i]
    print(f"Sum of primary diagonal : {pds}")
    print(f"Sum of secondary diagonal : {sds}")
main()